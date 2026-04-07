# 🕒 Distributed Clock Synchronization System (DCS)

## Overview

This project implements a **Distributed Clock Synchronization System** using **UDP socket programming in Python**.
It simulates how different machines synchronize their clocks by exchanging timestamps and computing **network delay** and **clock offset**.

The system supports:

* Secure communication (encryption + hashing)
* Multi-client synchronization
* Performance analysis with graphs
* Interactive UI using Streamlit

---

## Problem Statement

To design and implement a distributed clock synchronization system that minimizes time differences between clients using UDP communication, while ensuring secure and efficient message exchange.

---

## Objectives

* Implement clock synchronization using timestamp exchange
* Simulate real-world distributed systems
* Handle multiple clients concurrently
* Ensure secure communication
* Visualize performance metrics

---

## System Architecture

```
Client(s)  --->  Server  --->  Client(s)
   |              |              |
   |---- T1 ----->|              |
   |              |---- T2 ----->|
   |              |---- T3 ----->|
   |<---- T4 -----|              |
```

---

## Timestamp Definitions

| Timestamp | Description              |
| --------- | ------------------------ |
| T1        | Client sends request     |
| T2        | Server receives request  |
| T3        | Server sends response    |
| T4        | Client receives response |

---

## Calculations

### Network Delay

```
Delay = (T4 - T1) - (T3 - T2)
```

### Clock Offset

```
Offset = ((T2 - T1) + (T3 - T4)) / 2
```

---

## Security Features

* XOR-based encryption for data confidentiality
* SHA-256 hashing for data integrity verification
* Detection of tampered packets

---

## Multi-Client Support

* Uses Python threading
* Simulates multiple clients sending requests simultaneously
* Thread-safe result handling

---

## User Interface (Streamlit)

Features:

* Single client request
* Multi-client execution
* Display of timestamps (T1, T2, T3, T4)
* Delay and offset calculation
* Average delay computation
* Delay vs Run graph

---

## Project Structure

```
server.py         # UDP server with threading and security
client.py         # Single client logic
multi_client.py   # Multi-client (threaded execution)
ui.py             # Streamlit dashboard
```

---

## Requirements

* Python 3.x
* Streamlit
* Matplotlib

Install dependencies:

```
pip install streamlit matplotlib
```

---

## How to Run

### Step 1: Start Server

```
python server.py
```

### Step 2: Run UI

```
streamlit run ui.py
```

## Output

* Real-time delay and offset
  <img width="1365" height="592" alt="image" src="https://github.com/user-attachments/assets/666daf96-2294-463f-aa15-8023ae317e06" />

* Multi-client performance
  <img width="1365" height="718" alt="image" src="https://github.com/user-attachments/assets/964955ba-409b-4a57-b8a4-79ae5af21bd1" />

* Graphical visualization (Delay vs Run)
  <img width="1365" height="718" alt="image" src="https://github.com/user-attachments/assets/36720e44-4cc4-44d1-a3e7-a6dafaf50a5e" />

<img width="1365" height="721" alt="image" src="https://github.com/user-attachments/assets/eec7c67e-eb09-4d62-bf5f-beedb173fe17" />

---
## Performance Analysis

###  Latency (Delay) Analysis

#### Single Client

* Delay ≈ **2 ms**
* Offset ≈ **1.0 ms**

This indicates very low latency and efficient communication between client and server.

---

#### Multi-Client (5 Clients)

| Client   | Delay (ms) |
| -------- | ---------- |
| Client 1 | 4 ms       |
| Client 2 | 3 ms       |
| Client 3 | 2 ms       |
| Client 4 | 2 ms       |
| Client 5 | 3 ms       |

👉 **Average Delay ≈ 2.67 ms**

---

### Observations

* All delays fall within **2–4 ms**, indicating fast system response
* Slight increase in delay observed under multi-client load due to concurrent processing
* No extreme spikes or irregularities observed

 The system maintains **stable performance under load**

---

### Graph Analysis (Delay vs Run)

* Minimum delay → **2 ms**
* Maximum delay → **4 ms**
* Most values cluster around **2–3 ms**

 This shows:
* Consistent performance
* Minimal jitter
* No network instability

---

### Clock Offset Analysis

| Client   | Offset (ms) |
| -------- | ----------- |
| Client 1 | 1.0         |
| Client 2 | 0.5         |
| Client 3 | 1.0         |
| Client 4 | 1.0         |
| Client 5 | 1.5         |

Observations:
* Offset remains **very low (< 2 ms)**
* Indicates accurate clock synchronization

---

### Concurrency Performance

* Server successfully handled multiple clients simultaneously
* No packet loss or crashes observed
* All responses processed correctly

 Demonstrates effective use of **multithreading**

---

### Overall System Performance

* Low latency ✔
* Low clock offset ✔
* Stable behavior ✔
* Efficient multi-client handling ✔

 **Conclusion:**
The system demonstrates efficient and reliable clock synchronization with minimal delay and high stability under concurrent load. It is suitable for small-scale distributed systems and real-time synchronization scenarios.

---

## Key Highlights

* UDP-based lightweight communication
* Secure message exchange
* Real-time synchronization metrics
* Modular and scalable design
* Interactive visualization

---

## Concepts Used

* Socket Programming (UDP)
* Distributed Systems
* Multithreading
* Cryptography (Hashing & Encryption)
* Data Visualization

---

## Authors

* Valmiki Uma
* Yeshaswinie D

---

## Conclusion

This project demonstrates a complete implementation of clock synchronization in distributed systems, including security, concurrency, and visualization, making it suitable for real-world applications.

---
