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
            " How the user controls the robot "
            if robot.beacon_button_sensor.is_top_red_button_pressed():
                    robot.drive_system.start_moving(100, 100)
            elif robot.beacon_button_sensor.is_top_blue_button_pressed():
                robot.drive_system.start_moving(-100, -100)
            elif robot.beacon_button_sensor.is_bottom_red_button_pressed():
                robot.drive_system.stop_moving()
            elif robot.beacon_button_sensor.is_bottom_blue_button_pressed():
                robot.drive_system.stop_moving()
                robot.drive_system.right_wheel.start_spinning(100)
            elif robot.touch_sensor.is_pressed():
                robot.drive_system.stop_moving()
            time.sleep(.01)


def object_area():
    robot = rb.Snatch3rRobot()
    width = robot.camera.get_biggest_blob().width
    height = robot.camera.get_biggest_blob().height
    area = width * height
    return area


class RemoteControlEtc(object):
    def __init__(self, robot):
        """
        Stores the robot.
            :type robot: rb.Snatch3rRobot
        """
        self.robot = robot
        self.width = self.robot.camera.get_biggest_blob().width
        self.height = self.robot.camera.get_biggest_blob().height
        self.area = self.width * self.height

    def get_near_object(self):
        while True:
            width = self.robot.camera.get_biggest_blob().width
            height = self.robot.camera.get_biggest_blob().height

            area = width * height
            if area > 300:
                self.robot.sound.speak('Yes, I can see the object')
                self.robot.sound.set_wait_time(.05)
            elif object_area() < 100:
                self.robot.sound.speak('No, I cannot see the object')
                self.robot.sound.set_wait_time(.05)
            elif object_area() > 500:
                self.robot.sound.speak('I found the object, so I will stop looking')
                break




main()
