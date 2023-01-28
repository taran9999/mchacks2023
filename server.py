import socket
import sys
import time

new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
port = 8080

new_socket.bind((host_name, port))
print("Binding successful")
print("IP: " + s_ip)

name = input("Enter name: ")
new_socket.listen(1)

conn, add = new_socket.accept()
print("Rececived connection from: " + add[0])
print("Connection established from: " + add[0])

client = conn.recv(1024).decode()
print(client + " has connected")
conn.send(name.encode())

while True:
    message = input("Send message: ")
    conn.send(message.encode())
    message = conn.recv(1024).decode()
    print(client + ": " + message)