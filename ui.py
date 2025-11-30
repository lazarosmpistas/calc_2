from tkinter import *
from tkinter import ttk
from customtkinter import *
from customtkinter import CTkProgressBar
import calc


def call_compute(num1, num2, operator):
    if not calc.checks(num1, num2, operator):
        return "Invalid input my sister/brother!"
    else:
        num1, num2 = calc.process(num1, num2)
        result = calc.operation(num1, num2, operator)
        calc.log_results(num1, num2, operator, result)

root = CTk(screenName="CALC_V2", )
set_appearance_mode('dark')
root.geometry("500x300")

frame_header = CTkFrame(master=root)
frame_header.pack(expand=True, fill=BOTH)

w = CTkLabel(frame_header, text='CALC IS SHORT FOR CALCULATOR BTW')
w.pack(expand=True, fill=BOTH)

frame_operation = CTkFrame(master=root)
frame_operation.pack(expand=True, fill=BOTH)

b_num1 = CTkEntry(frame_operation, placeholder_text="Number 1")
b_num1.grid(row=0, column=0)
b_operand = CTkEntry(frame_operation, placeholder_text="Operation")
b_operand.grid(row=0, column=1)
b_num2 = CTkEntry(frame_operation, placeholder_text="Number 2")
b_num2.grid(row=0, column=2)

b1 = CTkButton(master=frame_operation, text="1", width=28, height=28)
b1.grid(row=1, column=0, pady=10)
#b1.pack(side=LEFT, expand=True)

b2 = CTkButton(master=frame_operation, text="2", width=28, height=28)
b2.grid(row=1, column=1, padx=10)
#b2.pack(expand=True, side=BOTTOM)

b3 = CTkButton(master=frame_operation, text="3", width=28, height=28)
b3.grid(row=1, column=2)
#b3.pack(side=RIGHT, expand=True)

b4 = CTkButton(master=frame_operation, text="4", width=28, height=28)
b4.grid(row=2, column=0, pady=10)
#b4.pack(side=LEFT, expand=True)

b5 = CTkButton(master=frame_operation, text="5", width=28, height=28)
b5.grid(row=2, column=1)
#b5.pack(expand=True, side=BOTTOM)

b6 = CTkButton(master=frame_operation, text="6", width=28, height=28)
b6.grid(row=2, column=2)
#b6.pack(side=RIGHT, expand=True)

b7 = CTkButton(master=frame_operation, text="7", width=28, height=28)
b7.grid(row=3, column=0, pady=10)
#b7.pack(side=LEFT, expand=True)

b8 = CTkButton(master=frame_operation, text="8", width=28, height=28)
b8.grid(row=3, column=1)
#b8.pack(expand=True, side=BOTTOM)

b9 = CTkButton(master=frame_operation, text="9", width=28, height=28)
b9.grid(row=3, column=2)
#b9.pack(side=RIGHT, expand=True)

b0 = CTkButton(master=frame_operation, text="0", width=28, height=28)
b0.grid(row=4, column=1, pady=10)
#b0.pack(expand=True, side=BOTTOM)

frame_util = CTkFrame(master=root)
frame_util.pack(expand=True, fill=BOTH)

b_compute = CTkButton(frame_util, text="compute", command=print(call_compute(b_num1.get(), b_num2.get(), b_operand.get())))
b_compute.pack(expand=True, pady=10)

r = CTkButton(frame_util, text="exit", command=root.destroy)
r.pack(expand=True)

progress_bar = CTkProgressBar(frame_util, mode='determinate', progress_color="green")
progress_bar.pack(expand=True, fill="x")

#float(b_num1.get())

root.mainloop()