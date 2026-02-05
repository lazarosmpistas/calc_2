from tkinter import *
from tkinter import ttk
from customtkinter import *
from customtkinter import CTkProgressBar
import calc
from PIL import Image
import io
import os


class coords:
    """
    class managing drawing on the canvas
    """
    def __init__(self):
        # default values for old_x and old_y
        self.old_x = None
        self.old_y = None

    def draw(self, event, c):
        # draw a line from the old coordinates to the new coordinates
        if self.old_x and self.old_y:
            c.create_line(self.old_x, self.old_y, event.x, event.y, fill="red", width=3, smooth=True)
        self.old_x, self.old_y = event.x, event.y

class exporter:
    """
    Docstring for exporter
    """
    def __init__(self):
        self.export_count = 0

    def increment_count(self):
        self.export_count += 1

    def ps_to_png(self, c: Canvas, dir, filename="canvas_output"):
        print("im in")
        if not os.path.exists(dir):
            os.makedirs(dir, exist_ok=True)
        c.update()
        ps_path = os.path.join(dir, f"{filename}_{self.export_count}.ps")
        # Tk canvas PostScript does not include the widget background by default.
        # Paint a background rectangle so the PS/PNG matches the on-screen color.
        bg = c.create_rectangle(
            0, 0, c.winfo_width(), c.winfo_height(),
            fill=c.cget("background"),
            outline=c.cget("background"),
        )
        c.tag_lower(bg)
        c.postscript(file=ps_path, colormode='color')
        c.delete(bg)
        with Image.open(ps_path) as img:
            img.save(os.path.join(dir, f"{filename}_{self.export_count}.png"))
        self.increment_count()
        os.remove(ps_path)


def main():
    """
    main Function of the UI
    """

    window = CTk(screenName="CALC_V2", )
    window.title("CALC_V2")
    set_appearance_mode('dark')

    main_frame = CTkFrame(master=window)
    #main_frame.grid(row=0, column=0)
    main_frame.pack(expand=True, fill=BOTH)

    """
    header frame with title
    """

    frame_header = CTkFrame(master=main_frame)
    frame_header.grid(row=0, column=0, sticky=NSEW)
    #frame_header.pack(expand=True, fill=BOTH)

    w = CTkLabel(frame_header, text='CALC IS SHORT FOR CALCULATOR BTW')
    w.pack(expand=True, fill=BOTH)

    """
    string frame with entry
    """
    string_frame = CTkFrame(master=main_frame)
    string_frame.grid(row=1, column=0, sticky=NSEW)

    operation_string = StringVar()
    string_entry = CTkEntry(string_frame, state="readonly", textvariable=operation_string)
    string_entry.pack(expand=True, fill=BOTH)

    """
    operation frame with buttons
    """
    frame_operation = CTkFrame(master=main_frame)
    frame_operation.grid(row=2, column=0, sticky=NSEW)

    b1 = CTkButton(master=frame_operation, text="1", width=50, height=50, command=lambda:
    operation_string.set(operation_string.get() + "1"))
    b1.grid(row=1, column=0, pady=10)

    b2 = CTkButton(master=frame_operation, text="2", width=50, height=50, command=lambda:
    operation_string.set(operation_string.get() + "2"))
    b2.grid(row=1, column=1, padx=10)

    b3 = CTkButton(master=frame_operation, text="3", width=50, height=50, command=lambda:
    operation_string.set(operation_string.get() + "3"))
    b3.grid(row=1, column=2)

    b4 = CTkButton(master=frame_operation, text="4", width=50, height=50, command=lambda:
    operation_string.set(operation_string.get() + "4"))
    b4.grid(row=2, column=0, pady=10)

    b5 = CTkButton(master=frame_operation, text="5", width=50, height=50, command=lambda:
    operation_string.set(operation_string.get() + "5"))
    b5.grid(row=2, column=1)

    b6 = CTkButton(master=frame_operation, text="6", width=50, height=50, command=lambda:
    operation_string.set(operation_string.get() + "6"))
    b6.grid(row=2, column=2)

    b7 = CTkButton(master=frame_operation, text="7", width=50, height=50, command=lambda:
    operation_string.set(operation_string.get() + "7"))
    b7.grid(row=3, column=0, pady=10)

    b8 = CTkButton(master=frame_operation, text="8", width=50, height=50, command=lambda:
    operation_string.set(operation_string.get() + "8"))
    b8.grid(row=3, column=1)

    b9 = CTkButton(master=frame_operation, text="9", width=50, height=50, command=lambda:
    operation_string.set(operation_string.get() + "9"))
    b9.grid(row=3, column=2)

    b0 = CTkButton(master=frame_operation, text="0", width=50, height=50, command=lambda:
    operation_string.set(operation_string.get() + "0"))
    b0.grid(row=4, column=1, pady=10)

    b_plus = CTkButton(master=frame_operation, text="+", width=50, height=50, command=lambda:
    operation_string.set(operation_string.get() + "+"))
    b_plus.grid(row=1, column=3, padx=10)

    b_minus = CTkButton(master=frame_operation, text="-", width=50, height=50, command=lambda:
    operation_string.set(operation_string.get() + "-"))
    b_minus.grid(row=2, column=3)

    b_multiply = CTkButton(master=frame_operation, text="*", width=50, height=50, command=lambda:
    operation_string.set(operation_string.get() + "*"))
    b_multiply.grid(row=3, column=3)

    b_divide = CTkButton(master=frame_operation, text="/", width=50, height=50, command=lambda:
    operation_string.set(operation_string.get() + "/"))
    b_divide.grid(row=4, column=3)

    b_backspace = CTkButton(master=frame_operation, text="<", width=50, height=50, command=lambda:
    operation_string.set(operation_string.get()[:len(operation_string.get()) - 1]))
    b_backspace.grid(row=4, column=2)

    frame_operation.columnconfigure(0, weight=1)
    frame_operation.columnconfigure(1, weight=1)
    frame_operation.columnconfigure(2, weight=1)
    frame_operation.columnconfigure(3, weight=1)

    """
    frame for drawing utils
    """

    frame_draw = CTkFrame(master=main_frame)
    frame_draw.grid(column=1, row=0, rowspan=4, sticky=NSEW)

    old = coords()
    c = Canvas(frame_draw, width=400, height=400, background="black")

    c.bind("<B1-Motion>", lambda event: old.draw(event, c))
    c.bind("<ButtonRelease-1>", lambda event: old.__init__())
    c.pack(expand=True, fill=BOTH)

    exp = exporter()
    extract_button = CTkButton(frame_draw, text="extract", command=lambda: exp.ps_to_png(c, "img", "extracted"))
    extract_button.pack(expand=True, fill=BOTH, side=LEFT, padx=5, pady=5)

    clear_button = CTkButton(frame_draw, text="clear", command=lambda: c.delete("all"))
    clear_button.pack(expand=True, fill=BOTH, side=LEFT, padx=5, pady=5)
    
    """
    frame for util buttons: compute, exit, progress bar
    """

    frame_util = CTkFrame(master=main_frame)
    frame_util.grid(row=3, column=0, sticky=NSEW)

    result_string = StringVar()
    result_label = CTkEntry(frame_util, state="readonly", textvariable=result_string)
    result_label.pack(expand=True, pady=10)

    b_compute = CTkButton(frame_util, text="compute", command=lambda: 
                          result_string.set(calc.compute(calc.split_compute_string(string_entry.get()))))
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
