import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class ListenerNode(Node):
    
    def __init__(self):

        super().__init__("listener")

        self.subscription = self.create_subscription(
            String, 'topic', self.listener_callback, 10
        )


    def listener_callback(self, msg):
        self.get_logger().info(f'Recivido {msg.data}')




def main(args = None):
    rclpy.init(args= args)

    #creacion 
    listener = ListenerNode()

    #uso 
    rclpy.spin(listener)

    #destruccion 
    listener.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()