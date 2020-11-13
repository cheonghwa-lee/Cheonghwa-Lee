'''
    Generated automatically by Splash Code Generator for sink_steering
'''
from std_msgs.msg import Float32

from scl.components import *
from scl.impl.singleton import Singleton

from evdev import *

class SinkSteering(Component, metaclass=Singleton):
    def __init__(self):
        super().__init__(name="sink_steering", factory=None, mode=None)
    
    def setup(self):
        self.attach_stream_input_port(msg_type=Float32, channel="processing_steering", callback=self.user_callback_1)
        self.str_publisher = self.create_publisher(Float32, "steering_command", 1)

    def run(self):
        pass

        # dev = InputDevice('/dev/input/event3')
        # print(dev)

        # for event in dev.read_loop():
        #     if event.type == ecodes.EV_KEY and event.code == 105:
        #         if event.value == 0:
        #             steering = 0.0
        #             new_msg = Float32()
        #             new_msg.data = steering
        #             self.str_publisher.publish(new_msg) 
        #         else:
        #             steering = 1.0
        #             new_msg = Float32()
        #             new_msg.data = steering
        #             self.str_publisher.publish(new_msg) 
        #     elif event.type == ecodes.EV_KEY and event.code == 106:
        #         if event.value == 0:
        #             steering = 0.0
        #             new_msg = Float32()
        #             new_msg.data = steering
        #             self.str_publisher.publish(new_msg) 
        #         else:
        #             steering = -1.0
        #             new_msg = Float32()
        #             new_msg.data = steering
        #             self.str_publisher.publish(new_msg) 
    
    def user_callback_1(self, msg):
        angle_z_command = msg.data
        steering_command = angle_z_command

        if steering_command > 1.0:
            steering = 1.0
        elif steering_command < -1.0:
            steering = -1.0
        else:
            steering = steering_command
        
        steering = steering_command

        new_msg = Float32()
        new_msg.data = steering
        self.str_publisher.publish(new_msg)
        
    
    

