from launch import LaunchDescription
from launch_ros.actions import Node
def generate_launch_description():
    return LaunchDescription([
        Node(package='lkas4', executable='splash_server'),
        Node(package='lkas4', executable='default_build_unit'),
    ])
