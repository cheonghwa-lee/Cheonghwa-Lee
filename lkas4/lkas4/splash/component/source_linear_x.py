'''
    Generated automatically by Splash Code Generator for source_linear_x
'''
from std_msgs.msg import Float32
from geometry_msgs.msg import TwistStamped

from scl.components import *
from scl.impl.singleton import Singleton

class SourceLinearX(Component, metaclass=Singleton):
    def __init__(self):
        super().__init__(name="source_linear_x", factory=None, mode=None)
    
    def setup(self):
        self.create_subscription(TwistStamped, "torcs_speed", self.torcs_speed_callback, 1)
        self.attach_stream_output_port(msg_type=Float32, channel="source_linear_x")

    def run(self):
        pass
    
    def torcs_speed_callback(self, msg):
        # self.get_logger().info("cur speed: {}".format(msg.twist.linear.x))
        linear_x = msg.twist.linear.x

        new_msg = Float32()
        new_msg.data = linear_x

        self.write("source_linear_x", new_msg)
    
    
    

