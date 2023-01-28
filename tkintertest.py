
import tkinter as tk

messages = []


def print_test():
    print("hello")
    
def get_text(txt_box):
    print(txt_box.get("1.0", tk.END))

def del_button(txt_box):
    txt_box.delete("1.0", tk.END)
    
def send_text(txt_box, msg):
    #adds each text that is sent via send button to list
    messages.append(txt_box.get("1.0",tk.END))
    print(messages)
    print(messages[0])
    del_button(txt_box)
    

#FIGURE OUT HOW TO ALIGN/FORMAT BUTTONS



window = tk.Tk()
window.title("Chat")
window.geometry('400x300')




# label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
# label1.place(x=335, y=250)

#side chat buttons
chat_1 = tk.Button(text= "Chat 0").grid(row=0)
chat_2 = tk.Button(text= "Chat 1").grid(row=1)
chat_3 = tk.Button(text= "Chat 2").grid(row=2)
chat_4 = tk.Button(text= "Chat 3").grid(row=3)
chat_5 = tk.Button(text= "Chat 4").grid(row=4)
chat_6 = tk.Button(text= "Chat 5").grid(row=5)
chat_7 = tk.Button(text= "Chat 7").grid(row=6)
chat_8 = tk.Button(text= "Chat 8").grid(row=7)
chat_9 = tk.Button(text= "Chat 9").grid(row=8)
chat_10 = tk.Button(text= "Chat 10").grid(row=9)


#text field
# text_box = tk.Text().grid(row=1,column=0)




send = tk.Button(text= "send", command= lambda: send_text(text_box, messages))
# b1.place(x=320, y=240)
# 
# 
# #delete button
delete = tk.Button(text= "delete", command= lambda t= "Button-1 Clicked": del_button(text_box))
# b2.place(x=320,y=270)
# 
# 


# text_box.place(x=0,y=0)

#issue with printing the name of textfield


# text_box.get("1.0")

window.mainloop()




# label = tk.Label(text="Hello, Tkinter", fg = "black", bg = "pink",  width = 10, height = 10)
# button = tk.Button(
#     text="Click",
#     width = 25,
#     height = 5,
#     bg = "blue",
#     fg = "yellow"
# )
# entry = tk.Entry(fg="yellow", bg="blue", width = 50)
# label.pack()
# button.pack()
# entry.pack()
# 
# b1= tk.Button(window, text= "Button-1", command= lambda t= "Button-1 Clicked": print_test())
# b1.pack()
# 
# entry.insert(0,"python")
# entry.insert(0, "real")

# 




#issue with printing the name of textfield



