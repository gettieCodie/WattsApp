import math
from tkinter import messagebox

class CalculateWork:
    def __init__(self, root, result_label):
        self.root = root
        self.result_label = result_label

    def calculate(self, angle, force, distance):
        try:
            force = float(force.get())
            distance = float(distance.get())
            angle_input = angle.get().strip()

            if angle_input == "":
                angle = 0.0
            else:
                angle = float(angle_input)

            if angle < 0:
                messagebox.showerror("Invalid Input", "Angle cannot be negative.")
                return

            angle_rad = math.radians(angle)
            work = force * distance * math.cos(angle_rad)
            self.result_label.config(text=f"{work:.2f} J")
        
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter numeric values for angle, force, or distance.")
