#!/usr/bin/env python3
from tkinter import *
import tkinter
import ROS

class Text():
    def Char(mainWindow, xloc, yloc, char): 
        charLabel = Label(mainWindow, text = char)
        charLabel.config(font = ('Helvetica bold', 50))
        charLabel.place(x = xloc, y = yloc)

    def Lbl(mainWindow, xloc, yloc, text):
        textLabel = Label(mainWindow, text = text)
        textLabel.config(font = ('Helvetica bold', 15))
        textLabel.place(x = xloc, y = yloc)

class Btn():
    def RosListener(mainWindow, xloc, yloc):
        listenerBtn = tkinter.Button(text = "Activar Listener", command = lambda : Action.Listen(mainWindow, xloc, yloc))
        listenerBtn.place(x = xloc, y = yloc)
    
    def ScreenSize(mainWindow, xloc, yloc):
        screenBtn = tkinter.Button(text = "Dimensiones ventana", command = lambda : Action.ReturnSize(mainWindow, xloc, yloc))
        screenBtn.place(x = xloc, y = yloc)

class Action():
    def Listen(mainWindow, xloc, yloc):
        data = ROS.Simple.listener()
        Text.Lbl(mainWindow, xloc + 200, yloc, data)
        print("Botón activado")
    
    def ReturnSize(mainWindow, xloc, yloc):
        screenWidth = mainWindow.winfo_screenwidth()
        screenHeight = mainWindow.winfo_screenheight()

        windowWidth = mainWindow.winfo_width()
        windowHeight = mainWindow.winfo_height()

        textDimension = "Window Dimension is: " + str(windowHeight) + "x" + str(windowWidth)
        print(textDimension)
        Text.Lbl(mainWindow, xloc + 200, yloc, textDimension)
