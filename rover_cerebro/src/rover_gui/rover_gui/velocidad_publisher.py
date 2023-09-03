import rclpy
from rclpy.node import Node
import time
import numpy as np

from random import randint
from std_msgs.msg import Int64


'''
import time
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
'''

class TalkerNode(Node):
    
    def __init__(self):


        #Creacion del nodo standard en ros
        super().__init__("talker")

        self.publisher_ = self.create_publisher(Int64, 'velocidad_rover', 10)
        time_period = 0.01  #Estrictamente necesario si queremos que la medida del tiempo sea precisa
        self.timer = self.create_timer(time_period, self.time_callback)
        self.velocidad = 47 #Cambiar esto
        self.tiempo_inicio = time.time()


    #Funcion que llamara al algoritmo
    #Para fines del espozo se tendra la velocidad fija, pero se espera que esta se obtenga de los datos del rover
    #igualmente 
    def time_callback(self):
        
        if np.floor((self.tiempo_inicio - time.time())* self.velocidad )%47 == 0:
            
            self.tiempo_inicio = time.time()
            msg = Int64()
            
            '''
            Temporal, en esta parte se debe de ejecutar la orden del regreso
            '''
            regresar:bool = (11 == randint(0,20))
            
            
            if regresar:
                #Mensaje para regresar
                msg.data = 2
            else:
                #Menesaje para continuar 
                msg.data = 1
                
            self.publisher_.publish(msg)
            



###Funcion main para que se llame desde el setup
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