'''
    Generated automatically by Splash Code Generator for fusion_operator_1
'''
from std_msgs.msg import Float32

from scl.components import *
from scl.impl.singleton import Singleton

class FusionOperator1(FusionOperator, metaclass=Singleton):
    def __init__(self):
        super().__init__(name="fusion_operator_1", factory=None, mode=None)
    
    def setup(self):
        self.attach_stream_input_port(msg_type=Float32, channel="source_linear_x")
        self.attach_stream_input_port(msg_type=Float32, channel="source_distance_mid")
        self.attach_stream_input_port(msg_type=Float32, channel="source_angle_z")
        self.attach_stream_output_port(channel="fusion1")
    
    def run(self):
        pass
    
    

