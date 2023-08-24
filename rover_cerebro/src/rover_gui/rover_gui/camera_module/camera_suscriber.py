
"""
Librerias necesarias para trabajar con imagenes
"""
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import rclpy
from rclpy.node import Node

from std_msgs.msg import String


#Puente necesario para la comunicacion entre ROS y OpenCV




class CameraListenerNode(Node):
    
    def __init__(self):

        #Constuctor del nod
        super().__init__("Camera_listener")
        self.subscription = self.create_subscription(
            Image, 'image_topic', self.listener_callback, 10
        )

        #Parametro necesario  para el envio de imagenes
        self.bridge = CvBridge()




    def listener_callback(self, msg):
        try:
            #Conversion de mensje de ROS a Cv2 para la visualizacion
            camera_frame = self.bridge.imgmsg_to_cv2(msg, "bgr8")
            
        except CvBridgeError:
            print("Error")

        #Funciones para la visualizacion de frame por frame
        cv2.imshow("camera", camera_frame)
        cv2.waitKey(1)





def main(args = None):
    rclpy.init(args= args)

    #creacion 
    listener = CameraListenerNode()

    #uso 
    rclpy.spin(listener)

    #destruccion 
    listener.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()


    