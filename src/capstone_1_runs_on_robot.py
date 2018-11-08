"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and Evan Cochrane.
"""

import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com


def main():

    robot = rb.Snatch3rRobot()

    rc = RemoteControl(robot)
    receiver = com.MqttClient(rc)
    receiver.connect_to_pc()

    while True:

        robot.sound.set_wait_time(1)

        red_pressed = robot.beacon_button_sensor.is_top_red_button_pressed()
        blue_pressed = robot.beacon_button_sensor.is_top_blue_button_pressed()

        if red_pressed and blue_pressed:
            robot.sound.play_beep()
            robot.sound.speak("Hello. How are you?", False)

        elif red_pressed and not blue_pressed:
            robot.sound.play_beep()

        elif blue_pressed and not red_pressed:
            robot.sound.speak("Hello. How are you?")

        time.sleep(0.01)  # For the delegate to do its work


class RemoteControl(object):
    def __init__(self, robot):
        """
        Stores the robot.
        :type robot: rb.Snatch3rRobot
        """
        self.robot = robot

    def go_forward(self, speed_as_string):
        """ Makes the robot go forward at the given speed. """

        print("The robot should start moving at speed:", speed_as_string)
        speed = int(speed_as_string)
        self.robot.drive_system.start_moving(speed, speed)


main()
