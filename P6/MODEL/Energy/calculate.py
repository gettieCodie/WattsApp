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
            
            PE = mass  * 9.81 * height
            self.result_label.config(text=f"{PE:.2f} J")  # Update result label
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter numeric values for Work and Time.")
        except ZeroDivisionError as e:
            messagebox.showerror("Error", str(e))

class CalculateKineticEnergy:
    def __init__(self, root, result_label):
        self.root = root
        self.result_label = result_label 
    
    def calculate(self, mass, velocity):
        try:
            mass = float(mass.get())
            velocity = float(velocity.get())
            KE = 0.5 * mass * (velocity**2)
            self.result_label.config(text=f"{KE:.2f} J")  # Update result label
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter numeric values for Power and Time.")

class CalculateTime:
    def __init__(self, root, result_label):
        self.root = root
        self.result_label = result_label
    
    def calculate(self, work_entry, power_entry):
        try:
            work = float(work_entry.get())
            power = float(power_entry.get())
            if power == 0:
                raise ZeroDivisionError("Power cannot be zero.")
            time = work / power
            self.result_label.config(text=f"{time:.2f} s")  # Update result label
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter numeric values for Work and Time.")
        except ZeroDivisionError as e:
            messagebox.showerror("Error", str(e))
