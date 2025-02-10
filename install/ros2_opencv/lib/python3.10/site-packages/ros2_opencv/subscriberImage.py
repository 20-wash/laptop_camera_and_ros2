import cv2
import rclpy
from sensor_msgs.msg import Image
from rclpy.node import Node
from cv_bridge import CvBridge

class SubscriberNodeClass(Node):
    def __init__(self):
        super().__init__('subscriber_node')

        # Initialize CvBridge for converting ROS2 images to OpenCV format
        self.bridgeObject = CvBridge()

        # Topic name must match the publisher's topic
        self.topicNameFrames = 'topic_camera_image'

        # Queue size for messages
        self.queueSize = 20

        # Create subscriber to receive images from the topic
        self.subscription = self.create_subscription(
            Image, self.topicNameFrames, self.listener_callbackFunction, self.queueSize
        )

    def listener_callbackFunction(self, imageMessage):
        # Log message when an image is received
        self.get_logger().info('The image frame is received')

        # Convert ROS2 Image message to OpenCV format
        openCVImage = self.bridgeObject.imgmsg_to_cv2(imageMessage, desired_encoding="bgr8")

        # Display the received image
        cv2.imshow("Camera Video", openCVImage)
        cv2.waitKey(1)  # Ensures OpenCV updates the window

def main(args=None):
    # Initialize rclpy
    rclpy.init(args=args)

    # Create subscriber node object
    subscriberNode = SubscriberNodeClass()

    # Keep spinning until shutdown
    rclpy.spin(subscriberNode)

    # Cleanup
    subscriberNode.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
