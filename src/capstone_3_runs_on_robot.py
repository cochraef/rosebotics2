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

    while True:
        #if robot.beacon_button_sensor.is_top_red_button_pressed():
            #ev3.Sound.beep()
        #if robot.beacon_button_sensor.is_top_blue_button_pressed():
            #ev3.Sound.speak('Hello, How are you?')

        " How the user controls the robot "
        if robot.beacon_button_sensor.is_top_red_button_pressed():
            robot.drive_system.start_moving(30, 30)
        if robot.beacon_button_sensor.is_top_blue_button_pressed():
            robot.drive_system.start_moving(-30, 30)
        "For the robot's proximity sensors"
        if robot.proximity_sensor.get_distance_to_nearest_object() > 50:
            ev3.Sound.speak('You must take another path')

        " If the robot sees any of these colors, do an action "
        if robot.color_sensor.wait_until_color_is(2):
            robot.drive_system.turn_degrees(90)
        if robot.color_sensor.wait_until_color_is(4):
            robot.drive_system.turn_degrees(-90)
        if robot.color_sensor.wait_until_color_is(7):
            robot.drive_system.turn_degrees(360)
        if robot.color_sensor.wait_until_color_is(5):
            ev3.Sound.speak('You completed the maze!')
        if robot.color_sensor.wait_until_color_is(3):
            ev3.Sound.speak("Would you like to go forward or turn right?")
            RemoteControlEtc.turn_right()


        time.sleep(0.01)


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

    def turn_right(self):
        self.robot.drive_system.turn_degrees(90)
        ev3.Sound.beep()

    def forward(self):
        ev3.Sound.beep()

main()
