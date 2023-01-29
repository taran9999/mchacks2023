# later on make gui responsive and resizable
# chat side buttons to go to new pages, kinda like other tabs (instead of opening a new window), each with still full chat functionality,
# while stil being able to go back to other tabs, having data there saved
# disable typing in the text field that shows text
import threading
import tkinter as tk
from datetime import datetime, time
import tkinter.ttk as ttk

import clientController
import client

messages = []


def get_text(txt_box):
    return txt_box.get("1.0", tk.END)


def clear_text(txt_box):
    txt_box.delete("1.0", tk.END)


def send_message():
    msg = get_text(text_box)
    clear_text(text_box)
    return msg.strip()


def trigger_message():
    msg = send_message()
    clientController.setMessage(msg)
    clientController.event.set()



def display_message(message):
    now = datetime.now()
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, now.strftime("%H:%M:%S") + " " + message + '\n')
    chat_history.config(state=tk.DISABLED)


def enter_send_text(text, show_txt, msg):
    text += "\n"
    if text != "\n":
        chat_history.config(state=tk.NORMAL)
        now = datetime.now()  # current date and time
        time = now.strftime("%H:%M:%S")
        # adds each text that is sent via send button to list
        messages.append(text)
        print(messages)
        show_txt.insert(tk.END, time + " " + messages[len(messages) - 1])
        # print(messages)
        # print(messages[0])
        clear_text(text_box)
        chat_history.config(state=tk.DISABLED)


# function for functionality of chat side buttons
def chat_buttons(sender_txt, show_txt, btn_txt):
    clear_text(sender_txt)
    clear_text(show_txt)
    window.title(btn_txt)
    print(messages)


def enter_press(event):
    # text_word = text_box.get("1.0",tk.END)
    # text_word = text_word.strip()
    # enter_send_text(text_word, chat_history, messages)
    trigger_message()


# FIGURE OUT HOW TO ALIGN/FORMAT BUTTONS

window = tk.Tk()
window.geometry('400x400')
style = ttk.Style(window)

window.tk.call("source", "azure dark/azure dark.tcl")
style.theme_use("azure")
window.title("Chat 1")

# text field
text_box = tk.Text()
text_box.place(x=10, y=350, height=50, width=340)

# send button
send = tk.Button(text="Send", command=lambda: trigger_message())
send.place(x=350, y=350, height=50, width=50)

# label for chat history
chat_history = tk.Text()
chat_history.place(x=0, y=0, height=350, width=400)
chat_history.config(state=tk.DISABLED)

window.bind('<Return>', enter_press)


def message_history_updater():
    previous_len = len(client.messages)
    print(previous_len)
    print(len(client.messages))

    while True:
        if previous_len != len(client.messages):
            display_message(client.messages[-1])
            previous_len = len(client.messages)


message_listener = threading.Thread(target=message_history_updater)
message_listener.start()

def launch():
    window.mainloop()

launch()


