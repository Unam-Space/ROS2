import rclpy
from rclpy.node import Node
import random
import time

from std_msgs.msg import Int64




#Clase la cual se utilizara para obtener los datos de la velocidad
class ListenerNode(Node):
    
    def __init__(self):
        super().__init__("listener")
        self.subscription = self.create_subscription(Int64, 'velocidad_rover', self.listener_callback, 10)
        self.posicionx:int = 0
        self.posiciony:int = 0
        self.direccion:int = 2
        self.regreso:list = [(self.posicionx,self.posiciony,-1)]
        self.bandera_regreso:bool = False

    
    
    #Funcion que se ejecutara cada que reciva el mensaje de la velocidad
    def listener_callback(self, msg:Int64) -> None:
        
        if msg.data == 1 and not self.bandera_regreso:
            self.movimiento_automo(matriz_prueba)
        
        elif not self.regreso_activado:
            self.bandera_regreso = True
            self.regresar()
            rclpy.shutdown()

    #Funcion que ejecuta la ahuristica
    #direcciones posibles:
    '''
    0 ->
    1 ^
    2 <-
    3 v
    '''
    def movimiento_automo(self, m:list) -> None:


        #Si la direccion es hacia la derecha
        if self.direccion  == 0:
            #Si hay obstaculo, dar giro
            if self.hay_obstaculo(self.posicionx+1 , self.posiciony):
                self.dar_giro()
            #De otra manera avanzar
            else:
                self.posicionx  += 1
                matriz_prueba[self.posiciony][self.posicionx] = 'P'
                
                
                
                
        #Si la direccion es hacia arriba
        elif self.direccion  == 1:
            
            #Si hay obstaculo, dar giro
            if self.hay_obstaculo(self.posicionx , self.posiciony-1):
                self.dar_giro()
            #De otra manera avanzar
            else:
                self.posiciony  -= 1
                matriz_prueba[self.posiciony][self.posicionx] = 'P'
                
                
                
                
        #Si la direccion es hacia la izquierda
        elif self.direccion  == 2:
            
            #Si hay obstaculo, dar giro
            if self.hay_obstaculo(self.posicionx-1 , self.posiciony):
                self.dar_giro()
            #De otra manera avanzar
            else:
                self.posicionx  -= 1
                matriz_prueba[self.posiciony][self.posicionx] = 'P'
                
                
                
        #Si la direccion es hacia abajo
        elif self.direccion  == 3:
            
            #Si hay obstaculo, dar giro
            if self.hay_obstaculo(self.posicionx , self.posiciony+1):
                self.dar_giro()
            #De otra manera avanzar
            else:
                self.posiciony  += 1
                matriz_prueba[self.posiciony][self.posicionx] = 'P'
        
        
        #Nuevo nodo por donde se tendra que regresar
        nuevo_nodo = tuple([self.posicionx,self.posiciony])
        #En caso de que se pudiera avanzar agregamos el nuevo nodo
        if len(self.regreso) > 0 and self.regreso[-1] != nuevo_nodo:
            self.regreso.append(nuevo_nodo)
        
        
        self.imprimir_matriz()
        
        
        
        
        
    #Cambiar esto cuando podamos reconocer de alguna manera el obstaxulo en frente del rover
    #Funcion que identifica si hay un obstaculo en frente del robot
    def hay_obstaculo(self, siguiente_pasox:int,siguiente_pasoy:int) -> bool:
        maximoy = len(matriz_prueba)
        maximox = len(matriz_prueba[0])
        
        #Validamos que no se salga de la matriz y que no sea obstaculo marcado
        if siguiente_pasox >= maximox or siguiente_pasoy >= maximoy or siguiente_pasox < 0 or siguiente_pasoy < 0 or matriz_prueba[siguiente_pasoy][siguiente_pasox] == 5:
            return True
    
        return False
    
    
    
    
    def regresar(self) -> None:
        
        print('=================================')
        print('=================================')
        print(self.regreso)
        print('=================================')
        print('=================================')


    
    def dar_giro(self):
        direcciones = [-1, 1]
        giro = direcciones[random.randint(0,12)%2]
        
        if self.direccion == 0 and giro == -1:
            self.direccion = 3
        else:
            self.direccion =  (self.direccion + giro)%4



    def imprimir_matriz(self):
        print('==========================================')
        for x in range(len(matriz_prueba)):
            for y in range(len(matriz_prueba[0])):
                print(matriz_prueba[x][y], end = '  ')
            print()
        print('==========================================')



#Funcion main que ejecutara el movimento autonomo
def main(args = None):
    
    rclpy.init(args= args)
    listener = ListenerNode()



    #Matriz para prueba
    #2 es el home
    #0 terreno posible
    #5 obstaculo
    #1 espacio por donde ya se paso
    global  matriz_prueba
    matriz_prueba  = [[2,0,0,0,0,0,5,0,0,0,0,0,0,0],
                      [0,0,0,0,5,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,5,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    
    rclpy.spin(listener)
    

    #uso 
    #rclpy.spin_once(listener)
    #destruccion 
    listener.destroy_node()
    rclpy.shutdown()





if __name__ == '__main__':
    main()
    
    '''
    colcon build

    source ./install/setup.bash

    ros2 run rover_gui GUINode

    '''