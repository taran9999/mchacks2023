import threading

event = threading.Event()

message = ''



def setMessage(msg):
    global message
    message = msg


def getMessage():
    return message
