"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():

    """ Runs YOUR specific part of the project """
    # run_test_for_wait_until_intensity_is_less_than()
    # run_test_for_wait_until_intensity_is_greater_than()
    # run_test_for_wait_until_color_is()
    run_test_for_wait_until_color_is_one_of()


def run_test_for_wait_until_intensity_is_less_than():
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving(50, 50)
    robot.color_sensor.wait_until_intensity_is_less_than(30)
    robot.drive_system.stop_moving(rb.StopAction.BRAKE)


def run_test_for_wait_until_intensity_is_greater_than():
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving(10, 10)
    robot.color_sensor.wait_until_intensity_is_greater_than(50)
    robot.drive_system.stop_moving(rb.StopAction.BRAKE)


# This one works!!!
def run_test_for_wait_until_color_is():

    # Test 1
    """The robot should stop if it sees Black"""
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving(20, 20)
    robot.color_sensor.wait_until_color_is(1)
    robot.drive_system.stop_moving(rb.StopAction.BRAKE)

    # Test 2
    """The robot should stop if it sees Blue"""
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving(30, 30)
    robot.color_sensor.wait_until_color_is(2)
    robot.drive_system.stop_moving(rb.StopAction.BRAKE)

    # Test 3
    """The robot should stop if it sees Blue"""
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving(40, 40)
    robot.color_sensor.wait_until_color_is(4)
    robot.drive_system.stop_moving(rb.StopAction.BRAKE)


def run_test_for_wait_until_color_is_one_of():
    # Test 1
    """The robot should stop if it sees Yellow, Red, or White"""
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving(30, 30)
    robot.color_sensor.wait_until_color_is_one_of([4, 5, 6])
    robot.drive_system.stop_moving(rb.StopAction.BRAKE)

    # Test 2
    """The robot should stop if it sees White, Blue, or Brown"""
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving(20, 20)
    robot.color_sensor.wait_until_color_is_one_of([6, 2, 7])
    robot.drive_system.stop_moving(rb.StopAction.BRAKE)

    # Test 3
    """The robot should stop if it sees Black, White, or Green"""
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving(60, 60)
    robot.color_sensor.wait_until_color_is_one_of([1, 6, 3])
    robot.drive_system.stop_moving(rb.StopAction.BRAKE)


main()
