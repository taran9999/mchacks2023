import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
messages = []

host_ip = input("Enter Sever IP: ")
host_port = int(input("Port: "))
client.connect((host_ip, host_port))

nickname = input('Enter Nickname: ')

def receive():
    while True:
        try:
            message = client.recv(1024).decode()

            if message == 'NICK':
                client.send(nickname.encode())
            elif message == '/summarize':
                pass
            elif message == '/sentiment':
                pass
            else:
                print(message)
                messages.append(message)
        except:
            print("An error has occured while receiving a message")
            client.close()
            break

def write():
    while True:
        message = nickname + ': ' + input()
        client.send(message.encode())

recieve_thread = threading.Thread(target=receive)
recieve_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()