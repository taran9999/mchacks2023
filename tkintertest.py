#later on make gui responsive and resizable
#chat side buttons to go to new pages, kinda like other tabs (instead of opening a new window), each with still full chat functionality,
#while stil being able to go back to other tabs, having data there saved
#disable typing in the text field that shows text

import tkinter as tk
from datetime import datetime
import keyboard



# print("time:", time)
# print(type(time))


messages = []


def print_test():
    print("hello")
    
def get_text(txt_box):
    print(txt_box.get("1.0", tk.END))

def del_button(txt_box):
    txt_box.delete("1.0", tk.END)
    
def send_text(sender_txt, show_txt, msg):
    text = sender_txt.get("1.0",tk.END)
    if text.strip() != "":
        chat_history.config(state= tk.NORMAL)
        now = datetime.now() # current date and time
        time = now.strftime("%H:%M:%S")
        #adds each text that is sent via send button to list
        messages.append(text)
        show_txt.insert(tk.END,time + " " + messages[len(messages)-1])
        print(messages)
        # print(messages[0])
        del_button(sender_txt)
        chat_history.config(state= tk.DISABLED)

def enter_send_text(text, show_txt, msg):
    text += "\n"
    if text != "\n":
        chat_history.config(state= tk.NORMAL)
        now = datetime.now() # current date and time
        time = now.strftime("%H:%M:%S")
        #adds each text that is sent via send button to list
        messages.append(text)
        print(messages)
        show_txt.insert(tk.END,time + " " + messages[len(messages)-1])
        # print(messages)
        # print(messages[0])
        del_button(text_box)
        chat_history.config(state= tk.DISABLED)


#function for functionality of chat side buttons
def chat_buttons(sender_txt, show_txt, btn_txt):
    del_button(sender_txt)
    del_button(show_txt)
    window.title(btn_txt)
    print(messages)
    # window_chat_2 = tk.Tk()
    # window_chat_2.title("Chat 2")
    # window_chat_2.geometry('400x400')
    #print("hello")

    # window.lift()
    # window.lower()

def enter_press(event):
    text_word = text_box.get("1.0",tk.END)
    text_word = text_word.strip()
    # print(text_word.strip())
    enter_send_text(text_word, chat_history, messages)
    # print(type(text_box))
    # print(text_box)

    # send_text(text_box-"\n",chat_history,messages)
    #issue w extra line


#FIGURE OUT HOW TO ALIGN/FORMAT BUTTONS



window = tk.Tk()
window.tk.call("C:\Users\Vincent\Downloads\Azure-ttk-theme-main\Azure-ttk-theme-main" , "azure.tcl") 
window.title("Chat 1")
window.geometry('400x400')






# label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
# label1.place(x=335, y=250)

#side chat buttons


chat_1= tk.Button(text= "Chat 1")
chat_1.place(x=0, y=0, height = 50, width = 100)

chat_2 = tk.Button(text= "Chat 2")
chat_2.place(x=0, y=50, height = 50, width = 100)

chat_3 = tk.Button(text= "Chat 3")
chat_3.place(x=0, y=100, height = 50, width = 100)

chat_4 = tk.Button(text= "Chat 4")
chat_4.place(x=0, y=150, height = 50, width = 100)

chat_5 = tk.Button(text= "Chat 5")
chat_5.place(x=0, y=200, height = 50, width = 100)

chat_6 = tk.Button(text= "Chat 6")
chat_6.place(x=0, y=250, height = 50, width = 100)

chat_7 = tk.Button(text= "Chat 7")
chat_7.place(x=0, y=300, height = 50, width = 100)

chat_8 = tk.Button(text= "Chat 8")
chat_8.place(x=0, y=350, height = 50, width = 100)

# chat_2 = tk.Button(text= "Chat 1").grid(row=1)
# chat_3 = tk.Button(text= "Chat 2").grid(row=2)
# chat_4 = tk.Button(text= "Chat 3").grid(row=3)
# chat_5 = tk.Button(text= "Chat 4").grid(row=4)
# chat_6 = tk.Button(text= "Chat 5").grid(row=5)
# chat_7 = tk.Button(text= "Chat 7").grid(row=6)
# chat_8 = tk.Button(text= "Chat 8").grid(row=7)
# chat_9 = tk.Button(text= "Chat 9").grid(row=8)
# chat_10 = tk.Button(text= "Chat 10").grid(row=9)

# frame= tk.Frame(window, width=30, height=10)
# tbox1 = tk.Text(frame)
# tbox1.place(x=50, y=50, height=10, width=10)
#text field
text_box = tk.Text()
text_box.place(x=100, y=350, height = 40, width = 250)
# text_box.bind("<Key>", click)


# delete = tk.Button(text= "delete", command= lambda t= "Button-1 Clicked": del_button(text_box))
# delete.place(x=350, y=350, height = 25, width = 50)

# delete.place(x=300,y=350, height = 50, width = 100)

#send button
send = tk.Button(text= "Send", command= lambda: send_text(text_box, chat_history, messages))
send.place(x=350, y=350, height = 50, width = 50)
print(text_box)

#label for chat history
chat_history = tk.Text()
chat_history.place(x=100, y=0, height = 350, width = 300)
chat_history.config(state= tk.DISABLED)

#fix enter check
# if messages[-1]

# if text_box:
#     print("enter")
#     send_text(text_box,chat_history,messages)

# print("helo" + text_box.get("1.0",tk.END))

# send.place(x=200, y=350, height = 50, width = 100)



# text_box.place(x=0,y=0)

#issue with printing the name of textfield


# text_box.get("1.0")
window.bind('<Return>', enter_press)

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



