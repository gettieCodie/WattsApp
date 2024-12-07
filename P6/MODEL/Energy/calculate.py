import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(current_dir, "Energy"))
from tkinter import messagebox

class CalculatePower:
    def __init__(self, root, result_label):
        self.root = root
        self.result_label = result_label
    
    def calculate(self, work_entry, time_entry):
        try:
            work = float(work_entry.get())
            time = float(time_entry.get())
            if time == 0:
                raise ZeroDivisionError("Time cannot be zero.")
            power = work / time
            self.result_label.config(text=f"{power:.2f} W")  # Update result label
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter numeric values for Work and Time.")
        except ZeroDivisionError as e:
            messagebox.showerror("Error", str(e))

class CalculateWork:
    def __init__(self, root, result_label):
        self.root = root
        self.result_label = result_label 
    
    def calculate(self, power_entry, time_entry):
        try:
            power = float(power_entry.get())
            time = float(time_entry.get())
            work = power * time
            self.result_label.config(text=f"{work:.2f} J")  # Update result label
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
