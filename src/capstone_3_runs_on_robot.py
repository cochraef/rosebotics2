"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and Jasmine SCott.
"""

import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


def main():
    robot = rb.Snatch3rRobot()

    rc = RemoteControlEtc(robot)
    mqtt_client = com.MqttClient(rc)
    mqtt_client.connect_to_pc()

    #if robot.beacon_button_sensor.is_top_red_button_pressed():
        #ev3.Sound.beep()
    #if robot.beacon_button_sensor.is_top_blue_button_pressed():
        #ev3.Sound.speak('Hello, How are you?')

    while True:
        " How the user controls the robot "
        if robot.beacon_button_sensor.is_top_red_button_pressed():
            robot.drive_system.move_for_seconds(3, 50, 50)
            " If the robot sees any of these colors, do an action "
            if robot.color_sensor.wait_until_color_is(2):
                robot.drive_system.spin_in_place_degrees(90)
            elif robot.color_sensor.wait_until_color_is(4):
                robot.drive_system.spin_in_place_degrees(270)
            #elif robot.color_sensor.wait_until_color_is(7):
                #robot.drive_system.spin_in_place_degrees(360)
            #elif robot.color_sensor.wait_until_color_is(1):
                #robot.sound.speak('You completed the maze!')
            #elif robot.color_sensor.wait_until_color_is(3):
                #robot.sound.speak("Would you like to go forward or turn right?")
            "For the robot's proximity sensors"
            #if robot.proximity_sensor.get_distance_to_nearest_object() > 100:
                #ev3.Sound.speak('You must take another path')
                #robot.drive_system.turn_degrees(90)
        elif robot.beacon_button_sensor.is_top_blue_button_pressed():
            robot.drive_system.move_for_seconds(3, -50, -50)
            " If the robot sees any of these colors, do an action "
            if robot.color_sensor.wait_until_color_is(2):
                robot.drive_system.spin_in_place_degrees(90)
            elif robot.color_sensor.wait_until_color_is(4):
                robot.drive_system.spin_in_place_degrees(270)
            #elif robot.color_sensor.wait_until_color_is(7):
                #robot.drive_system.spin_in_place_degrees(360)
            #elif robot.color_sensor.wait_until_color_is(1):
                #robot.sound.speak('You completed the maze!')
            #elif robot.color_sensor.wait_until_color_is(3):
                #robot.sound.speak("Would you like to go forward or turn right?")
            "For the robot's proximity sensors"
            #if robot.proximity_sensor.get_distance_to_nearest_object() > 100:
                #ev3.Sound.speak('You must take another path')
                #robot.drive_system.turn_degrees(90)
        time.sleep(.01)


class RemoteControlEtc(object):
    def __init__(self, robot):
        """
        Stores the robot.
            :type robot: rb.Snatch3rRobot
        """
        self.robot = robot

    def go_forwards(self, speed_string):
        """Makes the robot go forward at the given speed"""
        print('Telling the robot to start moving at', speed_string)
        speed = int(speed_string)
        self.robot.drive_system.start_moving(speed, speed)
        if self.robot.touch_sensor.is_pressed():
            self.robot.drive_system.stop_moving()
        print('COMPLETED')

    def beeping(self, beep_string):
        """Makes the robot beep a certain amount of times"""
        print('Telling the robot to beep', beep_string, 'times')
        beeps = int(beep_string)
        for k in range(beeps):
            self.robot.sound.play_beep()
            print('Beep #', (k + 1), 'completed')
            self.robot.sound.set_wait_time(0.5)


main()
