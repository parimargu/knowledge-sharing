
# 📘 API in Software Development

## ✅ What is an API?

**API** = **Application Programming Interface**

An **API** is a *set of rules or protocols that allows two software programs to talk to each other.*

In simple words:  
An API is like a **waiter in a restaurant**, who takes your order from the table (your app), delivers it to the kitchen (the server), and then brings the food back to you (the response).

---

## 🍲 Real-world Analogy: Restaurant

| **Who/What** | **Role** |
|---------------|-----------|
| You (Customer) | You place an order |
| Waiter (API)   | Takes your request to the kitchen and brings back the response |
| Kitchen (Server) | Prepares your food/data |

You never directly go into the kitchen yourself — you rely on the waiter.  
Similarly, your app does not directly access the database or server logic — it goes through an API.

---

## 🤖 Why are APIs Useful?

✅ Standardized way for software to communicate  
✅ You don’t have to know how the backend works  
✅ Faster development — reuse existing APIs  
✅ Security — only expose what’s necessary  
✅ Integration — apps/services can connect easily  

---

## 🌐 Examples of APIs

### 1️⃣ Google Maps API
Apps like Uber, Zomato, Swiggy use Google Maps API to show maps, calculate routes.

➡️ Example request:
```http
GET https://maps.googleapis.com/maps/api/directions/json?origin=A&destination=B
```
Response: Route details in JSON.

---

### 2️⃣ Weather API
To show the weather forecast in your app:
```http
GET https://api.openweathermap.org/data/2.5/weather?q=London&appid=yourkey
```
Response: Weather data.

---

### 3️⃣ Payment API
Stripe or Razorpay provides payment APIs.  
Your app sends payment details to their API and gets success/failure response.

---

## 🛠️ How to Create an API?

If you’re building your own API, you write code that:
- Exposes endpoints (like `/weather`, `/login`, `/products`)
- Accepts requests (GET, POST, PUT, DELETE…)
- Processes the request
- Returns a response (usually JSON)

---

### 🔷 Example: A Simple REST API in Python (Flask)

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy data
products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Mobile", "price": 15000}
]

# GET endpoint
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

# POST endpoint
@app.route('/products', methods=['POST'])
def add_product():
    new_product = request.json
    products.append(new_product)
    return jsonify(new_product), 201

if __name__ == '__main__':
    app.run(debug=True)
```

Run it and visit:  
📍 `http://127.0.0.1:5000/products`

---

## 🔷 Ways to Create APIs

Here are common technologies and approaches to build APIs:

| **Method**            | **Description**                | **Examples**                     |
|------------------------|--------------------------------|-----------------------------------|
| 🌐 **REST API**       | Uses HTTP methods (GET, POST)  | Flask, Django REST, Express.js   |
| 🌐 **GraphQL API**    | Flexible querying of data      | Apollo Server, Hasura            |
| 🖇️ **gRPC**          | Binary protocol, fast          | gRPC in Go, Java, Python         |
| 🛸 **WebSockets API** | For real-time communication    | Socket.IO                         |
| 🛠️ **SOAP API**      | XML-based, legacy              | Older enterprise systems         |

The most common for web/mobile apps today is **REST API** and sometimes **GraphQL**.

---

## 📌 Summary

✅ **API = interface between apps/services.**  
✅ Saves time, standardizes communication, secures your backend.  
✅ You can use APIs or build your own.  
✅ Build APIs using tools like:
- Flask, Django REST, FastAPI (Python)
- Express (Node.js)
- Spring Boot (Java)
- .NET (C#)

---


