import threading
from client import run_single_client

# ✅ MULTI-CLIENT FUNCTION
def run_multi_clients(n=5):
    results = []
    lock = threading.Lock()

    def worker(client_id):
        delay, offset, T1, T2, T3, T4 = run_single_client()
        if delay is not None:
            with lock:
                results.append(delay)

    threads = []
    for i in range(n):
        t = threading.Thread(target=worker, args=(i+1,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    return results


# Optional: run standalone
if __name__ == "__main__":
    delays = run_multi_clients(5)

    for i, d in enumerate(delays):
        print(f"Client {i+1} → Delay: {d} ms")