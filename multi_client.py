import threading
from client import run_single_client

# ✅ MULTI-CLIENT FUNCTION
def run_multi_clients(n=5):
    results = []
    lock = threading.Lock()

    def worker(client_id):
        result = run_single_client()

        # ✅ Handle None safely
        if result:
            delay, offset, T1, T2, T3, T4 = result

            # ✅ Thread-safe append
            with lock:
                results.append(delay)

            print(f"Client {client_id} → Delay: {delay} ms")
            print(f"Client {client_id} → Offset: {offset} ms")

        else:
            print(f"Client {client_id} → Request failed")

    threads = []

    # Create threads
    for i in range(n):
        t = threading.Thread(target=worker, args=(i+1,))
        t.start()
        threads.append(t)

    # Wait for all threads
    for t in threads:
        t.join()

    return results


# ✅ Run standalone (optional testing)
if __name__ == "__main__":
    delays = run_multi_clients(5)

    print("\nFinal Results:")
    for i, d in enumerate(delays):
        print(f"Client {i+1} → Delay: {d} ms")