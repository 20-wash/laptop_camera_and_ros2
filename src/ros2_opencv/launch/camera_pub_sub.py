import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Publisher Node
        Node(
            package='ros2_opencv',  # Your package name
            executable='cameraPublisher.py',  # Your publisher node script
            name='publisher_node',
            output='screen',
            parameters=[{'camera_device': '0'}]  # Optional parameters, add if needed
        ),
        
        # Subscriber Node
        Node(
            package='ros2_opencv',  # Your package name
            executable='subscriberImage.py',  # Your subscriber node script
            name='subscriber_node',
            output='screen'
        )
    ])
