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
        self.direction_ratio = 2.0
        self.prev_error = 0
        # self.k_d = 0
        #self.dt = 10
        self.flag = False
        self.angle_z_target = None
        self.target_updated_time = None
        self.distance_constant = 5.5 - 1.5
        self.direction_target = 0.0
        self.prev_error = 0
        self.dt = 1

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
        
        if abs(distance_mid) < 1.0:
            direction = angle_z - (distance_mid / self.distance_constant) * 0.1
        elif abs(distance_mid) < 2.0:
            direction = angle_z - (distance_mid / self.distance_constant) * 0.2
        elif abs(distance_mid) < 3.0:
            direction = angle_z - (distance_mid / self.distance_constant) * 0.3
        elif abs(distance_mid) < 4.0:
            direction = angle_z - (distance_mid / self.distance_constant) * 0.4
        else:
            direction = angle_z - (distance_mid / self.distance_constant) * 0.5

        error = self.direction_target - direction
        gain = self.get_parameter("gain").value
        kp = gain[0]
        ki = gain[1]
        kd = gain[2]

        new_msg = Float32()
        new_msg.data = kp*error + ki*(self.prev_error + error*self.dt) + kd*(error/self.dt)
        new_msg.data = direction 
        # new_msg.data = angle_z
        self.write("processing_steering", new_msg)

        # if abs(distance_mid) > 3.5:
        #     direction = angle_z - (distance_mid / 5.5) * 0.45
        # elif abs(distance_mid) > 2.5:
        #     direction = angle_z - (distance_mid / 5.5) * 0.25
        # elif abs(distance_mid) > 1.5:
        #     direction = angle_z - (distance_mid / 5.5) * 0.15
        # else:
        #     direction = angle_z - (distance_mid / 5.5) * angle_z
    
        # if abs(distance_mid) > 5.5:
        #     direction = angle_z - (distance_mid / 5.5) * 0.55
        # elif abs(distance_mid) > 4.5:
        #     direction = angle_z - (distance_mid / 5.5) * 0.50
        # elif abs(distance_mid) > 3.5:
        #     direction = angle_z - (distance_mid / 5.5) * 0.45
        # elif abs(distance_mid) > 2.5:
        #     direction = angle_z - (distance_mid / 5.5) * 0.25
        # elif abs(distance_mid) > 1.5:
        #     direction = angle_z - (distance_mid / 5.5) * 0.15
        # elif abs(distance_mid) > 0.5:
        #     direction = angle_z - (distance_mid / 5.5) * 0.05
        # else:
        #     direction = angle_z - (distance_mid / 5.5) * angle_z

