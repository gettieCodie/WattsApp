import math
from tkinter import messagebox

class Calculate_Work:
    def __init__(self, root, result_label):
        self.root = root
        self.result_label = result_label

    def calculate(self, angle_entry, force_entry, distance_entry):
        try:
            force = float(force_entry.get())
            distance = float(distance_entry.get())
            angle_input = angle_entry.get().strip()

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
