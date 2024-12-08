import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(current_dir, "Work"))


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
    def launchWork(root):
        from calcuWork import Work
        for widget in root.winfo_children():
            widget.pack_forget()
        Work(root)
    
    def launch(root):
        from calcuDash import CalcuDashboard
        for widget in root.winfo_children():
            widget.pack_forget()
        CalcuDashboard(root)

    def back(root):
        from calcuDash import CalcuDashboard
        for widget in root.winfo_children():
            widget.pack_forget()
        CalcuDashboard(root)

class Study_Dashboard: 
    @staticmethod
    def back(root):
        from studyView import WorkStudyDashboard
        for widget in root.winfo_children():
            widget.pack_forget()
        WorkStudyDashboard(root)
    
    def launch(root):
        from studyView import WorkStudyDashboard
        for widget in root.winfo_children():
            widget.pack_forget()
        WorkStudyDashboard(root)

class FlashCards:
    @staticmethod
    def launch(root):
        from masterFlash import FlashDash
        for widget in root.winfo_children():
            widget.pack_forget()
        FlashDash(root)
