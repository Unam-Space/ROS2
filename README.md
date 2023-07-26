# ROS2
Migracion y continuacion de desarrollo en ROS 2

El archivo el cual se debe ejecutar es:

> rover_cerebro/src/rover_gui/rover_gui/RoverGUI.py

Para la ejecucion en caso de no tener el source de ros ejecutar en la terminal:

> source /opt/ros/foxy/setup.bash

Para ejecutar el paquete con el archivo ejecutar las siguientes lineas donde se encuentre la carpeta src


> colcon build

> source ./install/setup.bash 

> ros2 run rover_gui GUINode


Para ejecutar el nodo talker ejecutar en otra terminal igaulmente donde se encuentre la carpeta src

> ros2 run rover_gui talkerNode



Hay un problema con la ruta de las imagenes, si se desea ejecutar cambiar a la ruta con tu nomre de ubuntu
