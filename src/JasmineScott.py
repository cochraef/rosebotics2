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
    # wait_until_intensity_is_less_than()
    # wait_until_intensity_is_greater_than()
    #wait_until_color_is()
    # wait_until_color_is_one_of()
    camera()
    # beep_for_top_red_button()
    # black_line()


def wait_until_intensity_is_less_than():

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


def wait_until_intensity_is_greater_than():

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
def wait_until_color_is():

    # Test 1
    """The robot should stop if it sees Green"""
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving(20, 20)
    robot.color_sensor.wait_until_color_is(3)
    robot.drive_system.stop_moving(rb.StopAction.BRAKE)

    # Test 2
    """The robot should stop if it sees Blue"""
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving(30, 30)
    robot.color_sensor.wait_until_color_is(2)
    robot.drive_system.stop_moving(rb.StopAction.BRAKE)

    # Test 3
    """The robot should stop if it sees Yellow"""
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving(40, 40)
    robot.color_sensor.wait_until_color_is(4)
    robot.drive_system.stop_moving(rb.StopAction.BRAKE)


def wait_until_color_is_one_of():
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


def camera():
    robot = rb2.Snatch3rRobot()
    while True:
        width = robot.camera.get_biggest_blob().width
        height = robot.camera.get_biggest_blob().height

        area = width * height

        if area > 700:
            ev3.Sound.beep()



def beep_for_top_red_button():
    robot = rb2.Snatch3rRobot()
    while True:
        if robot.beacon_button_sensor.is_top_red_button_pressed():
            ev3.Sound.beep()
        if robot.beacon_button_sensor.is_top_blue_button_pressed():
            ev3.Sound.speak('Hello, How are you?')
        if robot.touch_sensor.is_pressed():
            break


def black_line():
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving(25, 25)
    while True:
        if robot.color_sensor.wait_until_color_is(6) is True:
                robot.drive_system.stop_moving()
                robot.drive_system.left_wheel.start_spinning(50)
                if robot.color_sensor.wait_until_color_is(1):
                    robot.drive_system.stop_moving()
                    robot.drive_system.start_moving(25, 25)
        elif robot.touch_sensor.wait_until_pressed() is True:
            robot.drive_system.stop_moving()
            break
    print('COMPLETED')


def beep_for_red_button(self, beep_string):
    """Makes the robot if top-red button on Beacon is pressed"""
    print('Telling the robot to beep', beep_string, 'times')
    beeps = int(beep_string)
    for k in range(beeps):
        self.robot.sound.play_beep()
        print('Beep #', (k + 1), 'completed')
        self.robot.sound.set_wait_time(0.5)


def beep_for_blue_button(self, beep_string):
    """Makes the robot if top-blue_button on Beacon is pressed"""
    print('Telling the robot to beep', beep_string, 'times')
    beeps = int(beep_string)
    for k in range(beeps):
        self.robot.sound.play_beep()
        print('Beep #', (k + 1), 'completed')
        self.robot.sound.set_wait_time(0.5)

main()
