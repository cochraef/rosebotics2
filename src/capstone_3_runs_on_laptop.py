"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

This module runs on your LAPTOP.
It uses MQTT to SEND information to a program running on the ROBOT.

Authors:  David Mutchler, his colleagues, and Jasmine Scott.
"""
# ------------------------------------------------------------------------------
#  With your instructor, discuss the "big picture" of laptop-robot
#     communication:
#      - One program runs on your LAPTOP.  It displays a GUI.  When the
#         user presses a button intended to make something happen on the
#         ROBOT, the LAPTOP program sends a message to its MQTT client
#         indicating what it wants the ROBOT to do, and the MQTT client
#         SENDS that message TO a program running on the ROBOT.
#
#      - Another program runs on the ROBOT. It stays in a loop, responding
#        to events on the ROBOT (like pressing buttons on the IR Beacon).
#        It also, in the background, listens for messages TO the ROBOT
#        FROM the program running on the LAPTOP. When it hears such a
#        message, it calls the method in the DELAGATE object's class
#        that the message indicates, sending arguments per the message.
# ------------------------------------------------------------------------------

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

    # --------------------------------------------------------------------------
    #  Add code above that constructs a   com.MqttClient   that will
    # be used to send commands to the robot.  Connect it to this ev3.
    # --------------------------------------------------------------------------


def setup_gui(root_window, mqtt_client):
    """ Constructs and sets up widgets on the given window. """
    frame = ttk.Frame(root_window, padding=10)
    frame.grid()


    speed_entry_box = ttk.Entry(frame)
    go_forward_button = ttk.Button(frame, text="Go forward")
    speed_entry_box.grid()
    go_forward_button.grid()
    go_forward_button['command'] = \
        lambda: handle_go_forwards(speed_entry_box, mqtt_client)

def handle_go_forwards(entry_box, mqtt_client):
    """
    Tells the robot to go forward at the speed specified in the given entry box.
    """
    speed_string = entry_box.get()
    print('Sending the go_forward message with speed', speed_string)
    mqtt_client.send_message('go_forwards', [speed_string])


main()
