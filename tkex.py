from tkinter import *
from tkinter import ttk
window = Tk()
window.title('My GUI')

mainFrame = ttk.Frame(window, width=800, height=200, borderwidth=5, relief='raised').grid()
s = ttk.Style()
s.configure('Danger.TFrame', background='red', borderwidth=5, relief='raised')
dangerFrame = ttk.Frame(window, width=200, height=200, style='Danger.TFrame').grid()

window.mainloop()
