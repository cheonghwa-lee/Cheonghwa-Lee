'''
    Generated automatically by Splash Code Generator for processing_steering
'''
from std_msgs.msg import Float32

from scl.components import *
from scl.impl.singleton import Singleton

class ProcessingSteering(Component, metaclass=Singleton):
    def __init__(self):
        super().__init__(name="processing_steering", factory=None, mode=None)
        self.distance_constant = 11.0 / 2
        self.angle_z_constant = 3.14 / 2
        self.recovery_ratio = 1.0
        self.recovery_ratio1 = 0.15
        self.recovery_ratio2 = 0.05
        self.direction_ratio = 2.0
        self.prev_error = 0
        # self.k_d = 0
        #self.dt = 10
        self.flag = False
        self.angle_z_target = None
        self.target_updated_time = None

    def setup(self):
        self.attach_stream_input_port(channel="fusion1", callback=self.user_callback_1, from_fusion=True)
        self.attach_stream_output_port(msg_type=Float32, channel="processing_steering")
        self.declare_parameter('gain', (0.3, 0.0, 0.0))

    def run(self):
        pass
    
    def user_callback_1(self, msg):
        linear_x = msg.source_linear_x.data
        distance_mid = msg.source_distance_mid.data
        angle_z = msg.source_angle_z.data

        # self.get_logger().info("linear_x: {} distance_mid: {} angle_z: {}".format(linear_x, distance_mid, angle_z))
        
        new_msg = Float32()
        # new_msg.data = -(distance_mid / 5.5)
        # new_msg.data = angle_z - (distance_mid / 5.5) * 0.3#(3.14 / 4)
        new_msg.data = angle_z - (distance_mid / 5.5) * angle_z#(3.14 / 4)
        # self.get_logger().info("#####################################")
        self.write("processing_steering", new_msg)
        
    
    

