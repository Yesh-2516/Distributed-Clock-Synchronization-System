import streamlit as st
import matplotlib.pyplot as plt
from client import run_single_client
from multi_client import run_multi_clients

st.title("🕒 Clock Synchronization Dashboard")

# Store delays
if "delays" not in st.session_state:
    st.session_state.delays = []

# ✅ Single Client
if st.button("Single Client Request"):
    result = run_single_client()

    if result:
        delay, offset, T1, T2, T3, T4 = result

        st.session_state.delays.append(delay)

        st.subheader("📌 Timestamps")
        st.write(f"T1 (Client Send): {T1}")
        st.write(f"T2 (Server Receive): {T2}")
        st.write(f"T3 (Server Send): {T3}")
        st.write(f"T4 (Client Receive): {T4}")

        st.subheader("📊 Results")
        st.write(f"Delay: {delay} ms")
        st.write(f"Offset: {offset} ms")

    else:
        st.error("Error in response")

# ✅ Multi Client
if st.button("Run Multiple Clients (5)"):
    results = run_multi_clients(5)

    st.session_state.delays.extend(results)

    st.subheader("📊 Multi-client Results")
    for i, d in enumerate(results):
        st.write(f"Client {i+1} → Delay: {d} ms")

# ✅ Average Delay
if st.session_state.delays:
    avg_delay = sum(st.session_state.delays) / len(st.session_state.delays)
    st.subheader("📈 Average Delay")
    st.write(f"{avg_delay:.2f} ms")

# ✅ Graph
if st.button("Show Delay Graph"):
    if st.session_state.delays:
        fig, ax = plt.subplots()
        ax.plot(range(1, len(st.session_state.delays)+1),
                st.session_state.delays, marker='o')
        ax.set_xlabel("Run Number")
        ax.set_ylabel("Delay (ms)")
        ax.set_title("Delay vs Run")
        ax.grid()

        st.pyplot(fig)
    else:
        st.warning("No data available")

# ✅ Clear
if st.button("Clear Data"):
    st.session_state.delays = []
    st.success("Data cleared")