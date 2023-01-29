import socket
import sys
import threading
import clientController


def start():
    import start_menu
    return


start = threading.Thread(target=start)
start.start()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
messages = []
clientController.start_menu_event.wait()
host_ip, host_port, nickname = clientController.get_connection_dts()


# host_ip = input("Enter Server IP: ")
# host_port = int(input("Port: "))
# nickname = input('Enter Nickname: ')
host_port = int(host_port)
host_ip = host_ip.strip()
nickname = nickname.strip()

print([host_ip], host_port)
client.connect((host_ip, host_port))


def receive():
    while True:
        try:
            message = client.recv(1024).decode()

            if message == 'NICK':
                client.send(nickname.encode())
            elif message == '/summarize':
                pass
            elif message == '/classify':
                pass
            else:
                messages.append(message)
        except:
            print("An error has occured while receiving a message")
            client.close()
            sys.exit()
            break


def write():
    while True:
        clientController.event.wait()

        message = clientController.getMessage()
        client.send(message.encode())
        clientController.event.clear()


recieve_thread = threading.Thread(target=receive)
recieve_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
