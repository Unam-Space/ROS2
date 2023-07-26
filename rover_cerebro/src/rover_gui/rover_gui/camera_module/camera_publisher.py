
"""
Librerias necesarias para trabajar con imagenes
"""

from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class CameraTalkerNode(Node):
    
    def __init__(self):

        super().__init__("Camera_talker")

        #Constuctor del noto
        self.publisher_ = self.create_publisher(Image, 'image_topic', 0)
        
        #Mantener bajo este parametro para que el video se vea fluido
        time_period = 0.1
        self.timer = self.create_timer(time_period, self.time_callback)


        #Se toma la camara por defecto para la captura de imagenes
        #Cambar el numero si se quiere cambiar de camara
        self.camera_image = cv2.VideoCapture(0)
        #Puente para la conexion con ROS
        self.bridge = CvBridge()

        #Parametros de la camara
        self.camera_image.set(cv2.CAP_PROP_FRAME_WIDTH, 3000)
        self.camera_image.set(cv2.CAP_PROP_FRAME_HEIGHT, 3000)
        self.camera_image.set(cv2.CAP_PROP_FPS, 60)



    def time_callback(self):

        #Envio del frame capturado por la camara
        boolean, frame = self.camera_image.read() 
        msg = self.bridge.cv2_to_imgmsg(frame, "bgr8")
        self.publisher_.publish(msg)
        



def main(args = None) -> None:
    rclpy.init(args= args)

    #creacion 
    talker = CameraTalkerNode()

    #uso 
    rclpy.spin(talker)

    #destruccion 
    talker.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()