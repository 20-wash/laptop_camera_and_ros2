import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/biswash/ws_ros2_camera/install/ros2_opencv'
