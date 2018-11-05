"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import rosebotics_new as rb2
import ev3dev.ev3 as ev3
import time


def main():

    """ Runs YOUR specific part of the project """
    # run_test_for_wait_until_intensity_is_less_than()
    # run_test_for_wait_until_intensity_is_greater_than()
    # run_test_for_wait_until_color_is()
    # run_test_for_wait_until_color_is_one_of()
    run_test_for_beeping_based_camera()


def run_test_for_wait_until_intensity_is_less_than():

    # Test 1
    robot = rb.Snatch3rRobot()
    """The robot should stop if the self intensity is less than 30"""
    robot.drive_system.start_moving(50, 50)
    robot.color_sensor.wait_until_intensity_is_less_than(30)
    robot.drive_system.stop_moving(rb.StopAction.BRAKE)

    # Test 2
    robot = rb.Snatch3rRobot()
    """The robot should stop if the self intensity is less than 40"""
    robot.drive_system.start_moving(50, 50)
    robot.color_sensor.wait_until_intensity_is_less_than(40)
    robot.drive_system.stop_moving(rb.StopAction.BRAKE)

    # Test 3
    robot = rb.Snatch3rRobot()
    """The robot should stop if the self intensity is less than 50"""
    robot.drive_system.start_moving(50, 50)
    robot.color_sensor.wait_until_intensity_is_less_than(50)
    robot.drive_system.stop_moving(rb.StopAction.BRAKE)


def run_test_for_wait_until_intensity_is_greater_than():

    # Test 1
    robot = rb.Snatch3rRobot()
    """The robot should stop if the self intensity is greater than 30"""
    robot.drive_system.start_moving(20, 20)
    robot.color_sensor.wait_until_intensity_is_greater_than(30)
    robot.drive_system.stop_moving(rb.StopAction.BRAKE)

    # Test 2
    robot = rb.Snatch3rRobot()
    """The robot should stop if the self intensity is greater than 40"""
    robot.drive_system.start_moving(30, 30)
    robot.color_sensor.wait_until_intensity_is_greater_than(40)
    robot.drive_system.stop_moving(rb.StopAction.BRAKE)

    # Test 3
    robot = rb.Snatch3rRobot()
    """The robot should stop if the self intensity is greater than 50"""
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


def run_test_for_beeping_based_camera():
    robot = rb2.Snatch3rRobot()
    camera = robot.camera

    while True:
        width = camera.get_biggest_blob().width
        height = camera.get_biggest_blob().height

        area = width * height

        if  area > 1000:
            # print("I SEE THE COLOR")
            ev3.Sound.beep()




main()
