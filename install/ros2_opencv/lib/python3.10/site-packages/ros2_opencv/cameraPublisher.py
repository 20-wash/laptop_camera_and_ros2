import cv2
import rclpy
from sensor_msgs.msg import Image
from rclpy.node import Node
from cv_bridge import CvBridge

class PublisherNodeClass(Node):
    def __init__(self):
        super().__init__('publisher_node')
        
        # Set camera device number
        self.cameraDeviceNumber = 0
        self.camera = cv2.VideoCapture(self.cameraDeviceNumber)
        
        # Initialize CvBridge for converting OpenCV images to ROS2 messages
        self.bridgeObject = CvBridge()

        # Topic name for publishing camera images
        self.topicNameFrames = 'topic_camera_image'
        
        # Queue size for messages
        self.queueSize = 20
        
        # Create publisher
        self.publisher = self.create_publisher(Image, self.topicNameFrames, self.queueSize)
        
        # Communication period in seconds
        self.periodComunication = 0.02
        
        # Create timer to call self.timer_callbackFunction every self.periodComunication seconds
        self.timer = self.create_timer(self.periodComunication, self.timer_callbackFunction)
        
        # Image counter
        self.i = 0  

    def timer_callbackFunction(self):
        # Capture frame from camera
        success, frame = self.camera.read()
        
        # Resize image
        frame = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_CUBIC)
        
        if success:
            # Convert OpenCV image to ROS2 Image message
            ros2_image_message = self.bridgeObject.cv2_to_imgmsg(frame, encoding="bgr8")
            
            # Publish the image
            self.publisher.publish(ros2_image_message)
            
            # Log message
            self.get_logger().info('Publishing image number %d' % self.i)
            
            # Increment counter
            self.i += 1

def main(args=None):
    rclpy.init(args=args)
    
    # Create and run the publisher node
    publisherObject = PublisherNodeClass()
    rclpy.spin(publisherObject)
    
    # Cleanup
    publisherObject.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
