import streamlit as st
from groq import Groq

# Set up Groq client with error handling for missing API key
try:
    #client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    # llm_credentials - GROQ_API_KEY
    client = Groq(api_key=st.secrets.llm_credentials.GROQ_API_KEY)
except KeyError:
    st.error("Please set the GROQ_API_KEY in your Streamlit secrets. For local testing, add it to .streamlit/secrets.toml as GROQ_API_KEY='your_key_here'. For deployment on Streamlit Cloud, set it in the app settings.")
    st.stop()

# Define available models and tasks
models = ["llama3-70b-8192", "mixtral-8x7b-32768", "gemma-7b-it"]
tasks = ["Summarization", "Sentiment Analysis", "Translation"]

# Sidebar for model and task selection
st.sidebar.title("Settings")
selected_model = st.sidebar.selectbox("Select Model", models)
selected_task = st.sidebar.selectbox("Select Task", tasks)

# Helper function to query Groq API with custom system message
def query_groq(prompt, model, system_message="You are a helpful assistant."):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1024,
            temperature=0.5,
        )
        print(system_message)
        print("\n")
        print(prompt)
        print("\n")
        print(response.choices[0])
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Task-specific functions
def summarize_text(text, model):
    system_message = "You are a helpful assistant that summarizes text."
    prompt = f"Summarize the following text:\n\n{text}"
    return query_groq(prompt, model, system_message)

def analyze_sentiment(text, model):
    system_message = "You are a helpful assistant that analyzes sentiment."
    prompt = f"Analyze the sentiment of the following text and respond with 'Positive', 'Negative', or 'Neutral':\n\n{text}"
    return query_groq(prompt, model, system_message)

def translate_text(text, target_lang, model):
    system_message = "You are a helpful assistant that translates text."
    prompt = f"Translate the following text to {target_lang}:\n\n{text}"
    return query_groq(prompt, model, system_message)

# Main application logic based on selected task
if selected_task == "Summarization":
    st.header("Text Summarization")
    st.info("Enter text to summarize. The summary will be generated using the selected model.")
    default_text = "The rapid advancement of artificial intelligence has transformed industries worldwide. From healthcare to finance, AI systems are improving efficiency and accuracy. However, concerns about job displacement and ethical implications remain significant."
    text = st.text_area("Enter text to summarize", height=200, value=default_text)
    st.write(f"Character count: {len(text)} / 5000")
    if st.button("Summarize"):
        if not text.strip():
            st.warning("Please enter some text.")
        elif len(text) > 5000:
            st.warning("Text is too long. Please limit to 5000 characters.")
        else:
            with st.spinner("Summarizing..."):
                summary = summarize_text(text, selected_model)
                if summary.startswith("Error:"):
                    st.error(summary)
                else:
                    st.write("**Summary:**")
                    st.write(summary)

elif selected_task == "Sentiment Analysis":
    st.header("Sentiment Analysis")
    st.info("Enter text for sentiment analysis. The sentiment will be analyzed using the selected model.")
    default_text = "I absolutely love this product! It works flawlessly and exceeded my expectations."
    text = st.text_area("Enter text for sentiment analysis", height=200, value=default_text)
    st.write(f"Character count: {len(text)} / 5000")
    if st.button("Analyze"):
        if not text.strip():
            st.warning("Please enter some text.")
        elif len(text) > 5000:
            st.warning("Text is too long. Please limit to 5000 characters.")
        else:
            with st.spinner("Analyzing..."):
                sentiment = analyze_sentiment(text, selected_model)
                if sentiment.startswith("Error:"):
                    st.error(sentiment)
                else:
                    st.write("**Sentiment:**")
                    st.write(sentiment)

elif selected_task == "Translation":
    st.header("Language Translation")
    st.info("Enter text to translate and select the target language. The translation will be generated using the selected model.")
    default_text = "Hello, how are you today?"
    text = st.text_area("Enter text to translate", height=200, value=default_text)
    st.write(f"Character count: {len(text)} / 5000")
    languages = ["Tamil", "Spanish", "French", "German", "Chinese", "Japanese", "Russian"]
    target_lang = st.selectbox("Select target language", languages)
    if st.button("Translate"):
        if not text.strip():
            st.warning("Please enter some text.")
        elif len(text) > 5000:
            st.warning("Text is too long. Please limit to 5000 characters.")
        else:
            with st.spinner("Translating..."):
                translation = translate_text(text, target_lang, selected_model)
                if translation.startswith("Error:"):
                    st.error(translation)
                else:
                    st.write("**Translation:**")
                    st.write(translation)