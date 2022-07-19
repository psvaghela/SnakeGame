import tkinter
from tkinter import simpledialog

window = tkinter.Tk()
window.withdraw()

user_id = simpledialog.askstring(title="E-Mail",prompt="Enter your E-Mail")
password = simpledialog.askstring(title="Password",prompt="Enter Password")

print("email:",user_id)
print("password:",password)