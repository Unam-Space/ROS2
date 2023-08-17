import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64

'''
colcon build

source ./install/setup.bash

ros2 run rover_gui GUINode

'''


#Clase la cual se utilizara para obtener los datos de la velocidad
class ListenerNode(Node):
    def __init__(self):
        super().__init__("listener")
        self.subscription = self.create_subscription(
            Float64, 'velocidad_rover', self.listener_callback, 10
        )
    def listener_callback(self, msg):
        self.get_logger().info(f'Recivido {msg.data}')




def movimiento_automo(listener:ListenerNode, m:list):
    rclpy.spin_once(listener)





#Funcion main que ejecutara el movimento autonomo
def main(args = None):
    
    rclpy.init(args= args)
    listener = ListenerNode()


    matriz_prueba  = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    
    movimiento_automo(listener, matriz_prueba)

    #uso 
    #rclpy.spin_once(listener)
    #destruccion 
    listener.destroy_node()
    rclpy.shutdown()





if __name__ == '__main__':
    main()