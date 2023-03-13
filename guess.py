import random
from tkinter import simpledialog
import tkinter

k = random.randint(1,10)
print(k)
window = tkinter.Tk()
window.withdraw()

while True:
    guess = simpledialog.askinteger(title="Number-Guess",prompt="Guess the Number:")
    if(guess == k):
        print("True....")
        break
    elif(guess>k):
    else:
        print("Try Again please....")