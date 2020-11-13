'''
    Generated automatically by Splash Code Generator for stream_port_1
'''
from scl.channel import StreamOutputPort
from ..component.source_linear_x import SourceLinearX

class StreamPort1(StreamOutputPort):
    def __init__(self):
        super().__init__(name="stream_port_1", parent=SourceLinearX())

'''
    Generated automatically by Splash Code Generator for stream_port_2
'''
from scl.channel import StreamOutputPort
from ..component.source_distance_mid import SourceDistanceMid

class StreamPort2(StreamOutputPort):
    def __init__(self):
        super().__init__(name="stream_port_2", parent=SourceDistanceMid())

'''
    Generated automatically by Splash Code Generator for stream_port_3
'''
from scl.channel import StreamOutputPort
from ..component.source_angle_z import SourceAngleZ

class StreamPort3(StreamOutputPort):
    def __init__(self):
        super().__init__(name="stream_port_3", parent=SourceAngleZ())

'''
    Generated automatically by Splash Code Generator for stream_port_4
'''
from scl.channel import StreamInputPort
from ..component.processing_accel import ProcessingAccel

class StreamPort4(StreamInputPort):
    def __init__(self):
        super().__init__(name="stream_port_4", parent=ProcessingAccel())

'''
    Generated automatically by Splash Code Generator for stream_port_5
'''
from scl.channel import StreamOutputPort
from ..component.processing_accel import ProcessingAccel

class StreamPort5(StreamOutputPort):
    def __init__(self):
        super().__init__(name="stream_port_5", parent=ProcessingAccel())

'''
    Generated automatically by Splash Code Generator for stream_port_6
'''
from scl.channel import StreamInputPort
from ..component.sink_accel import SinkAccel

class StreamPort6(StreamInputPort):
    def __init__(self):
        super().__init__(name="stream_port_6", parent=SinkAccel())

'''
    Generated automatically by Splash Code Generator for stream_port_7
'''
from scl.channel import StreamOutputPort
from ..component.fusion_operator_1 import FusionOperator1

class StreamPort7(StreamOutputPort):
    def __init__(self):
        super().__init__(name="stream_port_7", parent=FusionOperator1())

'''
    Generated automatically by Splash Code Generator for stream_port_8
'''
from scl.channel import StreamInputPort
from ..component.fusion_operator_1 import FusionOperator1

class StreamPort8(StreamInputPort):
    def __init__(self):
        super().__init__(name="stream_port_8", parent=FusionOperator1())

'''
    Generated automatically by Splash Code Generator for stream_port_9
'''
from scl.channel import StreamInputPort
from ..component.fusion_operator_1 import FusionOperator1

class StreamPort9(StreamInputPort):
    def __init__(self):
        super().__init__(name="stream_port_9", parent=FusionOperator1())

'''
    Generated automatically by Splash Code Generator for stream_port_10
'''
from scl.channel import StreamInputPort
from ..component.fusion_operator_1 import FusionOperator1

class StreamPort10(StreamInputPort):
    def __init__(self):
        super().__init__(name="stream_port_10", parent=FusionOperator1())

'''
    Generated automatically by Splash Code Generator for stream_port_11
'''
from scl.channel import StreamInputPort
from ..component.processing_steering import ProcessingSteering

class StreamPort11(StreamInputPort):
    def __init__(self):
        super().__init__(name="stream_port_11", parent=ProcessingSteering())

'''
    Generated automatically by Splash Code Generator for stream_port_12
'''
from scl.channel import StreamOutputPort
from ..component.processing_steering import ProcessingSteering

class StreamPort12(StreamOutputPort):
    def __init__(self):
        super().__init__(name="stream_port_12", parent=ProcessingSteering())

'''
    Generated automatically by Splash Code Generator for stream_port_13
'''
from scl.channel import StreamInputPort
from ..component.sink_steering import SinkSteering

class StreamPort13(StreamInputPort):
    def __init__(self):
        super().__init__(name="stream_port_13", parent=SinkSteering())

