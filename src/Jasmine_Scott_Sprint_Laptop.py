
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

    get_near_object_button = ttk.Button(frame, text='Can you see the object?')
    get_near_object_button['command'] = lambda: get_near_object(mqtt_client)
    get_near_object_button.grid()


def get_near_object(mqtt_client):
    """
    Tells the robot to find the object and get close near it
    """
    mqtt_client.send_message('get_near_object')



main()
