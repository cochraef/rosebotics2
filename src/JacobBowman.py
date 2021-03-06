"""
  Capstone Project.  Code written by Jacob Bowman.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    # test_touch_sensor()
    # test_find_color(2)
    # test_black_line()
    test_arm()


def test_touch_sensor():
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving(25, 25)
    while True:
        if robot.touch_sensor.wait_until_pressed() is True:
            robot.drive_system.stop_moving()
            break


def find_color(color):
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving(25, 25)
    while True:
        if robot.color_sensor.wait_until_color_is(color) is True:
            robot.drive_system.stop_moving()
            break


def black_line():
    robot = rb.Snatch3rRobot()
    while True:
        if robot.color_sensor.wait_until_color_is(1) is True:
            robot.drive_system.start_moving(25, 25)
        elif robot.color_sensor.wait_until_color_is(6) is True:
            robot.drive_system.stop_moving()
            robot.drive_system.start_moving(50, 0)
        elif robot.color_sensor.wait_until_color_is(1) is True:
            robot.drive_system.stop_moving()
            robot.drive_system.start_moving(25, 25)


def test_find_color(color):
    find_color(color)


def test_black_line():
    black_line()


def test_arm():
    robot = rb.Snatch3rRobot()
    robot.arm.calibrate()


def ryg():
    robot = rb.Snatch3rRobot()
    robot.camera.get_biggest_blob().__getattribute__('color')


main()
