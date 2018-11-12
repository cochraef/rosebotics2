import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as com

import math
import time


def main():
    root = tkinter.Tk()
    root.title("Photocopier Project")

    construct_root(root)

    root.mainloop()


def construct_root(root):

    frame = ttk.Frame(root, width=750, height=400)
    frame.grid()

    width_window_text = ttk.Label(frame, text='Width')
    width_window_text.grid(column=0, row=0)

    height_window_text = ttk.Label(frame, text='Height')
    height_window_text.grid(column=1, row=0)

    width_window = ttk.Entry(frame)
    width_window.grid(column=0, row=1)

    height_window = ttk.Entry(frame)
    height_window.grid(column=1, row=1)

    button = ttk.Button(frame, text='Go!')
    button.grid(columnspan=2, row=2)
    button['command'] = lambda: construct_photo_window(width_window, height_window)


def construct_photo_window(width_window, height_window):

    width = width_window.get()
    height = height_window.get()

    tkinter.Toplevel(width=width, height=height)


main()
