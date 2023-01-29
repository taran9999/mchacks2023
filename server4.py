import socket
import traceback

import select
import sys
'''Replace "thread" with "_thread" for python 3'''
from _thread import *

"""The first argument AF_INET is the address domain of the
socket. This is used when we have an Internet Domain with
any two hosts The second argument is the type of socket.
SOCK_STREAM means that data or characters are read in
a continuous flow."""
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
print("IP: " + s_ip)
# takes the first argument from command prompt as IP address
IP_address = input("Enter Server's IP address: ")

# takes second argument from command prompt as port number
Port = int(input("Enter server's port: "))

"""
binds the server to an entered IP address and at the
specified port number.
The client must be aware of these parameters
"""
server.bind((s_ip, Port))

"""
listens for 100 active connections. This number can be
increased as per convenience.
"""
server.listen(100)
list_of_clients = []

def clientthread(conn, addr):

	# sends a message to the client whose user object is conn
	conn.send("Welcome to this chatroom!".encode())

	while True:
			try:

				message = conn.recv(2048).decode().strip()


				if message:

					"""prints the message and address of the
					user who just sent the message on the server
					terminal"""
					print("<" + addr[0] + "> " + message)


					# Calls broadcast function to send message to all
					message_to_send = "<" + addr[0] + "> " + message
					broadcast(message, conn)

				else:
					"""message may have no content if the connection
					is broken, in this case we remove the connection"""
					#remove(conn)
					print("removed")
                    

			except:
				traceback.print_stack()
				continue

def serverthread(conn, addr):

	# sends a message to the client whose user object is conn
    conn.send("Welcome to this chatroom!".encode())
    
    while True:
        try:
            
            message = conn.recv(2048).decode().strip()
            message = input('Server: ')
            
            
            #broadcast(my_message, server)
            print(message)

            if message:

                """prints the message and address of the
                user who just sent the message on the server
                terminal"""
                #print("<" + addr[0] + "> " + message)


                # Calls broadcast function to send message to all
                message_to_send = "<" + addr[0] + "> " + message
                broadcast(message_to_send, conn)

            else:
                """message may have no content if the connection
                is broken, in this case we remove the connection"""
                print("removed")
                
                

        except:
            traceback.print_stack()
            continue

"""Using the below function, we broadcast the message to all
clients who's object is not the same as the one sending
the message """
def broadcast(message, connection):
    for clients in list_of_clients:
        try:
            encodedMessage = str.encode(message)
            clients.send(encodedMessage)
        except:
            clients.close()

            # if the link is broken, we remove the client
            remove(clients)
            print("error with link removing client")

"""The following function simply removes the object
from the list that was created at the beginning of
the program"""
def remove(connection):
	if connection in list_of_clients:
		list_of_clients.remove(connection)

#Server chat
con, add = server.accept()
print("Received connection from ", add[0])
print('Connection Established. Connected From: ',add[0])
list_of_clients.append(con)
start_new_thread(serverthread,(con,add))
#


while True:
    

	#"""Accepts a connection request and stores two parameters,
	#conn which is a socket object for that user, and addr
	#which contains the IP address of the client that just
	#connected"""
    
   

   

    conn, addr = server.accept()

	#"""Maintains a list of clients for ease of broadcasting
	#a message to all available people in the chatroom"""
    list_of_clients.append(conn)

	# prints the address of the user that just connected
    print (addr[0] + " connected")

	# creates and individual thread for every user
	# that connects
    start_new_thread(clientthread,(conn,addr))
    
    

conn.close()
server.close()