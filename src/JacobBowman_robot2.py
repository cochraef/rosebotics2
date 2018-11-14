import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


def main():

    robot = rb.Snatch3rRobot()

    rc = RemoteControlEtc(robot)
    receiver = com.MqttClient(rc)
    receiver.connect_to_pc()

    while True:
        time.sleep(.01)


class RemoteControlEtc(object):
    """
    Stores the robot.
        :type robot: rb.Snatch3rRobot
    """
    def __init__(self, robot):
        self.robot = robot
        pass

    def go_forward(self):
        self.robot.drive_system.start_moving(70, 70)

    def go_forward_slow(self):
        self.robot.drive_system.start_moving(20, 20)
        self.robot.touch_sensor.wait_until_pressed()
        self.robot.drive_system.stop_moving()
        self.robot.sound.play_beep()
        time.sleep(.1)
        self.robot.sound.speak('Did I just get rear-ended')

    def stop__(self):
        self.robot.drive_system.start_moving(0, 0)


main()

"""
            if self.robot.proximity_sensor.get_distance_to_nearest_object_in_inches() < 1:
                self.robot.drive_system.stop_moving()
                self.robot.sound.play_beep()
                time.sleep(.1)
                self.robot.sound.speak('Get out of the way')
                time.sleep(.5)
            elif self.robot.proximity_sensor.get_distance_to_nearest_object_in_inches() > 1:
                self.robot.color_sensor.wait_until_color_is('white')
                self.robot.drive_system.stop_moving()
                self.robot.drive_system.left_wheel.start_spinning(70)
                self.robot.color_sensor.wait_until_color_is('black')
                self.robot.drive_system.left_wheel.stop_spinning()
                self.robot.drive_system.start_moving(20, 20)
"""