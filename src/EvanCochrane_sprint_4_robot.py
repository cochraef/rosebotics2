import rosebotics_new as rb
import mqtt_remote_method_calls as com
import time
import math


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
        self.clockwise = None
        self.counterclockwise = None

        self.average_floor_color = [0, 0, 0]

    def initialize(self, using_custom_floor_color_as_string):
        """ Sets the algorithm that lets the robot map out the floor plan. """

        if using_custom_floor_color_as_string == '1':
            using_custom_floor_color = True
        else:
            using_custom_floor_color = False

        self.robot.sound.set_wait_time(2)

        # self.robot.sound.speak("Put me in a corner facing facing a wall, then press the touch sensor to start.")

        while True:
            if self.robot.touch_sensor.is_pressed():
                self.run_floor_plan_algorithm(using_custom_floor_color)
                break

    def run_floor_plan_algorithm(self, custom_floor_color):
        """ Determines whether to move clockwise or counterclockwise to map the walls."""
        self.robot.drive_system.turn_degrees(90, 100)
        if self.robot.proximity_sensor.get_distance_to_nearest_object_in_inches() <= 6:
            self.counterclockwise = True
        self.robot.drive_system.turn_degrees(180, -100)
        if self.robot.proximity_sensor.get_distance_to_nearest_object_in_inches() <= 6:
            self.clockwise = True

        if self.counterclockwise and self.clockwise:
            print("The robot appears to be in a tight corridor. It should be up against only two walls. Aborting.")

        if not self.counterclockwise and not self.clockwise:
            print("The robot appears to not be in a corner. Aborting.")

        if self.counterclockwise and not self.clockwise:
            self.robot.sound.speak("Starting Counterclockwise Movement.")
            self.floor_plan(custom_floor_color, -1)

        if not self.counterclockwise and self.clockwise:
            self.robot.sound.speak("Starting Clockwise Movement.")
            self.floor_plan(custom_floor_color, 1)

        print(custom_floor_color)

    def floor_plan(self, custom_floor_color, n):
        """ General algorithm for determining the layout of a room and sending positional
        information about the room back to to laptop. """
        while True:

            count = -1
            self.robot.drive_system.go_straight_inches(10, 80)
            count += 1
            self.check_for_missing_walls(10, n)
            if not custom_floor_color:
                color_tuple = self.robot.color_sensor.get_value()
                for k in range(len(color_tuple)):
                    self.average_floor_color[k] = (self.average_floor_color[k] + color_tuple[k])/(count + 1)
            elif self.robot.proximity_sensor.get_distance_to_nearest_object_in_inches() <= 6:
                self.robot.drive_system.turn_degrees(90, math.copysign(100, n))
            elif math.sqrt(self.robot.drive_system.x_coord_in_inches ** 2 +
                           self.robot.drive_system.y_coord_in_inches ** 2) <= 1 and count > 4:
                break

    def check_for_missing_walls(self, inches, n):
        """
        Checks to ensure the robot remains along the wall if the wall has a corner that turns away
        from the path of the robot. Automatically heads back until it finds the wall and turns down it.
        """

        self.robot.drive_system.turn_degrees(90, math.copysign(100, -n))
        if self.robot.proximity_sensor.get_distance_to_nearest_object_in_inches() >= 6:
            self.robot.drive_system.turn_degrees(90, math.copysign(100, n))
            self.robot.drive_system.go_straight_inches(inches/2, -80)
            self.check_for_missing_walls(inches/2, n)
        elif inches == 10:
            self.robot.drive_system.turn_degrees(90, math.copysign(100, n))
        else:
            self.robot.drive_system.go_straight_inches(6)
            self.robot.drive_system.turn_degrees(90, math.copysign(100, -n))


main()
