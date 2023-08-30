#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import cv2
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError
from pyzbar.pyzbar import decode

class QRDecoder(Node):
    def __init__(self):
        super().__init__('QR_decoder_node')
        self.image_sub = self.create_subscription(Image, '/image_raw', self.decode_callback, 10)
        self.image_sub
        self.qrdata_pub = self.create_publisher(String, 'camera/qrdata', 10)
        self.bridge = CvBridge()
        
    def decode_callback(self, msg):
        # self.get_logger().info("Receiving frame")
        frame = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        
        detectedBarcodes = decode(frame)
        if len(detectedBarcodes) > 0:
            data_read = detectedBarcodes[0].data.decode()
            qr_msg = String()
            qr_msg.data = data_read
            self.qrdata_pub.publish(qr_msg)
        
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