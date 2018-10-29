"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():

    """ Runs YOUR specific part of the project """
    run_test_for_wait_until_intensity_is_less_than()
    run_test_for_wait_until_color_is()


def run_test_for_wait_until_intensity_is_less_than():
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving(50, 50)
    robot.color_sensor.wait_until_intensity_is_less_than(30)


def run_test_for_wait_until_color_is():
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving(20, 20)
    robot.color_sensor.wait_until_color_is(2)


main()
