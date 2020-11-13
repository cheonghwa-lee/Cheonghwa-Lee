'''
    Generated automatically by Splash Code Generator for source_angle_z
'''
from std_msgs.msg import Float32
from torcs_interfaces.msg import TORCSSensors

from scl.components import *
from scl.impl.singleton import Singleton

class SourceAngleZ(Component, metaclass=Singleton):
    def __init__(self):
        super().__init__(name="source_angle_z", factory=None, mode=None)
    
    def setup(self):
        self.create_subscription(TORCSSensors, "torcs_sensors_out", self.torcs_sensor_callback, 1)
        self.attach_stream_output_port(msg_type=Float32, channel="source_angle_z")
    
    def run(self):
        pass
    
    def torcs_sensor_callback(self, msg):
        angle_z = msg.angle
        new_msg = Float32()
        new_msg.data = angle_z
        self.write("source_angle_z", new_msg)
    
    

