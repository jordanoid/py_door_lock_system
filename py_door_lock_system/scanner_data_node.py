#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy
from std_msgs.msg import String
import threading
import serial

class Scanner(Node):
    def __init__(self):
        super().__init__('scanner_data_node')
        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )
        self.qrdata_pub = self.create_publisher(String, 'qrdata', qos_profile=qos_profile)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.data_publish)
        

    def data_publish(self):
        decoded_data = String()
        try:
            ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  # Adjust the port and baud rate as needed
            data = ser.readline()
            if data:
                decoded_data.data = data.decode('utf-8')
                self.qrdata_pub.publish(decoded_data)
        except serial.SerialException as e:
            rclpy.get_logger().error(f"SerialException: {e}")
        finally:
            if ser.is_open:
                ser.close()
def main(args=None):
    rclpy.init(args=args)
    
    scanner_data = Scanner()

    th = threading.Thread(target=scanner_data.data_publish)   
    th.start=()
    
    rclpy.spin(scanner_data)
    
    scanner_data.destroy_node()
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()