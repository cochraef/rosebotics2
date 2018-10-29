"""
  Capstone Project.  Code written by Jacob Bowman.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    test_touch_sensor()


def test_touch_sensor():
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving(25, 25)
    while True:
        if robot.touch_sensor.wait_until_pressed() is True:
            robot.drive_system.stop_moving()
            break


def find_color(color_value):
    a = 0


main()
