
import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


def main():
    """ Constructs and runs a GUI for this program. """
    root = tkinter.Tk()
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    setup_gui(root, mqtt_client)

    root.mainloop()


def setup_gui(root_window, mqtt_client):
    """ Constructs and sets up widgets on the given window. """
    frame = ttk.Frame(root_window, padding=50)
    frame.grid()

    ttk.Style().configure("TButton", padding=9, relief="flat")

    get_near_object_button = ttk.Button(frame, text='Finds the object')
    get_near_object_button['command'] = lambda: get_near_objects(mqtt_client)
    get_near_object_button.grid()

    wall_button = ttk.Button(frame, text='Get near the object')
    wall_button['command'] = lambda: wall(mqtt_client)
    wall_button.grid()

    color_entry_box = ttk.Entry(frame)
    color_entry_box.grid()
    color_button = ttk.Button(frame, text='Finds the color')
    color_button['command'] = lambda: find_color(color_entry_box, mqtt_client)
    color_button.grid()


def get_near_objects(mqtt_client):
    """
    Tells the robot to find the object and get close near it
    """
    mqtt_client.send_message('get_near_objects')


def wall(mqtt_client):
    """
    Tells the robot how close is should get to the object in the given entry box.
    """
    mqtt_client.send_message('get_near_objects')


def find_color(color_entry_box, mqtt_client):
    """
    Tells the robot how close is should get to the object in the given entry box.
    """
    color_string = color_entry_box.get()
    print('Sending the get_near_object message with area', color_string)
    mqtt_client.send_message('get_near_objects', [color_string])




main()
