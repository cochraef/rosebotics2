import rosebotics_new as rb
import math
import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


def main():

    robot = rb.Snatch3rRobot()

    rc = RemoteControl(robot)
    receiver = com.MqttClient(rc)
    receiver.connect_to_pc()


class RemoteControl(object):
    def __init__(self, robot):
        """
        Stores the robot.
        :type robot: rb.Snatch3rRobot
        """
        self.robot = robot
        self.drive_system = robot.drive_system

    def go_straight_inches(self, distance_as_string, duty_cycle_percent_as_string='100'):
        """
        Makes the robot go forward a certain number of inches.
        """

        distance = float(distance_as_string)
        duty_cycle_percent = float(duty_cycle_percent_as_string)

        self.drive_system.go_straight_inches(distance, duty_cycle_percent)


main()
