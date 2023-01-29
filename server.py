import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)

print("Server IP: " + host_ip)
port = int(input("Enter Port: "))

server_socket.bind((host_ip, port))
server_socket.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(index)
            client.close()
            broadcast((nicknames[index] + " has left the chat").encode())
            nicknames.remove(index)
            break

def receive():
    while True:
        client, address = server_socket.accept()
        print("Connected with" + str(address))

        client.send('NICK'.encode())
        nickname = client.recv(1024).decode()
        nicknames.append(nickname)
        clients.append(client)

        print('Nickname of the client is: ' + nickname)
        broadcast((nickname + 'has joined the chat').encode())
        client.send('connected to the server'.encode())

        thread = threading.Thread(target=handle, args=(client, ))
        thread.start()


print('Server is starting!')
receive()


