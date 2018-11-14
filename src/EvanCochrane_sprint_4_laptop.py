"""
The part of the sprint 4 individual application that runs on the laptop.

Creates a tkinter GUI that uses MQTT to send information from the robot to the laptop.
Also receives information from the robot and displays it on the GUI.

Authors: Evan Cochrane.
"""

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as com


class StoreObjects(object):
    """ Stores various Tkinter objects for use across functions. """
    def __init__(self):
        self.viewing_window = None
        self.canvas = None


def main():
    """ Executes first when the code is run. Sets up the MQTT client. """
    instructor = com.MqttClient()
    instructor.connect_to_ev3()

    root = tkinter.Tk()
    root.title("Floor Plan Mapper Project")

    store_window = StoreObjects()

    construct_root_window(root, store_window, instructor)

    root.mainloop()


def construct_root_window(root, window_store, mqtt_client):
    """ Constructs the setup (root) window for the tkinter GUI. """

    # Frame
    frame = ttk.Frame(root, padding='40 10')
    frame.grid()

    root_desc = tkinter.Label(frame, text='Choose Settings', fg='blue')
    root_desc.grid(columnspan=5, row=0)

    # Viewing Window Size Control
    entry_box_desc = tkinter.Label(frame, text='Size of the viewing window, in pixels.')
    entry_box_desc.grid(columnspan=3, row=1)

    width_window = ttk.Entry(frame)
    width_window.grid(column=3, row=1)

    height_window = ttk.Entry(frame)
    height_window.grid(column=4, row=1)

    width_window_text = ttk.Label(frame, text='Width')
    width_window_text.grid(column=3, row=2)

    height_window_text = ttk.Label(frame, text='Height')
    height_window_text.grid(column=4, row=2)

    # Wall and Floor Colors
    wall_color = ttk.Entry(frame)
    wall_color.grid(column=2, row=3)

    wall_color_desc = tkinter.Label(frame, text='Wall Color')
    wall_color_desc.grid(column=3, row=3)

    floor_color = ttk.Entry(frame)
    floor_color.grid(column=2, row=6)

    floor_color_desc = tkinter.Label(frame, text='Floor Color')
    floor_color_desc.grid(column=3, row=6)

    custom_floor_color = tkinter.Checkbutton(frame)
    custom_floor_color.grid(column=2, row=5)
    checkbox_observer = tkinter.StringVar()
    custom_floor_color['variable'] = checkbox_observer

    custom_floor_color_desc = tkinter.Label(frame, text='Use Custom Floor Color')
    custom_floor_color_desc.grid(column=3, row=5)

    # Manipulate the viewing window
    create_button = tkinter.Button(frame, text='Create Window', fg='white', bg='blue')
    create_button.grid(column=2, row=7)
    create_button['command'] = lambda: construct_viewing_window(mqtt_client, width_window,
                                                                height_window, window_store,
                                                                checkbox_observer, wall_color,
                                                                floor_color)

    pause_button = tkinter.Button(frame, text='Reset Window', fg='white', bg='blue')
    pause_button.grid(column=3, row=7)
    pause_button['command'] = lambda: reset_viewing_window(window_store)

    stop_button = tkinter.Button(frame, text='Kill Window', fg='white', bg='red')
    stop_button.grid(column=4, row=7)
    stop_button['command'] = lambda: kill_viewing_window(window_store)


def construct_viewing_window(mqtt_client, width_window, height_window, window_store, observer,
                             wall_color, floor_color):
    """ Constructs the viewing window for the GUI based on parameters passed"""

    if width_window.get() == '':
        width = 500
    else:
        width = int(width_window.get())

    if width_window.get() == '':
        height = 400
    else:
        height = int(height_window.get())

    viewing_window = tkinter.Toplevel()

    canvas = tkinter.Canvas(viewing_window, width=width, height=height)
    canvas.grid()

    start_button = tkinter.Button(viewing_window, text='Go!', bg='blue', fg='white')
    start_button.place(x=0, y=height-20)
    start_button['command'] = lambda: handle_initialize(mqtt_client, observer)

    window_store.viewing_window = viewing_window
    window_store.canvas = canvas

    print(observer.get())


def kill_viewing_window(window_store):
    """ Closes the viewing window when called. Ends the robot's program. """
    if window_store.viewing_window is not None:
        window_store.viewing_window.destroy()


def reset_viewing_window(window_store):
    """
    Deletes all canvas objects on the viewing window when called. Ends the robot's program.
    """
    if window_store.canvas is not None:
        window_store.canvas.delete(tkinter.ALL)


def handle_initialize(mqtt_client, using_custom_floor_color_as_string):
    """ Causes the robot to start its program. """
    mqtt_client.send_message("initialize", [using_custom_floor_color_as_string])


main()
