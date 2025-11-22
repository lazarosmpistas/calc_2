from tkinter import *
from tkinter import ttk

root = Tk(screenName="CALC_V2", )

w = Label(root, text='CALC IS SHORT FOR CALCULATOR BTW')
w.pack()

text = StringVar()
text.set("0")
e1 = Entry(root)
e2 = Entry(root)
e1.insert(0, "First number:")
#e2.insert(0, "Second number:")
e1.pack()
e2.pack()

r = Button(root, text="exit", command=root.destroy)
r.pack()

progress_bar = ttk.Progressbar(root, orient='horizontal', length=100, mode='determinate')
progress_bar.pack()

root.mainloop()