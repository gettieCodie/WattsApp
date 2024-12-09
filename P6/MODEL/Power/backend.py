import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(current_dir, "Power"))
sys.path.insert(0, os.path.join(current_dir, "Energy"))
form_energy_dir = os.path.normpath(os.path.join(current_dir, "../../FORM/Energy"))
sys.path.insert(0, form_energy_dir)


class Problem_Set:
    @staticmethod
    def launch(root):
        from probSet import ProblemSet
        for widget in root.winfo_children():
            widget.pack_forget()
        ProblemSet(root)

class Master_Dashboard:
    @staticmethod
    def launch(root):
        from masterDash import MasterDashboard
        for widget in root.winfo_children():
            widget.pack_forget()
        MasterDashboard(root)
    
    def back(root):
        from masterDash import MasterDashboard
        for widget in root.winfo_children():
            widget.pack_forget()
        MasterDashboard(root)

class Calculator:
    @staticmethod
    def launchPower(root):
        from calcuPower import Power
        for widget in root.winfo_children():
            widget.pack_forget()
        Power(root)

    def launchWork(root):
        from calcuWork import Work
        for widget in root.winfo_children():
            widget.pack_forget()
        Work(root)
    
    def launchTime(root):
        from calcuTime import Time
        for widget in root.winfo_children():
            widget.pack_forget()
        Time(root)
    
    def launchKE(root):
        from calcuKE import KineticEnergy
        for widget in root.winfo_children():
            widget.pack_forget()
        KineticEnergy(root)
    
    def launchPE(root):
        from calcuPE import PotentialEnergy
        for widget in root.winfo_children():
            widget.pack_forget()
        PotentialEnergy(root)

    def back(root):
        from calcuDash import CalcuDashboard
        for widget in root.winfo_children():
            widget.pack_forget()
        CalcuDashboard(root)

class Study_Dashboard: 
    @staticmethod
    def back(root):
        from studyView import StudyDashboard
        for widget in root.winfo_children():
            widget.pack_forget()
        StudyDashboard(root)
    
    def launch(root):
        from studyView import StudyDashboard
        for widget in root.winfo_children():
            widget.pack_forget()
        StudyDashboard(root)

class FlashCards:
    @staticmethod
    def launch(root):
        from masterFlash import FlashDash
        for widget in root.winfo_children():
            widget.pack_forget()
        FlashDash(root)
