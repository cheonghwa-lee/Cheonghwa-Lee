'''
    Generated automatically by Splash Code Generator for default_build_unit
'''
import rclpy
from rclpy.executors import MultiThreadedExecutor

from scl.link import Link
from scl.build_unit import BuildUnit

from ..component.processing_accel import ProcessingAccel
from ..component.processing_steering import ProcessingSteering

from ..component.source_linear_x import SourceLinearX
from ..component.source_distance_mid import SourceDistanceMid
from ..component.source_angle_z import SourceAngleZ

from ..component.sink_accel import SinkAccel
from ..component.sink_steering import SinkSteering

from ..component.fusion_operator_1 import FusionOperator1

from ..stream_port import *

class DefaultBuildUnit(BuildUnit):
    def __init__(self):
        super().__init__()
        processing_accel = ProcessingAccel()
        processing_accel.set_links(links=[Link(StreamPort1(), StreamPort4(), "source_linear_x"), Link(StreamPort5(), StreamPort6(), "processing_accel")])
        processing_accel.set_build_unit(self)
        processing_accel.setup()
        self.components.append(processing_accel)
        
        processing_steering = ProcessingSteering()
        processing_steering.set_links(links=[Link(StreamPort12(), StreamPort13(), "processing_steering"), Link(StreamPort7(), StreamPort11(), "fusion1")])
        processing_steering.set_build_unit(self)
        processing_steering.setup()
        self.components.append(processing_steering)
        
        source_linear_x = SourceLinearX()
        source_linear_x.set_links(links=[Link(StreamPort1(), StreamPort4(), "source_linear_x"), Link(StreamPort1(), StreamPort8(), "source_linear_x")])
        source_linear_x.set_build_unit(self)
        source_linear_x.setup()
        self.components.append(source_linear_x)
        
        source_distance_mid = SourceDistanceMid()
        source_distance_mid.set_links(links=[Link(StreamPort2(), StreamPort9(), "source_distance_mid")])
        source_distance_mid.set_build_unit(self)
        source_distance_mid.setup()
        self.components.append(source_distance_mid)
        
        source_angle_z = SourceAngleZ()
        source_angle_z.set_links(links=[Link(StreamPort3(), StreamPort10(), "source_angle_z")])
        source_angle_z.set_build_unit(self)
        source_angle_z.setup()
        self.components.append(source_angle_z)
        
        sink_accel = SinkAccel()
        sink_accel.set_links(links=[Link(StreamPort5(), StreamPort6(), "processing_accel")])
        sink_accel.set_build_unit(self)
        sink_accel.setup()
        self.components.append(sink_accel)
        
        sink_steering = SinkSteering()
        sink_steering.set_links(links=[Link(StreamPort12(), StreamPort13(), "processing_steering")])
        sink_steering.set_build_unit(self)
        sink_steering.setup()
        self.components.append(sink_steering)
        
        fusion_operator_1 = FusionOperator1()
        fusion_operator_1.set_links(links=[Link(StreamPort1(), StreamPort8(), "source_linear_x"), Link(StreamPort2(), StreamPort9(), "source_distance_mid"), Link(StreamPort3(), StreamPort10(), "source_angle_z"), Link(StreamPort7(), StreamPort11(), "fusion1")])
        fusion_operator_1.set_build_unit(self)
        fusion_operator_1.set_fusion_rule(fusion_rule={'optional_ports': ['stream_port_10'], 'mandatory_ports': ['stream_port_8', 'stream_port_9'], 'optional_ports_threshold': '0', 'correlation': '100'})
        fusion_operator_1.setup()
        self.components.append(fusion_operator_1)
        

