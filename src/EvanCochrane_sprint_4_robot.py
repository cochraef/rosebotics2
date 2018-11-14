import rosebotics_new as rb
import mqtt_remote_method_calls as com
import time


def main():

    robot = rb.Snatch3rRobot()

    rc = RemoteControl(robot)
    receiver = com.MqttClient(rc)
    receiver.connect_to_pc()

    while True:
        time.sleep(0.01)


class RemoteControl(object):
    def __init__(self, robot):
        """
        Stores the robot.
        :type robot: rb.Snatch3rRobot
        """
        self.robot = robot


    def initialize(self, using_custom_floor_color_as_string):
        """ Sets the algorithm that lets the robot map out the floor plan. """

        if using_custom_floor_color_as_string == '1':
            using_custom_floor_color = True
        else:
            using_custom_floor_color = False

        self.robot.sound.set_wait_time(2)

        self.robot.sound.speak("Put me in a corner facing facing a wall, then press the touch sensor to start.")

        while True:
            if self.robot.touch_sensor.is_pressed():
                self.run_floor_plan_algorithm(using_custom_floor_color)

    def run_floor_plan_algorithm(self, custom_floor_color):



main()
