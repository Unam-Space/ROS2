#!/usr/bin/env python3
from cProfile import label
from pprint import pp
from PIL import ImageTk, Image, ImageShow
from click import command
from std_msgs.msg import String
import PIL.Image
from tkinter import *
import tkinter 
import rospy
#Modulos
import Window
import Gadgets
import Component
import KeyboardControl

#I cannot figure out how to make this code work inside a module (KeyboardControl.py)
def KeyboardControl(event): #Perhaps a lambda function
    key = event.keysym
    if(key == "W" or key == "w" or key == "Up"):
        Component.Text.Char(mainWindow, 1700, 800, "W")
    elif(key == "A" or key == "a" or key == "Left"):
        Component.Text.Char(mainWindow, 1700, 800, "A")
    elif(key == "S" or key == "s" or key == "Right"):
        Component.Text.Char(mainWindow, 1700, 800, "S")
    elif(key == "D" or key == "d" or key == "Down"): 
        Component.Text.Char(mainWindow, 1700, 800, "D")

scaleNumber = 1
percentage = 100

print("Proceso iniciado")
global mainWindow
mainWindow = tkinter.Tk()

mainWindow.title("Interfaz Grafica Rover V1.7")
mainWindow.configure(bg = '#2E3349')
frameWdth = [0, 0, 0, 0] ; frameHght = [0, 0, 0, 0]

mainWindow.geometry(str(mainWindow.winfo_screenwidth()) + "x" + str(mainWindow.winfo_screenwidth()))
#Dimensiones de mi ventana: 1016x1852

def Execute():
    frameWdth, frameHght = Window.Panel.FrameControl(mainWindow)
    Window.Panel.SetFrames(mainWindow, frameWdth, frameHght)
    Window.Utilities.SetImage(mainWindow, frameWdth, frameHght)
    Gadgets.Animations.Battery(mainWindow, frameWdth, frameHght, scaleNumber, percentage) #(!)

    Component.Btn.RosListener(mainWindow, frameWdth[0] + 200, frameHght[1] / 2)

#(!) ROS needed
mainWindow.bind("<Key>", KeyboardControl) #Tracks the keyboard actions
mainWindow.after(40, lambda: Execute()) #Only executes one time
mainWindow.after(50, lambda:  Window.Utilities.AutoAdjust(mainWindow)) #Executes multiple times
mainWindow.mainloop()
print("Fin del proceso!")