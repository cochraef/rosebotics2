"""
  Capstone Project.  Code written by Evan Cochrane.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time


def main():
    """ Runs YOUR specific part of the project. Uncomment tests as needed. """

    print('why not?')

    # test_go_straight_inches_method()
    test_spin_in_place_degrees_method()
    # test_turn_degrees_method()
    # test_move_in_polygon_function()
    # infrared_tester(9, 15)


def move_in_polygon(robot, n, length_of_each_side=5, speed=100):
    """ Causes the given rb.Robot object to move in a regular n-gon pattern, with optional length and speed options.

    :type robot: rb.Snatch3rRobot
    :type n: int
    :type length_of_each_side: float
    :type speed: int
    """
    for _ in range(n):
        robot.drive_system.go_straight_inches(length_of_each_side, speed)
        robot.drive_system.spin_in_place_degrees((360 / n), speed)


def test_go_straight_inches_method():
    """ Tests the go_straight_inches method """
    my_robot = rb.Snatch3rRobot()

    print('Test 1: Forward 5 Inches')
    my_robot.drive_system.go_straight_inches(5, 50)

    time.sleep(10)

    print('Test 2: Backward 5 Inches')
    my_robot.drive_system.go_straight_inches(-5, -50)

    time.sleep(10)

    print('Test 3: Forward 0.5 Inches')
    my_robot.drive_system.go_straight_inches(0.5, 20)

    time.sleep(10)

    print('Test 4: Forward 0 Inches')
    my_robot.drive_system.go_straight_inches(0, 100)

    time.sleep(10)

    print('Test 5: Forward 60 Inches')
    my_robot.drive_system.go_straight_inches(60, 100)

    time.sleep(10)


def test_spin_in_place_degrees_method():
    """ Tests the spin_in_place_degrees method """
    my_robot = rb.Snatch3rRobot()

    print('Test 1: Clockwise 90 Degrees')
    my_robot.drive_system.spin_in_place_degrees(90, 100)

    time.sleep(10)

    print('Test 2: Counter 90 Degrees')
    my_robot.drive_system.spin_in_place_degrees(-90, -100)

    time.sleep(10)

    print('Test 3: Clockwise 360 Degrees')
    my_robot.drive_system.spin_in_place_degrees(360, 40)

    time.sleep(10)

    print('Test 4: Clockwise 0 Degrees')
    my_robot.drive_system.spin_in_place_degrees(0, 50)

    time.sleep(10)

    print('Test 5: Counter 720 Degrees')
    my_robot.drive_system.spin_in_place_degrees(-720, -100)

    time.sleep(10)


def test_turn_degrees_method():
    """ Tests the spin_in_place_degrees method """
    my_robot = rb.Snatch3rRobot()

    print('Test 1: Clockwise 90 Degrees')
    my_robot.drive_system.turn_degrees(90, 100)

    time.sleep(10)

    print('Test 2: Counter 90 Degrees')
    my_robot.drive_system.turn_degrees(-90, -100)

    time.sleep(10)

    print('Test 3: Clockwise 360 Degrees')
    my_robot.drive_system.turn_degrees(360, 40)

    time.sleep(10)

    print('Test 4: Clockwise 0 Degrees')
    my_robot.drive_system.turn_degrees(0, 50)

    time.sleep(10)

    print('Test 5: Counter 720 Degrees')
    my_robot.drive_system.turn_degrees(-720, -100)

    time.sleep(10)


def test_move_in_polygon_function():
    """ Tests the move_in_polygon function. """
    my_robot = rb.Snatch3rRobot()

    print('Test 1: Octagon')
    move_in_polygon(my_robot, 8)

    time.sleep(10)

    print('Test 2: Small Square')
    move_in_polygon(my_robot, 4, 2)

    time.sleep(10)

    print('Test 3: Slow Triangle')
    move_in_polygon(my_robot, 3, 10, 50)

    time.sleep(10)

    print('Test 4: Decagon')
    move_in_polygon(my_robot, 10, 1)

    time.sleep(10)

    print('Test 5: OH GOD WHY')
    move_in_polygon(my_robot, 100, 0.1)

    time.sleep(10)


def infrared_tester(low, high, beep_volume=100):
    """Causes the robot to beep with volume beep_volume between 0 and 100 when an object is placed between the lower bound
    and upper bound of the function.

        :type low: float
        :type high: float
        :type beep_volume: int

    """
    my_robot = rb.Snatch3rRobot()
    my_robot.sound.set_wait_time(1)
    my_robot.sound.set_volume(beep_volume)
    while True:
        dist = my_robot.proximity_sensor.get_distance_to_nearest_object_in_inches()
        print(dist)
        if low <= dist <= high:
            my_robot.sound.play_beep()
        if my_robot.touch_sensor.is_pressed():
            break


def test_movement(robot, duty_cycle_percent, seconds):
    """ DEPRECATED - USED TO CALCULATE LINEAR REGRESSION """

    robot.drive_system.right_wheel.reset_degrees_spun()
    robot.drive_system.left_wheel.reset_degrees_spun()
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


def test_rotation(bottom, top, n):
    """DEPRECATED - USED TO GUESS-AND-CHECK"""
    robot = rb.Snatch3rRobot()
    for k in range(bottom, round(top * n)):
        print('Testing rotation with test value', k / n)
        robot.drive_system.spin_in_place_degrees(90, k / n)
        time.sleep(20)


main()
