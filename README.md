# 🕒 Distributed Clock Synchronization System (DCS)

## 📌 Overview

This project implements a **Distributed Clock Synchronization System** using **UDP socket programming in Python**.
It simulates how different machines synchronize their clocks by exchanging timestamps and computing **network delay** and **clock offset**.

The system supports:

* Secure communication (encryption + hashing)
* Multi-client synchronization
* Performance analysis with graphs
* Interactive UI using Streamlit

---

## 🎯 Objectives

* Implement clock synchronization using timestamp exchange
* Simulate real-world distributed systems
* Handle multiple clients concurrently
* Ensure secure communication
* Visualize performance metrics

---

## 🏗️ System Architecture

```
Client(s)  --->  Server  --->  Client(s)
   |              |              |
   |---- T1 ----->|              |
   |              |---- T2 ----->|
   |              |---- T3 ----->|
   |<---- T4 -----|              |
```

---

## ⏱️ Timestamp Definitions

| Timestamp | Description              |
| --------- | ------------------------ |
| T1        | Client sends request     |
| T2        | Server receives request  |
| T3        | Server sends response    |
| T4        | Client receives response |

---

## 📊 Calculations

### 🔹 Network Delay

```
Delay = (T4 - T1) - (T3 - T2)
```

### 🔹 Clock Offset

```
Offset = ((T2 - T1) + (T3 - T4)) / 2
```

---

## 🔐 Security Features

* XOR-based encryption for data confidentiality
* SHA-256 hashing for data integrity verification
* Detection of tampered packets

---

## 🧵 Multi-Client Support

* Uses Python threading
* Simulates multiple clients sending requests simultaneously
* Thread-safe result handling

---

## 🌐 User Interface (Streamlit)

Features:

* Single client request
* Multi-client execution
* Display of timestamps (T1, T2, T3, T4)
* Delay and offset calculation
* Average delay computation
* Delay vs Run graph

---

## 📂 Project Structure

```
server.py         # UDP server with threading and security
client.py         # Single client logic
multi_client.py   # Multi-client (threaded execution)
ui.py             # Streamlit dashboard
```

---

## ⚙️ Requirements

* Python 3.x
* Streamlit
* Matplotlib

Install dependencies:

```
pip install streamlit matplotlib
```

---

## ▶️ How to Run

### Step 1: Start Server

```
python server.py
```

### Step 2: Run UI

```
streamlit run ui.py
```

## 📈 Output

* Real-time delay and offset
* Multi-client performance
* Graphical visualization (Delay vs Run)

---

## 🎯 Key Highlights

* UDP-based lightweight communication
* Secure message exchange
* Real-time synchronization metrics
* Modular and scalable design
* Interactive visualization

---

## 🧠 Concepts Used

* Socket Programming (UDP)
* Distributed Systems
* Multithreading
* Cryptography (Hashing & Encryption)
* Data Visualization

---

## 👨‍💻 Authors

* Valmiki Uma
* Yeshaswinie D

---

## 📌 Conclusion

This project demonstrates a complete implementation of **clock synchronization in distributed systems**, including **security, concurrency, and visualization**, making it suitable for real-world applications.

---
