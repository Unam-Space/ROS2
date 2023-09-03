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
        self.regreso:list = [(self.posicionx,self.posiciony)]
        self.bandera_regreso:bool = False
        self.regreso_activado:bool = False

    
    
    #Funcion que se ejecutara cada que reciva el mensaje de la velocidad
    def listener_callback(self, msg:Int64) -> None:
        
        if msg.data == 1 and not self.bandera_regreso:
            self.movimiento_automo(matriz_prueba)
        
        elif not self.regreso_activado:
            self.bandera_regreso = True
            self.regresar()
            rclpy.shutdown()







    #direcciones posibles:
    '''
    0 ->
    1 ^
    2 <-
    3 v
    '''
    def movimiento_automo(self, m:list) -> None:
        """Funcion que ejecuta la ehuristica

        Args:
            m (list): temoporal para pruebas
        """        


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
        
            print(self.direccion)
            self.imprimir_matriz()
        
        
        
        
        
        
        
        
    #Cambiar esto cuando podamos reconocer de alguna manera el obstaxulo en frente del rover
    def hay_obstaculo(self, siguiente_pasox:int,siguiente_pasoy:int) -> bool:
        """Funcion que verifica si hay un obstaculo en el siguiente paso posible del rover

        Args:
            siguiente_pasox (int): siguiente cordenada en x 
            siguiente_pasoy (int):  siguiente cordenada en y

        Returns:
            bool: Si es que se encuentra obstaculo
        """        
        maximoy = len(matriz_prueba)
        maximox = len(matriz_prueba[0])
        
        #Validamos que no se salga de la matriz y que no sea obstaculo marcado
        if siguiente_pasox >= maximox or siguiente_pasoy >= maximoy or siguiente_pasox < 0 or siguiente_pasoy < 0 or matriz_prueba[siguiente_pasoy][siguiente_pasox] == 5:
            return True
    
        return False



    
    
    
    def dar_giro(self, cambio_direccion:int = None):
        """Funcion que cambia la direccion del rover 

        Args:
            cambio_direccion (int, optional): En caso de el regreso e ir cambiando de direccion automaticamente. Defaults to None.
        """        
        
        if cambio_direccion is None:
            direcciones = [-1, 1]
            giro = direcciones[random.randint(0,12)%2]
            
            if self.direccion == 0 and giro == -1:
                self.direccion = 3
            else:
                self.direccion =  (self.direccion + giro)%4
        
        else:
            self.direccion = cambio_direccion    
            
            




    def regresar(self) -> None:
        """Funcion que hace el regreso por medio del camino guardado 
        """        
        
        
        
 
        #Se invierte el arreglo para operar mas facil con el:
        self.regreso = self.regreso[::-1]
        
        #CMABIAR CUANDO SE TENGA EL ROVER
        #Vuelta de 180 grados
        self.direccion = (self.direccion + 2) % 4
        
    
    
        for nodo in range(len(self.regreso)-1):
            
            #Se calcula hacia donde fue el movimento
            movimentox = self.regreso[nodo+1][0] - self.regreso[nodo][0]
            movimentoy = self.regreso[nodo+1][1] - self.regreso[nodo][1]

            #Se modifica la posicion del ROver
            self.posicionx += movimentox
            self.posiciony += movimentoy
            
            
            #Cambio de la direccion para el movimiento del rover
            if movimentox == 1:  self.dar_giro(cambio_direccion= 0)
            elif movimentox == -1: self.dar_giro(cambio_direccion= 2)
            elif movimentoy == 1: self.dar_giro(cambio_direccion= 3)
            elif movimentoy == -1: self.dar_giro(cambio_direccion= 1)
            
            
            
            #ELIMINAR 
            matriz_prueba[self.posiciony][self.posicionx] = 'R'
            self.imprimir_matriz()





    ##Borrar esto cuando se implemente en el verdadero rover
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