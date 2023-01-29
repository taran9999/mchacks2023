#same theme, window for 3 text fields
#3 labels above each textfield

import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()
window.geometry('400x200')
style = ttk.Style(window)


window.tk.call("source", "azure dark/azure dark.tcl")
print(style.theme_names())
style.theme_use("azure")
# style.configure("Accentbutton", foreground='black')
window.title("Start Menu")

nickname_text = tk.Text()
nickname_text.place(x=20, y=100, height = 50, width = 100)

nickname_label = tk.Label(text= "Nickname", fg = "black", bg = "white")
nickname_label.place(x=20, y=40, height = 50, width = 100)

port_text = tk.Text()
port_text.place(x=140, y=100, height = 50, width = 100)

port_label = tk.Label(text= "Port", fg = "black", bg = "white")
port_label.place(x=140, y=40, height = 50, width = 100)

ip_text = tk.Text()
ip_text.place(x=260, y=100, height = 50, width = 100)

ip_label = tk.Label(text= "IP", fg = "black", bg = "white")
ip_label.place(x=260, y=40, height = 50, width = 100)

#button to connect
connect_button = tk.Button(text="Connect")
connect_button.place(x=140, y = 160, height = 30, width = 100 )


window.mainloop()
