"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and Jacob Bowman.
"""


import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


def main():

    robot = rb.Snatch3rRobot()
    # --------------------------------------------------------------------------
    # TODO: 4. Add code that constructs a   com.MqttClient   that will
    # TODO:    be used to receive commands sent by the laptop.
    # TODO:    Connect it to this robot.  Test.  When OK, delete this TODO.
    # --------------------------------------------------------------------------
    rc = RemoteControlEtc(robot)
    receiver = com.MqttClient(rc)
    receiver.connect_to_pc()
    # --------------------------------------------------------------------------
    # TODO: 5. Add a class for your "delegate" object that will handle messages
    # TODO:    sent from the laptop.  Construct an instance of the class and
    # TODO:    pass it to the MqttClient constructor above.  Augment the class
    # TODO:    as needed for that, and also to handle the go_forward message.
    # TODO:    Test by PRINTING, then with robot.  When OK, delete this TODO.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # TODO: 6. With your instructor, discuss why the following WHILE loop,
    # TODO:    that appears to do nothing, is necessary.
    # TODO:    When you understand this, delete this TODO.
    # --------------------------------------------------------------------------
    while True:
        # ----------------------------------------------------------------------
        # TODO: 7. Add code that makes the robot beep if the top-red button
        # TODO:    on the Beacon is pressed.  Add code that makes the robot
        # TODO:    speak "Hello. How are you?" if the top-blue button on the
        # TODO:    Beacon is pressed.  Test.  When done, delete this TODO.
        # ----------------------------------------------------------------------
        time.sleep(0.01)  # For the delegate to do its work

        red = robot.beacon_button_sensor.is_top_red_button_pressed()
        blue = robot.beacon_button_sensor.is_top_blue_button_pressed()

        if red:
            ev3.Sound.beep()
        elif blue:
            ev3.Sound.speak('Hello. How are you?')


class RemoteControlEtc(object):
    """
    Stores the robot.
        :type robot: rb.Snatch3rRobot
    """
    def __init__(self, robot):
        self.robot = robot
        pass

    def go_forward(self, speed_str):
        print('Telling the robot to start moving at', speed_str)
        speed = int(speed_str)
        self.robot.drive_system.start_moving(speed, speed)


main()