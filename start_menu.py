#same theme, window for 3 text fields
#3 labels above each textfield
import sys
import threading
import tkinter as tk
import tkinter.ttk as ttk
import clientController

window = tk.Tk()
window.geometry('400x200')
style = ttk.Style(window)


window.tk.call("source", "azure dark/azure dark.tcl")
style.theme_use("azure")
# style.configure("Accentbutton", foreground='black')
window.title("Start Menu")


nickname_text = tk.Text()
nickname_text.place(relx=0.05, rely=0.5, relheight = 0.25, relwidth = 0.25)

nickname_label = tk.Label(text= "Nickname", fg = "black", bg = "white", font=15)
nickname_label.place(relx=0.05, rely=0.2, relheight=0.25, relwidth=0.25)

port_text = tk.Text()
port_text.place(relx=0.35, rely=0.5, relheight=0.25, relwidth = 0.25)

port_label = tk.Label(text= "Port", fg = "black", bg = "white", font=15)
port_label.place(relx=0.35, rely=0.2, relheight = 0.25, relwidth = 0.25)

ip_text = tk.Text()
ip_text.place(relx=0.65, rely=0.5, relheight=0.25, relwidth=0.25)

ip_label = tk.Label(text= "IP", fg = "black", bg = "white", font=15)
ip_label.place(relx=0.65, rely=0.2, relheight = 0.25, relwidth = 0.25)

# #button to connect
connect_button = tk.Button(text="Connect", font = 15, command=lambda: connect_btn())
connect_button.place(relx=0.35, rely = 0.8, relheight = 0.15, relwidth=0.25)


def connect_btn():
    connection_details = get_connection_details()
    clientController.set_connection_dts(connection_details)
    clientController.start_menu_event.set()
    window.destroy()
def get_connection_details():
    ip_host = ip_text.get("1.0", tk.END)

    port = port_text.get("1.0", tk.END)
    nickname = nickname_text.get("1.0", tk.END)
    return (ip_host, port, nickname)



window.mainloop()
