'''
    Generated automatically by Splash Code Generator for sink_accel
'''
from std_msgs.msg import Float32, Int32

from scl.components import *
from scl.impl.singleton import Singleton

from evdev import *

class SinkAccel(Component, metaclass=Singleton):
    def __init__(self):
        super().__init__(name="sink_accel", factory=None, mode=None)
        super().__init__(name="sink_steering", factory=None, mode=None)
        # dev = InputDevice('/dev/input/event3')
    
    def setup(self):
        self.attach_stream_input_port(msg_type=Float32, channel="processing_accel", callback=self.user_callback_1)
        # self.create_subscription(Float32, "", self.run, 1)
        self.acc_publisher = self.create_publisher(Float32, "accel_command", 1)
        self.brk_publisher = self.create_publisher(Float32, "brake_command", 1)
        self.str_publisher = self.create_publisher(Float32, "steering_command", 1)
        self.gear_publisher = self.create_publisher(Int32, "gear_command", 1)

    def run(self):
        # pass

        dev = InputDevice('/dev/input/event3')
        print(dev)

        for event in dev.read_loop():
            if event.type == ecodes.EV_KEY and event.code == 103:
                if event.value == 0:
                    accel = 0.0
                    new_msg_acc = Float32()
                    new_msg_acc.data = accel
                    self.get_logger().info("3: {}".format(accel))
                    self.acc_publisher.publish(new_msg_acc)
                else:
                    accel = 1.0
                    new_msg_acc = Float32()
                    new_msg_acc.data = accel
                    self.get_logger().info("4: {}".format(accel))
                    self.acc_publisher.publish(new_msg_acc)
            elif event.type == ecodes.EV_KEY and event.code == 108:
                if event.value == 0:
                    brake = 0.0
                    new_msg_brk = Float32()
                    new_msg_brk.data = brake
                    self.get_logger().info("1: {}".format(brake))
                    self.brk_publisher.publish(new_msg_brk)
                else:
                    brake = 1.0
                    new_msg_brk = Float32()
                    new_msg_brk.data = brake
                    self.get_logger().info("2: {}".format(brake))
                    self.brk_publisher.publish(new_msg_brk)
            elif event.type == ecodes.EV_KEY and event.code == 105:
                if event.value == 0:
                    steering = 0.0
                    new_msg = Float32()
                    new_msg.data = steering
                    self.str_publisher.publish(new_msg) 
                else:
                    steering = 0.5
                    new_msg = Float32()
                    new_msg.data = steering
                    self.str_publisher.publish(new_msg) 
            elif event.type == ecodes.EV_KEY and event.code == 106:
                if event.value == 0:
                    steering = 0.0
                    new_msg = Float32()
                    new_msg.data = steering
                    self.str_publisher.publish(new_msg) 
                else:
                    steering = -0.5
                    new_msg = Float32()
                    new_msg.data = steering
                    self.str_publisher.publish(new_msg) 
            elif event.type == ecodes.EV_KEY and event.code == 11:
                if event.value == 1:
                    gear = -1
                    new_msg = Int32()
                    new_msg.data = gear
                    self.gear_publisher.publish(new_msg) 
            elif event.type == ecodes.EV_KEY and event.code == 41:
                if event.value == 1:
                    gear = 0
                    new_msg = Int32()
                    new_msg.data = gear
                    self.gear_publisher.publish(new_msg) 
            elif event.type == ecodes.EV_KEY and event.code == 2:
                if event.value == 1:
                    gear = 1
                    new_msg = Int32()
                    new_msg.data = gear
                    self.get_logger().info("100: {}".format(gear))
                    self.gear_publisher.publish(new_msg) 
            elif event.type == ecodes.EV_KEY and event.code == 3:
                if event.value == 1:
                    gear = 2
                    new_msg = Int32()
                    new_msg.data = gear
                    self.gear_publisher.publish(new_msg)   
            elif event.type == ecodes.EV_KEY and event.code == 4:
                if event.value == 1:
                    gear = 3
                    new_msg = Int32()
                    new_msg.data = gear
                    self.gear_publisher.publish(new_msg)    
            elif event.type == ecodes.EV_KEY and event.code == 5:
                if event.value == 1:
                    gear = 4
                    new_msg = Int32()
                    new_msg.data = gear
                    self.gear_publisher.publish(new_msg)    
            elif event.type == ecodes.EV_KEY and event.code == 6:
                if event.value == 1:
                    gear = 5
                    new_msg = Int32()
                    new_msg.data = gear
                    self.gear_publisher.publish(new_msg)    
            elif event.type == ecodes.EV_KEY and event.code == 7:
                if event.value == 1:
                    gear = 6
                    new_msg = Int32()
                    new_msg.data = gear
                    self.gear_publisher.publish(new_msg)          
                
            
    
    def user_callback_1(self, msg):
        linear_x_command = msg.data
        accel = 0.0
        if linear_x_command > 1.0:
            accel = 1.0
        elif linear_x_command < 0.0:
            accel = 0.01
        else:
            accel = linear_x_command

        new_msg_acc = Float32()
        new_msg_acc.data = accel
        self.acc_publisher.publish(new_msg_acc)
        
    
    

