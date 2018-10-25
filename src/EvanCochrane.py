"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """

    print('why not?')
    # all_movement_tests()
    test_go_straight_inches_method()


def test_go_straight_inches_method():
    """ Tests the go_straight_inches method """
    my_robot = rb.Snatch3rRobot()

    print('Test 1: Forward 5 Inches')
    my_robot.drive_system.go_straight_inches(5, 50)

    print('Test 2: Backward 5 Inches')
    my_robot.drive_system.go_straight_inches(-5, -50)

    print('Test 3: Forward 0.5 Inches')
    my_robot.drive_system.go_straight_inches(0.5, 5)

    print('Test 4: Forward 0 Inches')
    my_robot.drive_system.go_straight_inches(0, 100)

    print('Test 5: Forward 60 Inches')
    my_robot.drive_system.go_straight_inches(60, 100)


def test_movement(robot, duty_cycle_percent, seconds):
    """ DEPRECATED - USED TO CALCULATE LINEAR REGRESSION """

    robot.drive_system.right_wheel.reset_degrees_spun()
    robot.drive_system.right_wheel.reset_degrees_spun()
    robot.drive_system.start_moving(duty_cycle_percent, duty_cycle_percent)
    time.sleep(seconds)
    robot.drive_system.stop_moving()
    x = robot.drive_system.right_wheel.get_degrees_spun()
    y = robot.drive_system.left_wheel.get_degrees_spun()
    print('Degrees spun in right wheel, Degrees spun in left wheel:', x, y)


def all_movement_tests():
    """ DEPRECATED - USED TO CALCULATE LINEAR REGRESSION """
    my_robot = rb.Snatch3rRobot()
    duty = [100, 50, 100, 25, 10, 50, -100, -20]
    seconds = [3, 6, 1, 4, 10, 10, 10, 1, 5]
    for k in range(len(duty)):
        test_movement(my_robot, duty[k], seconds[k])
        time.sleep(30)


main()