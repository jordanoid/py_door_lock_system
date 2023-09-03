#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_srvs.srv import Empty
# import RPi.GPIO as GPIO
import time

relay_gpio = 16

class LockService(Node):
    def __init__(self):
        super().__init__('Lock_Service_Node')
        self.srv = self.create_service(Empty, "trigger_lock", self.lock_service_callback)
        # GPIO.setmode(GPIO.BOARD)
        # GPIO.setup(relay_gpio, GPIO.OUT)

    def lock_service_callback(self, request, response):
        self.get_logger().info("Door Open")
        # GPIO.output(relay_gpio, True)
        # time.sleep(5)
        # GPIO.output(relay_gpio, False)
        return response

def main(args=None):
    rclpy.init(args=args)
    
    lock_service = LockService()
    
    rclpy.spin(lock_service)
    
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()