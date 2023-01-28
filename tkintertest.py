
import tkinter as tk

def print_test():
    print("hello")
    
def get_text(txt_box):
    print(txt_box.get("1.0", tk.END))

def del_button(txt_box):
    txt_box.delete("1.0", tk.END)

#FIGURE OUT HOW TO ALIGN/FORMAT BUTTONS



top = tk.Tk()
top.title("bigboi")
top.geometry('400x300')



# b1= tk.Button(top, text= "print", command= lambda t= "Button-1 Clicked": get_text(text_box))
# b1.pack()


#delete button
b2 = tk.Button(top, text= "delete", command= lambda t= "Button-1 Clicked": del_button(text_box))
b2.pack()


text_box = tk.Text()
text_box.pack()

#issue with printing the name of textfield


# text_box.get("1.0")

top.mainloop()
print(name)



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
# b1= tk.Button(top, text= "Button-1", command= lambda t= "Button-1 Clicked": print_test())
# b1.pack()
# 
# entry.insert(0,"python")
# entry.insert(0, "real")

# 




#issue with printing the name of textfield



