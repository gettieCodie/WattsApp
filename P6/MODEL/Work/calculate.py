import os
import sys
import math
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(current_dir, "Work"))
from tkinter import messagebox

class CalculateWork:
    def __init__(self, root, result_label):
        self.root = root
        self.result_label = result_label
    
    def calculate(self, angle, force, distance):
        try:
            angle = float(angle.get())
            force = float(force.get())
            distance = float(distance.get())
            
            if angle < 0:
                messagebox.showerror("Invalid Input", "Angle cannot be negative.")
                return
            
            angle_rad = math.radians(angle)

            if angle == 0:
                work = force * distance
            else:
                work = force * distance * math.cos(angle_rad)
            self.result_label.config(text=f"{work:.2f} J") 
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter numeric values for angle, force, and distance.")