#!/usr/bin/env python3
from pickle import FRAME
from PIL import ImageTk, Image, ImageShow
import PIL.Image
from tkinter import *
import tkinter 
import customtkinter #Biblioteca de prueba

import Gadgets
import Component

class Panel():
    def FrameControl(mainWindow): #Quitar scaleNumber cuando sea posible
        windowWidth = mainWindow.winfo_width()
        windowHeight = mainWindow.winfo_height()

        global originalSizeWindow
        originalSizeWindow = str(windowWidth) + "x" + str(windowHeight)
        print("OriginalSize: " + originalSizeWindow)
        #Creates arrays with the width and height value of the panels
        frameWdth = windowWidth * (1/6), windowWidth * (4/6), windowWidth * (1/6) - 30, windowWidth     #x Size of frames
        frameHght = windowHeight * (4/6), windowHeight * (2/6) - 30, 0, windowHeight                    #y Size of frames

        return frameWdth, frameHght

    def SetFrames(mainWindow, frameWdth, frameHght):
        frameQuantity = 5

        nFrame = [Frame] * (frameQuantity) #Set dimensions of each frame (!)
        nFrame[0] = Frame(mainWindow, width = frameWdth[0], height = frameWdth[3], bg = "#181E36", bd = 1, relief = FLAT)
        nFrame[1] = Frame(mainWindow, width = frameWdth[1], height = frameHght[0], bg = "#252A40", bd = 1, relief = FLAT)
        nFrame[2] = Frame(mainWindow, width = frameWdth[2], height = frameHght[0], bg = "#252A40", bd = 1, relief = FLAT)
        nFrame[3] = Frame(mainWindow, width = frameWdth[1], height = frameHght[1], bg = "#252A40", bd = 1, relief = FLAT)
        nFrame[4] = Frame(mainWindow, width = frameWdth[2], height = frameHght[1], bg = "#252A40", bd = 1, relief = FLAT)
        
        nFrame[0].place(x = 0, y = 0) #Places frames 
        nFrame[1].place(x = frameWdth[0] + 10, y = 10) ; nFrame[2].place(x = frameWdth[0] + frameWdth[1] + 20, y = 10)
        nFrame[3].place(x = frameWdth[0] + 10, y = frameHght[0] + 20) ; nFrame[4].place(x = frameWdth[0] + frameWdth[1] + 20, y = frameHght[0] + 20)    

class Utilities():
    def SetImage(mainWindow, frameWdth, frameHght):
        global UNAMSpaceLogo

        logoSize = int(frameWdth[0] - 40)
        imgOffset = (frameWdth[0] - int(logoSize))/2 #Space used to center the logo in the first panel

        UNAMSpaceLogo = ImageTk.PhotoImage(PIL.Image.open("Images/US-White.png").resize((logoSize,logoSize)))
        labelLogo = tkinter.Label(mainWindow, bg = "#181E36", image = UNAMSpaceLogo, width = logoSize , height = logoSize)
        labelLogo.place(x = imgOffset, y = imgOffset)

    def AutoAdjust(mainWindow): #This is a listener that tells you if the window has changed size
        global originalSizeWindow
        windowWidth = mainWindow.winfo_width()
        windowHeight = mainWindow.winfo_height()
        
        currentWindowSize = str(windowWidth) + "x" + str(windowHeight)

        if(currentWindowSize != originalSizeWindow):
            print("Dimension de la ventana cambió!")

            for widgets in mainWindow.winfo_children(): #Destroys all panels to build new
                widgets.destroy()

            frameWdth = windowWidth * (1/6), windowWidth * (4/6), windowWidth * (1/6) - 30, windowWidth     #x Size of frames
            frameHght = windowHeight * (4/6), windowHeight * (2/6) - 30, 0, windowHeight                    #y Size of frames

            #(!) Esto debería correr en main, no aquí (Hacer main una clase tambien)
            Panel.SetFrames(mainWindow, frameWdth, frameHght)
            Utilities.SetImage(mainWindow, frameWdth, frameHght)
            Gadgets.Animations.Battery(mainWindow, frameWdth, frameHght, 1, 100) #(!)
            Component.Btn.RosListener(mainWindow, frameWdth[0] + 200, frameHght[1] / 2)

            originalSizeWindow = currentWindowSize

        mainWindow.after(10, lambda : Utilities.AutoAdjust(mainWindow))

        #print("Window Dimension is: " + str(windowHeight) + "x" + str(windowWidth))


        

#Width == ancho && Height == Altura

