#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class QRDecoder(Node):
    def __init__(self):
        super().__init__('QR_decoder_node')
        self.subscription = self.create_subscription(Image, '/image_raw', self.decode_callback, 10)
        self.subscription
        self.bridge = CvBridge()
        
    def decode_callback(self, msg):
        self.get_logger().info("Receiving frame")
        frame = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        
        cv2.imshow("camera", frame)
        cv2.waitKey(1)
        
def main(args=None):
    rclpy.init(args=args)
    
    qr_decode = QRDecoder()
    
    rclpy.spin(qr_decode)
    
    qr_decode.destroy_node()
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()