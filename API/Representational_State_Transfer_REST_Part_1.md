## What is Representational State Transfer (REST)?

**REST (Representational State Transfer)** is an architectural style for designing networked applications, especially web APIs. It was defined by Roy Fielding in 2000 in his PhD dissertation.

At its core, REST is about:

> **Using standard web principles (like HTTP) to manipulate resources in a simple, scalable, and stateless way.**

---

# 1️⃣ Key Concepts of REST

Let’s break this down clearly.

## 1. Resource-Based

In REST, **everything is a resource**.

A resource can be:

* A user
* A product
* An order
* A blog post
* A file

Each resource is identified by a **URL**.

Example:

```
/users/123
/products/45
/orders/999
```

Think of a resource as a *noun*, not a verb.

---

## 2. Representation

When you request a resource, you don’t get the actual object — you get a **representation** of it.

Common formats:

* JSON
* XML
* HTML

Example:

Request:

```
GET /users/123
```

Response:

```json
{
  "id": 123,
  "name": "Alice",
  "email": "alice@example.com"
}
```

That JSON is a *representation* of the user.

---

## 3. Statelessness

REST is **stateless**.

This means:

* The server does NOT remember previous requests.
* Each request must contain all the information needed.

If you authenticate, the token must be sent in **every request**.

Example:

```
GET /orders
Authorization: Bearer xyz123
```

The server does not remember you logged in earlier.

---

## 4. Standard HTTP Methods

REST uses standard HTTP verbs to operate on resources:

| HTTP Method | Meaning          | Example      |
| ----------- | ---------------- | ------------ |
| GET         | Retrieve data    | Get user     |
| POST        | Create           | Create user  |
| PUT         | Update (full)    | Update user  |
| PATCH       | Update (partial) | Change email |
| DELETE      | Remove           | Delete user  |

Example:

```
POST /users
PUT /users/123
DELETE /users/123
```

---

## 5. Uniform Interface

REST requires a consistent, predictable interface:

* Resources identified by URL
* Standard HTTP methods
* Standard status codes (200, 404, 500)
* Clear structure

---

## 6. Client-Server Separation

* Client handles UI.
* Server handles data.
* They are independent.

---

# 🏪 Real-World Analogy: Restaurant

Let’s imagine a restaurant.

### 🍽 The Menu = API Documentation

It lists what you can order (available resources).

---

### 🧾 Each Dish = Resource

* `/pizza/1`
* `/drinks/5`
* `/desserts/2`

Each item is uniquely identifiable.

---

### 🗣 You Place an Order = HTTP Request

You say:

> “I want pizza #1”

That’s:

```
GET /pizza/1
```

---

### 🍕 The Dish You Receive = Representation

You don’t get the recipe or kitchen.
You get the **prepared dish**.

Just like you don’t get the database record — you get JSON.

---

### 📦 Statelessness in Restaurant

Imagine:

* Every time you talk to the waiter, you must repeat your table number.
* The waiter does NOT remember your previous conversation.

Each interaction is independent.

That’s REST statelessness.

---

### 🔄 Different Actions (HTTP Methods)

| Restaurant Action | REST Equivalent |
| ----------------- | --------------- |
| Ask for menu item | GET             |
| Order new dish    | POST            |
| Change your order | PUT/PATCH       |
| Cancel order      | DELETE          |

---

# 🚫 What is NOT REST?

Now this is important.

Just because something uses HTTP does NOT mean it is REST.

---

## ❌ 1. RPC over HTTP

Example:

```
/getUser
/createUser
/deleteUser
```

This is RPC-style (Remote Procedure Call).

Why it's NOT REST:

* URLs represent actions (verbs), not resources.
* Violates resource-based design.

REST prefers:

```
GET /users/123
POST /users
DELETE /users/123
```

---

## ❌ 2. Stateful APIs

If the server remembers your session without requiring full request context:

Example:

* Login once
* Server stores session
* Future requests rely on server memory

That breaks REST stateless constraint.

---

## ❌ 3. Ignoring HTTP Methods

Bad example:

```
POST /deleteUser/123
POST /getUser/123
```

Everything using POST = not RESTful design.

---

## ❌ 4. Single Endpoint for Everything

Example:

```
POST /api
{
  "action": "deleteUser",
  "id": 123
}
```

This is NOT REST.
This is RPC tunneled over HTTP.

---

## ❌ 5. SOAP Web Services

SOAP:

* Uses XML
* Uses single endpoint
* Action-driven
* Heavy protocol

SOAP is NOT REST.

---

# ⚖️ REST vs Not REST (Quick Comparison)

| REST                             | Not REST                        |
| -------------------------------- | ------------------------------- |
| Resource-based URLs              | Action-based URLs               |
| Uses HTTP verbs properly         | Uses POST for everything        |
| Stateless                        | Stateful sessions               |
| Multiple endpoints for resources | Single endpoint for all actions |
| Lightweight (JSON)               | Heavy (SOAP XML)                |

---

# 🧠 Another Real-World Analogy: Library

## RESTful Library

You:

* Go to shelf `/books/123`
* Ask librarian to fetch it (GET)
* Add new book (POST)
* Replace book (PUT)
* Remove book (DELETE)

Each book has:

* Unique location
* Standard interaction rules

Everything is organized around **resources (books)**.

---

## Non-REST Library

Instead of shelves:

You go to one desk and say:

* “Execute getBook”
* “Execute deleteBook”
* “Execute updateBook”

The librarian acts based on verbs.

This is RPC-style, not RESTful.

---

# 🎯 Why REST Became Popular

* Simple
* Scalable
* Works naturally with HTTP
* Easy to cache
* Easy to integrate
* Language-agnostic

---

# 🏁 Final Summary

### REST IS:

* Resource-oriented
* Stateless
* Uses HTTP methods properly
* Has uniform interface
* Client-server separated
* Returns representations (JSON/XML)

### REST IS NOT:

* Action/verb-based URLs
* Stateful session-based systems
* Single endpoint with action parameter
* SOAP services
* POST-for-everything APIs

---
