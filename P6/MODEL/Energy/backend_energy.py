import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(current_dir, "Energy"))


class Problem_Set_Energy:
    @staticmethod
    def launch(root):
        from probSetE import ProblemSet
        for widget in root.winfo_children():
            widget.pack_forget()
        ProblemSet(root)

class Master_Dashboard_Energy:
    @staticmethod
    def launch(root):
        from masterDasheE import MasterDashboard
        for widget in root.winfo_children():
            widget.pack_forget()
        MasterDashboard(root)
    
    def back(root):
        from masterDashE import MasterDashboard
        for widget in root.winfo_children():
            widget.pack_forget()
        MasterDashboard(root)

class Calculator_Energy:
    @staticmethod
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
    
    def launch(root):
        from calcuDashE import CalcuDashboard
        for widget in root.winfo_children():
            widget.pack_forget()
        CalcuDashboard(root)

    def back(root):
        from calcuDashE import CalcuDashboard
        for widget in root.winfo_children():
            widget.pack_forget()
        CalcuDashboard(root)

class Study_Dashboard_Energy: 
    @staticmethod
    def back(root):
        from studyViewE import EnergyStudyDashboard
        for widget in root.winfo_children():
            widget.pack_forget()
        EnergyStudyDashboard(root)
    
    def launch(root):
        from studyViewE import EnergyStudyDashboard
        print("Energy Study Dashboard opened.")
        for widget in root.winfo_children():
            widget.pack_forget()
        EnergyStudyDashboard(root)

class FlashCards_Energy:
    @staticmethod
    def launch(root):
        from masterFlashE import FlashDash
        for widget in root.winfo_children():
            widget.pack_forget()
        FlashDash(root)
