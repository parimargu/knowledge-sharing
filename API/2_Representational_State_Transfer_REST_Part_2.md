We’ll cover:

1. REST vs GraphQL
2. REST vs gRPC
3. Richardson Maturity Model (Levels 0–3)
4. HATEOAS (the most misunderstood REST constraint)

---

# 1️⃣ REST vs GraphQL

## 🔹 Core Philosophy Difference

| REST                              | GraphQL                           |
| --------------------------------- | --------------------------------- |
| Many endpoints                    | Single endpoint                   |
| Server defines response structure | Client defines response structure |
| Multiple requests often needed    | Usually single request            |
| Uses HTTP semantics heavily       | Uses HTTP as transport only       |

---

## 🏪 Real-World Analogy: Restaurant

### 🍽 REST Restaurant

You order from predefined menu items.

You say:

> “Give me combo meal #5.”

You get:

* Burger
* Fries
* Coke

Even if you only wanted fries.

If you want:

* Just fries → separate request
* Just drink → separate request

Server decides what’s included in the meal.

---

### 🧠 GraphQL Restaurant

You build your own meal.

You say:

> “I want burger patty only, no bun, plus two sauces, and only half fries.”

The kitchen prepares **exactly what you asked for**.

Client controls the data shape.

---

## 🔍 Example

### REST

```
GET /users/1
```

Response:

```json
{
  "id": 1,
  "name": "Alice",
  "email": "alice@email.com",
  "address": {...},
  "orders": [...]
}
```

You might not need all fields → over-fetching.

To get orders separately:

```
GET /users/1/orders
```

Multiple round trips.

---

### GraphQL

Single endpoint:

```
POST /graphql
```

Query:

```graphql
{
  user(id: 1) {
    name
    orders {
      total
    }
  }
}
```

You get **exactly**:

```json
{
  "data": {
    "user": {
      "name": "Alice",
      "orders": [
        {"total": 200}
      ]
    }
  }
}
```

---

## ⚖️ When to Use What?

### Use REST When:

* Simple CRUD systems
* Public APIs
* Caching important
* Standard HTTP behavior needed

### Use GraphQL When:

* Mobile apps (bandwidth sensitive)
* Complex nested data
* Many UI variations
* Need flexible querying

---

# 2️⃣ REST vs gRPC

## 🔹 Core Difference

| REST                       | gRPC                            |
| -------------------------- | ------------------------------- |
| Text-based (JSON)          | Binary (Protocol Buffers)       |
| HTTP/1.1 or HTTP/2         | HTTP/2 only                     |
| Human-readable             | Not human-readable              |
| Web-friendly               | Internal microservices friendly |
| Stateless request-response | Supports streaming              |

---

## 🚚 Real-World Analogy: Postal Service vs Private Courier

### REST = Postal Service

* Uses standard format (envelope + address)
* Anyone can send/receive
* Slower but universal
* Easy to read letter content

Good for:

* Public APIs
* Web browsers

---

### gRPC = High-Speed Corporate Courier

* Uses compressed packages
* Extremely fast
* Structured packaging rules
* Only trained systems understand format

Good for:

* Microservices communication
* High performance systems
* Internal service-to-service calls

---

## 🧠 Example

### REST

```
GET /orders/123
```

Response:

```json
{
  "id": 123,
  "amount": 450
}
```

---

### gRPC

You define:

```
service OrderService {
  rpc GetOrder(OrderRequest) returns (OrderResponse);
}
```

Binary encoded, ultra-fast.

---

## 🚀 When to Use gRPC

* 100+ microservices
* Real-time streaming
* Financial systems
* High throughput systems

---

# 3️⃣ Richardson Maturity Model (How RESTful Are You?)

This model defines **4 levels of REST maturity**.

---

## 🧱 Level 0 — The Swamp of POX

Single endpoint.

```
POST /api
{
  "action": "createUser"
}
```

Like going to a government office and saying:

> “Process this request.”

Everything goes through one counter.

Not REST.

---

## 🧱 Level 1 — Resources Introduced

Now we have:

```
/users
/orders
```

But still:

```
POST /users/delete
```

Resources exist, but HTTP verbs not properly used.

---

## 🧱 Level 2 — Proper HTTP Verbs

Now:

```
GET /users/1
POST /users
PUT /users/1
DELETE /users/1
```

Uses:

* Proper status codes
* Proper verbs

This is where **most APIs stop**.

---

## 🧱 Level 3 — HATEOAS (True REST)

Now responses include navigation links.

Example:

```json
{
  "id": 1,
  "name": "Alice",
  "links": [
    { "rel": "self", "href": "/users/1" },
    { "rel": "orders", "href": "/users/1/orders" }
  ]
}
```

Client discovers actions dynamically.

---

## 🏨 Real-World Analogy: Hotel

### Level 0

One counter. Ask for everything.

### Level 1

Different departments exist.

### Level 2

You use correct forms for each department.

### Level 3

Hotel gives you brochure:

* Restaurant → Floor 2
* Spa → Floor 3
* Checkout → Lobby

You don’t guess URLs. You follow guidance.

---

# 4️⃣ HATEOAS (Hypermedia as the Engine of Application State)

This is the most misunderstood REST constraint.

---

## 🧠 What It Means

Server response should tell the client:

* What can I do next?
* Where can I go next?

Client should not hardcode URLs.

---

## 🔹 Without HATEOAS

Client knows:

```
GET /users/1/orders
```

Hardcoded.

If URL changes → client breaks.

---

## 🔹 With HATEOAS

Server sends:

```json
{
  "id": 1,
  "name": "Alice",
  "links": [
    {
      "rel": "orders",
      "href": "/customers/1/purchases"
    }
  ]
}
```

Client just follows link.

Server can change internal structure without breaking client.

---

## 🌍 Real-World Analogy: Google Maps

Without HATEOAS:
You memorize every road manually.

With HATEOAS:
GPS tells you:

* Turn left
* Take highway
* Exit 14

You follow dynamic navigation.

---

# 🏁 Final Big Picture

| Concept          | Think Of It As                      |
| ---------------- | ----------------------------------- |
| REST             | Standard restaurant ordering system |
| GraphQL          | Customizable meal builder           |
| gRPC             | High-speed internal courier         |
| Richardson Model | REST maturity scale                 |
| HATEOAS          | GPS navigation for APIs             |

---

# 🎯 Ultimate Understanding

REST is not just:

* JSON
* HTTP
* CRUD

True REST means:

* Resource-based design
* Statelessness
* Proper HTTP usage
* Hypermedia navigation (HATEOAS)

Most APIs today are:
👉 Level 2 REST (not full REST)

---
