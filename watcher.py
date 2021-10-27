from socket import socket
from os import system
from time import sleep

s = socket()

s.bind(('localhost', 50550))
s.listen(1)

while True:
    try:
        conn, addr = s.accept()
        conn.close()
    except KeyboardInterrupt:
        sleep(0.2)
    system('clear')
    system('git -P adog')

