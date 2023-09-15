#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy
from std_srvs.srv import Empty
from std_msgs.msg import Bool
import RPi.GPIO as GPIO
import time

relay_gpio = 23

class LockService(Node):
    def __init__(self):
        super().__init__('Lock_Service_Node')
        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )
        self.srv = self.create_service(Empty, "trigger_lock", self.lock_service_callback)
        self.lock_pub = self.create_publisher(Bool, "lock_state", qos_profile=qos_profile)
        self.lock_state = Bool()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(relay_gpio, GPIO.OUT)

    def lock_service_callback(self, request, response):
        self.get_logger().info("Door Open")
        GPIO.output(relay_gpio, GPIO.HIGH)
        self.lock_state.data = False
        self.lock_pub.publish(self.lock_state)
        time.sleep(3)
        self.get_logger().info("Door Close")
        GPIO.output(relay_gpio, GPIO.LOW)
        self.lock_state.data = True
        self.lock_pub.publish(self.lock_state)
        return response

def main(args=None):
    rclpy.init(args=args)
    
    lock_service = LockService()
    
    rclpy.spin(lock_service)
    
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()