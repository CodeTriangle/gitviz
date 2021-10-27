from socket import socket

s = socket()

print("Starting git watcher...")
s.bind(('localhost', 50550))
s.listen(1)
print("Listening on port 50550.")

while True:
    print("Waiting for connection...")
    conn, addr = s.accept()
    print(f"Got connection: {addr[0]}:{addr[1]}")

    conn.close()
