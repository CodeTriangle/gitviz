from socket import socket
from os import system

s = socket()

s.bind(('localhost', 50550))
s.listen(1)

while True:
    conn, addr = s.accept()
    system('clear')
    system('git -P adog')

    conn.close()
