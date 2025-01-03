import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(current_dir, "Energy"))
from tkinter import messagebox

class CalculatePotentialEnergy:
    def __init__(self, root, result_label):
        self.root = root
        self.result_label = result_label
    
    def calculate(self, height, mass):
        try:
            height = float(height.get())
            mass = float(mass.get())

            PE = mass  * 9.8 * height
            self.result_label.config(text=f"{PE:.2f} J")  # Update result label
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter numeric values for mass and height.")


class CalculateKineticEnergy:
    def __init__(self, root, result_label):
        self.root = root
        self.result_label = result_label 
    
    def calculate(self, mass, velocity):
        try:
            mass = float(mass.get())
            velocity = float(velocity.get())
            KE =  0.5 * mass * velocity ** 2
            self.result_label.config(text=f"{KE:.2f} J")  # Update result label
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter numeric values for mass and velocity.")
