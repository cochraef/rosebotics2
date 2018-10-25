"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    test_touch_sensor()


def test_touch_sensor():
    robot = rb.Snatch3rRobot()
    sensor = rb.TouchSensor(robot.touch_sensor)
    robot.drive_system.start_moving(25, 25)
    while True:
        if sensor.wait_until_pressed() is True:
            robot.drive_system.stop_moving()
            break


main()
