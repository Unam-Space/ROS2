#!/usr/bin/env python3
import tkinter
from tkinter import *

class Animations():
    def Battery(mainWindow, frameWdth, frameHght, scaleNumber, percentage):
        #Set dimensions of the battery cells
        bSize = 125, 42 ; tipSize = 62.5, 25
        bSize = frameWdth[0] / 2, frameHght[0] / 14 ; tipSize = frameWdth[0] / 4, frameHght[0] / 22
        cellQuantity = 6

        #Scales dimension of battery cell
        bSize = [item * scaleNumber for item in bSize]
        tipSize = [item * scaleNumber for item in tipSize]

        #Location of the battery 
        xloc = 20 + frameWdth[0] + frameWdth[1] + ((frameWdth[2] - bSize[0])/2)
        yloc = 50

        #Stores space for the upcoming cells
        cell = [Frame] * cellQuantity

        #El código debe pasar por aqui una sola vez: Cuando se crea la interfaz
        for i in range(cellQuantity):
            if(i == 0): #cell[0] is the top of the battery
                cell[i] = Frame(mainWindow, width = tipSize[0], height = tipSize[1], bg = 'lime', bd = 2, relief = GROOVE)
                cell[i].place(x = xloc + bSize[0]/4, y = yloc + (bSize[1] - tipSize[1]))
            else:
                cell[i] = Frame(mainWindow, width = bSize[0], height = bSize[1], bg = 'lime', bd = 2, relief = GROOVE)
                cell[i].place(x = xloc, y = yloc + i * bSize[1])

        #Changes the animation of the battery (!)
        if(percentage >= 90): 
            pass
        elif(75 <= percentage < 90):
            pass
        elif(60 <= percentage < 75):
            pass
        elif(40 <= percentage < 60):
            pass
        elif(20 <= percentage < 40):
            pass
        elif(5 < percentage < 20):
            pass
        else:
            print("Battery is empty!")
            
        

