import socket
import json
import time
import threading
import hashlib

localIP     = "127.0.0.1"
localPort   = 8080
bufferSize  = 1024
key = 123

UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

def encrypt(data):
    return ''.join(chr(ord(c) ^ key) for c in data)

def decrypt(data):
    return ''.join(chr(ord(c) ^ key) for c in data)

def handle_client(message, address):
    try:
        decrypted = decrypt(message.decode())

        # ✅ Safe split
        if "|" not in decrypted:
            print("Invalid message format, skipping...")
            return

        data_part, recv_hash = decrypted.split("|", 1)

        # Integrity check
        calc_hash = hashlib.sha256(data_part.encode()).hexdigest()
        if calc_hash != recv_hash:
            print("Data tampered! Ignoring request.")
            return

        request = json.loads(data_part)

        if request.get("type") != "REQUEST":
            print("Unknown request type")
            return

        T1 = request["timestamp"]

        # Server timestamps
        T2 = int(time.time() * 1000)
        time.sleep(0.001)
        T3 = int(time.time() * 1000)

        response = {
            "T2": T2,
            "T3": T3
        }

        response_json = json.dumps(response)

        hash_val = hashlib.sha256(response_json.encode()).hexdigest()
        final_msg = encrypt(response_json + "|" + hash_val)

        UDPServerSocket.sendto(final_msg.encode(), address)

        print(f"\n[CLIENT {address}]")
        print(f"T1: {T1}")
        print(f"T2: {T2}")
        print(f"T3: {T3}")

    except Exception as e:
        print("Error:", e)


while True:
    try:
        message, address = UDPServerSocket.recvfrom(bufferSize)
        threading.Thread(target=handle_client, args=(message, address), daemon=True).start()
    except Exception as e:
        print("Server error:", e)