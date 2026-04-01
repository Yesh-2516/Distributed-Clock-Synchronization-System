import socket
import time
import json
import hashlib

SERVER_IP = "127.0.0.1"
SERVER_PORT = 8080
bufferSize = 1024
key = 123

def get_time():
    return int(time.time() * 1000)

def encrypt(data):
    return ''.join(chr(ord(c) ^ key) for c in data)

def decrypt(data):
    return ''.join(chr(ord(c) ^ key) for c in data)

# ✅ MAIN FUNCTION (used by UI & multi-client)
def run_single_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    T1 = get_time()

    request_packet = {
        "type": "REQUEST",
        "timestamp": T1
    }

    request_json = json.dumps(request_packet)

    hash_val = hashlib.sha256(request_json.encode()).hexdigest()
    final_msg = encrypt(request_json + "|" + hash_val)

    client_socket.sendto(final_msg.encode(), (SERVER_IP, SERVER_PORT))

    data, addr = client_socket.recvfrom(bufferSize)

    T4 = get_time()

    decrypted = decrypt(data.decode())

    if "|" not in decrypted:
        return None

    data_part, recv_hash = decrypted.split("|", 1)

    calc_hash = hashlib.sha256(data_part.encode()).hexdigest()
    if calc_hash != recv_hash:
        return None

    reply = json.loads(data_part)

    T2 = reply["T2"]
    T3 = reply["T3"]

    delay = (T4 - T1) - (T3 - T2)
    offset = ((T2 - T1) + (T3 - T4)) / 2

    client_socket.close()

    return delay, offset, T1, T2, T3, T4