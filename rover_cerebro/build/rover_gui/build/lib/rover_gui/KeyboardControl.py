#!/usr/bin/env python3
import Component

class Key():
    def Action(event):
        key = event.keysym
        if(key == "W" or key == "w" or key == "Up"):
            print("W")
        elif(key == "A" or key == "a" or key == "Left"):
            print("A")
        elif(key == "S" or key == "s" or key == "Right"):
            print("S")
        elif(key == "D" or key == "d" or key == "Down"): 
            print("D")
    
