"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    run_test_for_wait_until_intensity_is_less_than()


def run_test_for_wait_until_intensity_is_less_than():
    rb.DriveSystem.start_moving(left_wheel_duty_cycle_percent=100, right_wheel_duty_cycle_percent=100)
    rb.ColorSensor.wait_until_intensity_is_less_than()


main()
