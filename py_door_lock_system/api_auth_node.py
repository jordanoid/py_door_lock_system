#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy
from std_srvs.srv import Empty
from std_msgs.msg import String

class Authenticator(Node):
    def __init__(self):
        super().__init__("Authenticator_Node")
        qos_profile = QoSProfile(
            realibility=ReliabilityPolicy.BEST_EFFORT,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )
        self.qrdata_sub = self.create_subscription(String, 'camera/qrdata', self.qrdata_callback, qos_profile)
        self.qrdata_sub
        self.client = self.create_client(Empty, 'trigger_lock')
        self.req = Empty.Request()
        self.data_in = ""
        
        
    def trigger_srv(self):
        self.future = self.client.call_async(self.req)



    def qrdata_callback(self, msg):
        self.data_in = msg.data
        self.get_logger().info(self.data_in)
        if self.data_in == "opentest":
            self.trigger_srv()

def main(args=None):
    rclpy.init(args=args)
    
    api_auth = Authenticator()
 
    rclpy.spin(api_auth)
    api_auth.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()