import streamlit as st
import requests

def get_available_models():
    """Fetch list of available models from Ollama."""
    try:
        url = "http://localhost:11434/api/tags"
        response = requests.get(url)
        if response.status_code == 200:
            return [model["name"] for model in response.json()["models"]]
        else:
            return ["llama3"]
    except:
        st.error("Unable to connect to Ollama. Please make sure it's running.")
        return []

def query_ollama(prompt, model):
    """Query the Ollama model with a given prompt."""
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return response.json()["response"]
        else:
            return "Error: Unable to get response from model"
    except:
        return "Error: Unable to connect to Ollama"

def summarize_text(text, model):
    """Summarize the input text using the selected model."""
    if len(text) > 1000:
        return "Error: Text is too long. Please limit to 1000 characters."
    prompt = f"Summarize the following text:\n\n{text}"
    return query_ollama(prompt, model)

def analyze_sentiment(text, model):
    """Analyze sentiment of the input text using the selected model."""
    if len(text) > 1000:
        return "Error: Text is too long. Please limit to 1000 characters."
    prompt = f"Analyze the sentiment of the following text and respond with 'Positive', 'Negative', or 'Neutral':\n\n{text}"
    return query_ollama(prompt, model)

def translate_text(text, target_lang, model):
    """Translate the input text to the target language using the selected model."""
    if len(text) > 1000:
        return "Error: Text is too long. Please limit to 1000 characters."
    prompt = f"No explanation is needed about the translation. Translate the following text to {target_lang}:\n\n{text}"
    return query_ollama(prompt, model)

# Set up Streamlit page configuration
st.set_page_config(page_title="LLM Tasks", layout="wide")

# Get available models and handle case where none are found
available_models = get_available_models()
if not available_models:
    st.error("No models available. Please pull some models in Ollama (e.g., 'ollama pull llama3').")
    st.stop()

# Sidebar for model and task selection
selected_model = st.sidebar.selectbox("Select Model", available_models)
task = st.sidebar.selectbox("Select Task", ["Summarization", "Sentiment Analysis", "Translation"])

# Summarization task
if task == "Summarization":
    st.header("Text Summarization")
    st.info("Enter text to summarize. Processing might take a few seconds.")
    text = st.text_area("Enter text to summarize", height=200)
    st.write(f"Character count: {len(text)} / 1000")
    if st.button("Summarize"):
        if text:
            with st.spinner("Summarizing..."):
                summary = summarize_text(text, selected_model)
                st.write("Summary:")
                st.write(summary)
        else:
            st.warning("Please enter some text.")

# Sentiment Analysis task
elif task == "Sentiment Analysis":
    st.header("Sentiment Analysis")
    st.info("Enter text for sentiment analysis. Processing might take a few seconds.")
    text = st.text_area("Enter text for sentiment analysis", height=200)
    st.write(f"Character count: {len(text)} / 1000")
    if st.button("Analyze"):
        if text:
            with st.spinner("Analyzing..."):
                sentiment = analyze_sentiment(text, selected_model)
                st.write("Sentiment:")
                st.write(sentiment)
        else:
            st.warning("Please enter some text.")

# Translation task
elif task == "Translation":
    st.header("Language Translation")
    st.info("Enter text to translate and select target language. Processing might take a few seconds.")
    text = st.text_area("Enter text to translate", height=200)
    st.write(f"Character count: {len(text)} / 1000")
    target_lang = st.selectbox("Select target language", ["Tamil", "Spanish", "French", "German", "Chinese"])
    if st.button("Translate"):
        if text:
            with st.spinner("Translating..."):
                translation = translate_text(text, target_lang, selected_model)
                st.write("Translation:")
                st.write(translation)
        else:
            st.warning("Please enter some text.")