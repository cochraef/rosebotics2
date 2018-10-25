"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """

    print('why not?')


main()




my_robot = rb.Snatch3rRobot()


def test_movement(robot, duty_cycle_percent, seconds):
    robot.drive_system.right_wheel.reset_degrees_spun()
    robot.drive_system.right_wheel.reset_degrees_spun()
    robot.drive_system.start_moving(duty_cycle_percent, duty_cycle_percent)
    time.sleep(seconds)
    robot.drive_system.stop_moving()
    x = robot.drive_system.right_wheel.get_degrees_spun()
    y = robot.drive_system.left_wheel.get_degrees_spun()
    print('Degrees spun in right wheel, Degrees spun in left wheel:', x, y)


test_movement(my_robot, 100, 3)
# test_movement(my_robot, 50, 6)
# test_movement(my_robot, 100, 1)
# test_movement(my_robot, 25, 4)
# test_movement(my_robot, 10, 10)
# test_movement(my_robot, 50, 10)
# test_movement(my_robot, -100, 1)
# test_movement(my_robot, -20, 5)
