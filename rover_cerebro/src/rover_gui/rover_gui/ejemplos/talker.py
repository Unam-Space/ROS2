import rclpy
from rclpy.node import Node
import serial
from std_msgs.msg import String

class TalkerNode(Node):

    def __init__(self):

        super().__init__("talker")

        self.publisher_ = self.create_publisher(String, 'topic', 10)
        time_period = 0.5
        self.timer = self.create_timer(time_period, self.time_callback)
        self.count = 0


    def time_callback(self):
        msg = String()
        msg.data = f'Holi {self.count}'

        self.publisher_.publish(msg)

        self.count += 1

        if self.count%5 == 0:
            msg = String()
            msg.data = 'pan ============================================'
            self.publisher_.publish(msg)


        #self.get_logger().info(f"Publicando {msg.data}")

def main(args = None):
    rclpy.init(args= args)

    #creacion
    talker = TalkerNode()

    #uso
    rclpy.spin(talker)

    #destruccion
    talker.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
