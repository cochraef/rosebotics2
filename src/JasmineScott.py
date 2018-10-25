"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time
robot = rb.Snatch3rRobot()

def main():
    """ Runs YOUR specific part of the project """
    run_test_for_wait_until_intensity_is_less_than()


def run_test_for_wait_until_intensity_is_less_than():
    robot.drive_system.start_moving(50, 50)
    robot.color_sensor.wait_until_intensity_is_less_than(30)


main()
