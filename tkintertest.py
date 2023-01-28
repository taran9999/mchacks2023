import tkinter as tk
top = tk.Tk()
top.title("bigboi")
top.geometry('400x300')


label = tk.Label(text="Hello, Tkinter", fg = "black", bg = "pink",  width = 10, height = 10)
button = tk.Button(
    text="Click",
    width = 25,
    height = 5,
    bg = "blue",
    fg = "yellow"
)
entry = tk.Entry(fg="yellow", bg="blue", width = 50)
label.pack()
button.pack()
entry.pack()
name = entry.get()



#issue with printing the name of textfield


top.mainloop()
print(name)
