from tkinter import *
from tkinter import ttk
root = Tk()
button = ttk.Button(root, command="buttonpressed")
button.grid()
# button.configure(text="goodby")
# button["text"] = "ok"
# button.configure(command="btn_click")
print(button.configure())




# print(button["text"])
# print(button["command"])
