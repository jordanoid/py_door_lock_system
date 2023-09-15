#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy
from std_msgs.msg import String
import threading

class Scanner(Node):
    def __init__(self):
        super().__init__('scanner_data_node')
        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )
        self.qrdata_pub = self.create_publisher(String, 'qrdata', qos_profile=qos_profile)
        

    def data_publish(self):
        while True:
            data_read = input("Scan hre")
            qr_msg = String()
            qr_msg.data = data_read
            self.qrdata_pub.publish(qr_msg)
            self.get_logger().info("MSG Published")
        
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