import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class ListenerNode(Node):
    
    def __init__(self, topic:str = 'topic', name:str = 'listener_gui'):

        super().__init__(name)
        self.subscription = self.create_subscription(
            String, topic, self.listener_callback, 10
        )

    def listener_callback(self, msg):
        self.get_logger().info(f'Recivido {msg.data}')





