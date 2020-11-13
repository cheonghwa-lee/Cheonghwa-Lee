'''
    Generated automatically by Splash Code Generator for processing_accel
'''
from std_msgs.msg import Float32

from scl.components import *
from scl.impl.singleton import Singleton

class ProcessingAccel(Component, metaclass=Singleton):
    def __init__(self):
        super().__init__(name="processing_accel", factory=None, mode=None)
        self.linear_x_target = 100.0
        self.prev_error = 0
        self.dt = 1
        self.prev_linear_x = 0
        self.cur_linear_x = 0

    def setup(self):
        self.attach_stream_input_port(msg_type=Float32, channel="source_linear_x", callback=self.user_callback_1)
        self.attach_stream_output_port(msg_type=Float32, channel="processing_accel")
        self.declare_parameter('gain2', (0.2, 0.0, 0.0))

    def run(self):
        pass
    
    def user_callback_1(self, msg):
        error = self.linear_x_target - msg.data
        gain = self.get_parameter("gain2").value
        kp = gain[0]
        ki = gain[1]
        kd = gain[2]

        new_msg = Float32()
        new_msg.data = kp*error + ki*(self.prev_error + error*self.dt) + kd*(error/self.dt)
        self.write("processing_accel", new_msg)
        
    
    

