import tkinter
p = tkinter.Tk()
p.title('First GUI')
#button = tkinter.Button(p,text='Exit',width=5,command=p.destroy)
#button.pack()

tkinter.Label(p,text='Enter your first name:').grid(row=0)
tkinter.Label(p,text='Enter your last name:').grid(row=1)
e1 = tkinter.Entry(p).grid(row=0,column=1)
e2 = tkinter.Entry(p).grid(row=1,column=1)

button = tkinter.Button(p,text='Ok',width=5,command=p.destroy).grid(row=2,column=1)
#button.pack()
'''
widgets are added here
'''
print(e1)
print(e2)
p.mainloop()