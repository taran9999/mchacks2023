import threading

event = threading.Event()

message = ''

connection_dts = ()

def set_connection_dts(connection):
    global connection_dts
    connection_dts = connection

def get_connection_dts():
    return connection_dts

start_menu_event = threading.Event()




def setMessage(msg):
    global message
    message = msg


def getMessage():
    return message
