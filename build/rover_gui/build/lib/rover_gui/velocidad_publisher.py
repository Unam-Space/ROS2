import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64

class TalkerNode(Node):
    
    def __init__(self):

        super().__init__("talker")

        self.publisher_ = self.create_publisher(Float64, 'velocidad_rover', 10)
        time_period = 0.5
        self.timer = self.create_timer(time_period, self.time_callback)
        self.count = 0


    def time_callback(self):
        msg = Float64()
        msg.data = 4.5

        self.publisher_.publish(msg)



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