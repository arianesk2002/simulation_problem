# 🚗 Simulation Problem (Queueing System)

A discrete-event simulation of a **two-stage service system** implemented in Python using **SimPy**. The project models customer/vehicle arrivals, service processing, and waiting times in a stochastic environment.

---

## 📌 Overview

This project simulates a real-world queueing system with:

- 🚗 Random customer/vehicle arrivals
- 🧑‍🍳 Two service stations (Habil and Khabaz)
- ⏱️ Stochastic service times
- ⏳ Queue waiting time analysis
- 📊 Final performance results stored in a structured dataset

The goal is to analyze system performance under uncertainty using simulation techniques.

---

## ⚙️ System Description

Each customer passes through the system as follows:

1. Arrives according to a random interarrival time distribution
2. Waits if service stations are busy
3. Gets served in one of the available servers:
   - **Habil (Server 1)**
   - **Khabaz (Server 2)**
4. Leaves system after service completion
5. Metrics are recorded

---

## 🧮 Key Components

### 🚗 Arrival Process
- Interarrival times: `[1, 2, 3, 4]`
- Probabilities: `[0.25, 0.40, 0.20, 0.15]`
- Each arrival is generated using a discrete probability distribution

---

### 🧑‍🍳 Service Stations

#### Habil
- Service times: `[2, 3, 4, 5]`
- Probabilities: `[0.30, 0.28, 0.25, 0.17]`

#### Khabaz
- Service times: `[3, 4, 5, 6]`
- Probabilities: `[0.35, 0.25, 0.20, 0.20]`

---

## 📊 Output Dataset

The simulation generates a table with the following columns:

| Column | Description |
|--------|-------------|
| customer | Customer ID |
| random_interarrival | Random number used for arrival generation |
| interarrival_time | Time between consecutive arrivals |
| arrival_time | Time of entering the system |
| habil_service_time | Service time at Habil |
| habil_start | Start time of service at Habil |
| habil_end | End time of service at Habil |
| khabaz_service_time | Service time at Khabaz |
| khabaz_start | Start time at Khabaz |
| khabaz_end | End time at Khabaz |
| waiting_time | Time spent waiting in queue |

---

## 📈 Performance Metrics

The system measures:

- ⏳ Average waiting time
- 🚗 Flow of customers in the system
- 🧑‍🍳 Server utilization (implicit)
- 📊 Service time distribution effects

---

## 🛠️ Requirements

- Python 3.x
- simpy
- numpy
- pandas
