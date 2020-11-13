'''
    Generated automatically by Splash Code Generator for sink_steering
'''
from std_msgs.msg import Float32

from scl.components import *
from scl.impl.singleton import Singleton

class SinkSteering(Component, metaclass=Singleton):
    def __init__(self):
        super().__init__(name="sink_steering", factory=None, mode=None)
    
    def setup(self):
        self.attach_stream_input_port(msg_type=Float32, channel="processing_steering", callback=self.user_callback_1)
        self.publisher = self.create_publisher(Float32, "steering_command", 1)

    def run(self):
        pass
    
    def user_callback_1(self, msg):
        angle_z_command = msg.data
        self.get_logger().info("angle_z_command: {}".format(angle_z_command))
        # steering_command = angle_z_command * 2 / 3
        # steering = max(-1.0, min(1.0, angle_z_command))
        
        steering_command = angle_z_command 

        steering = 0.0
        if steering_command > 1.0:
            steering = 1.0
        elif steering_command < -1.0:
            steering = -1.0
        else:
            steering = steering_command

        # steering = 0.5

        self.get_logger().info("steering: {}".format(steering))
        #steering = angle_z_command
        new_msg = Float32()
        new_msg.data = steering

        self.publisher.publish(new_msg)
        
    
    

