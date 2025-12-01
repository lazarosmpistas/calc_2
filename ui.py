from tkinter import *
from tkinter import ttk
from customtkinter import *
from customtkinter import CTkProgressBar
import calc
import re


"""
TODO: CHANGE DEF TO SUPPORT ONE ENTRY FIELD FOR OPERATION (MANAGE 1 STRING INPUT)
"""
def call_compute(operation_str):
    #nums = re.split('+-*/', operation_str)
    print(re.search('\s*[0-9]+\s*[+-/*]\s*[0-9]+\s*', operation_str))
    #num1 = nums[0]
    #num2 = nums[1]

#    if not calc.checks(num1, num2, operator):
#        print("Invalid input my sister/brother!")
#    else:
#        num1, num2 = calc.process(num1, num2)
#        result = calc.operation(num1, num2, operator)
#        calc.log_results(num1, num2, operator, result)
#        print(result)
        
def main():
    window = CTk(screenName="CALC_V2", )
    set_appearance_mode('dark')
    #root.geometry("500x300")

    main_frame = CTkFrame(master=window)
    main_frame.grid(row=0, column=0)

    # HEADER FRAME

    frame_header = CTkFrame(master=main_frame)
    frame_header.grid(row=0, column=0, sticky=NSEW)
    #frame_header.pack(expand=True, fill=BOTH)

    w = CTkLabel(frame_header, text='CALC IS SHORT FOR CALCULATOR BTW')
    w.pack(expand=True, fill=BOTH)
    
    frame_header.columnconfigure(0, weight=1)
    frame_header.rowconfigure(0, weight=1)

    # OPERATION FRAME

    frame_nums = CTkFrame(master=main_frame)
    frame_nums.grid(row=1, column=0, sticky=NSEW)
    
    operation_entry = CTkEntry(frame_nums, placeholder_text="Number 1", width=100)
    operation_entry.grid(row=0, column=1, sticky=NSEW)
    #b_operand = CTkEntry(frame_operation, placeholder_text="Operation", width=70)
    #b_operand.grid(row=0, column=1, sticky=NSEW)
    #b_num2 = CTkEntry(frame_operation, placeholder_text="Number 2", width=70)
    #b_num2.grid(row=0, column=2, sticky=E)

    b1 = CTkButton(master=frame_nums, text="1", width=50, height=50, command=lambda: operation_entry.insert(END, "1"))
    b1.grid(row=1, column=0, pady=10)

    b2 = CTkButton(master=frame_nums, text="2", width=50, height=50, command=lambda: operation_entry.insert(END, "2"))
    b2.grid(row=1, column=1, padx=10)

    b3 = CTkButton(master=frame_nums, text="3", width=50, height=50, command=lambda: operation_entry.insert(END, "3"))
    b3.grid(row=1, column=2)

    b4 = CTkButton(master=frame_nums, text="4", width=50, height=50, command=lambda: operation_entry.insert(END, "4"))
    b4.grid(row=2, column=0, pady=10)

    b5 = CTkButton(master=frame_nums, text="5", width=50, height=50, command=lambda: operation_entry.insert(END, "5"))
    b5.grid(row=2, column=1)

    b6 = CTkButton(master=frame_nums, text="6", width=50, height=50, command=lambda: operation_entry.insert(END, "6"))
    b6.grid(row=2, column=2)

    b7 = CTkButton(master=frame_nums, text="7", width=50, height=50, command=lambda: operation_entry.insert(END, "7"))
    b7.grid(row=3, column=0, pady=10)

    b8 = CTkButton(master=frame_nums, text="8", width=50, height=50, command=lambda: operation_entry.insert(END, "8"))
    b8.grid(row=3, column=1)

    b9 = CTkButton(master=frame_nums, text="9", width=50, height=50, command=lambda: operation_entry.insert(END, "9"))
    b9.grid(row=3, column=2)

    b0 = CTkButton(master=frame_nums, text="0", width=50, height=50, command=lambda: operation_entry.insert(END, "0"))
    b0.grid(row=4, column=1, pady=10)

    frame_operands = CTkFrame(master=main_frame)
    frame_operands.grid(row=2, column=0, sticky=NSEW)

    frame_nums.columnconfigure(0, weight=1)
    frame_nums.columnconfigure(1, weight=1)
    frame_nums.columnconfigure(2, weight=1)
    frame_nums.rowconfigure(0, weight=1)
    frame_nums.rowconfigure(1, weight=1)
    frame_nums.rowconfigure(2, weight=1)
    frame_nums.rowconfigure(3, weight=1)
    frame_nums.rowconfigure(4, weight=1)

    b_plus = CTkButton(master=frame_nums, text="+", width=50, height=50, command=lambda: operation_entry.insert(END, "+"))
    b_plus.grid(row=5, column=0)

    b_minus = CTkButton(master=frame_nums, text="-", width=50, height=50, command=lambda: operation_entry.insert(END, "-"))
    b_minus.grid(row=5, column=1)
    b_multiply = CTkButton(master=frame_nums, text="*", width=50, height=50, command=lambda: operation_entry.insert(END, "*"))
    b_multiply.grid(row=5, column=2)

    frame_util = CTkFrame(master=main_frame)
    frame_util.grid(row=3, column=0, sticky=NSEW)

    b_compute = CTkButton(frame_util, text="compute", command=lambda: call_compute(operation_entry.get()))
    b_compute.pack(expand=True, pady=10)

    r = CTkButton(frame_util, text="exit", command=window.destroy)
    r.pack(expand=True)

    progress_bar = CTkProgressBar(frame_util, mode='determinate', progress_color="green")
    progress_bar.pack(expand=True, fill="x")

    window.update_idletasks()
    window.geometry(f"{main_frame.winfo_reqwidth()}x{main_frame.winfo_reqheight()}")
    window.columnconfigure(0, weight=1)
    window.rowconfigure(1, weight=1)
    window.mainloop()


if __name__ == "__main__":
    main()