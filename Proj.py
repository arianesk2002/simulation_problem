import simpy
import numpy as np
import pandas as pd


# ---------------------------
# Random Distributions
# ---------------------------

def vehicle_interarrival_times():
    interarrival_times = [1, 2, 3, 4]
    probs = [0.25, 0.40, 0.20, 0.15]
    t = int(np.random.choice(interarrival_times, p=probs))

    if t == 1:
        rnd = np.random.randint(1, 26)
    elif t == 2:
        rnd = np.random.randint(26, 66)
    elif t == 3:
        rnd = np.random.randint(66, 86)
    else:
        rnd = np.random.randint(86, 101)

    return t, rnd


def habil_service_time_distribution():
    service = [2, 3, 4, 5]
    probs = [0.30, 0.28, 0.25, 0.17]
    t = int(np.random.choice(service, p=probs))

    ranges = {
        2: (1, 31),
        3: (31, 59),
        4: (59, 84),
        5: (84, 101)
    }
    rnd = np.random.randint(*ranges[t])
    return t, rnd


def khabaz_service_time_distribution():
    service = [3, 4, 5, 6]
    probs = [0.35, 0.25, 0.20, 0.20]
    t = int(np.random.choice(service, p=probs))

    ranges = {
        3: (1, 36),
        4: (36, 61),
        5: (61, 81),
        6: (81, 101)
    }
    rnd = np.random.randint(*ranges[t])
    return t, rnd


# ---------------------------
# Simulation Process
# ---------------------------

results = []
queue = []


def customer(env, customer_id, data, habil, khabaz):
    arrival = env.now

    queue.append(arrival)

    # ---------------- Habil ----------------
    if len(habil.queue) == 0:
        with habil.request() as req:
            yield req

            service, rnd = habil_service_time_distribution()

            start = env.now
            yield env.timeout(service)
            end = env.now

            wait = start - queue.pop(0)

            results.append([
                customer_id, rnd, data["interarrival"][customer_id - 1],
                arrival, service, start, end, "-", "-", "-", wait
            ])
            return

    # ---------------- Khabaz ----------------
    with khabaz.request() as req:
        yield req

        service, rnd = khabaz_service_time_distribution()

        start = env.now
        yield env.timeout(service)
        end = env.now

        wait = start - queue.pop(0)

        results.append([
            customer_id, rnd, data["interarrival"][customer_id - 1],
            arrival, "-", "-", "-", service, start, end, wait
        ])


# ---------------------------
# Generator
# ---------------------------

def generate(env, data, habil, khabaz, max_customers=30):
    for i in range(1, max_customers + 1):

        inter, rnd = vehicle_interarrival_times()
        data["interarrival"].append(inter)

        yield env.timeout(inter)

        env.process(customer(env, i, data, habil, khabaz))


# ---------------------------
# Main Simulation
# ---------------------------

env = simpy.Environment()

habil = simpy.Resource(env, capacity=1)
khabaz = simpy.Resource(env, capacity=1)

data = {"interarrival": []}

env.process(generate(env, data, habil, khabaz, max_customers=30))

env.run()


# ---------------------------
# Output 
# ---------------------------

columns = [
    "customer",
    "random_interarrival",
    "interarrival_time",
    "arrival_time",
    "habil_service_time",
    "habil_start",
    "habil_end",
    "khabaz_service_time",
    "khabaz_start",
    "khabaz_end",
    "waiting_time"
]

df = pd.DataFrame(results, columns=columns)

df.to_csv("simulation_results.csv", index=False)

print("Simulation completed successfully.")
print(df.head(10))