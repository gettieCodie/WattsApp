import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(current_dir, "Power"))
sys.path.insert(0, os.path.join(current_dir, "Energy"))
sys.path.insert(0, os.path.join(current_dir, "Work"))
form_energy_dir = os.path.normpath(os.path.join(current_dir, "../../FORM/Energy"))
form_work_dir = os.path.normpath(os.path.join(current_dir, "../../FORM/Work"))
sys.path.insert(0, form_energy_dir)
sys.path.insert(0, form_work_dir)

class Problem_Set_Work:
    @staticmethod
    def launch(root):
        from probSetW import ProblemSet
        for widget in root.winfo_children():
            widget.pack_forget()
        ProblemSet(root)

class Master_Dashboard_Work:
    @staticmethod
    def launch(root):
        from masterDashW import MasterDashboard
        for widget in root.winfo_children():
            widget.pack_forget()
        MasterDashboard(root)
    
    def back(root):
        from masterDashW import MasterDashboard
        for widget in root.winfo_children():
            widget.pack_forget()
        MasterDashboard(root)

class Calculator_Work:
    @staticmethod
    def launchWork(root):
        from calcuWorkW import Work
        for widget in root.winfo_children():
            widget.pack_forget()
        Work(root)
    
    def launch(root):
        from calcuDashW import CalcuDashboard
        for widget in root.winfo_children():
            widget.pack_forget()
        CalcuDashboard(root)

    def back(root):
        from calcuDashW import CalcuDashboard
        for widget in root.winfo_children():
            widget.pack_forget()
        CalcuDashboard(root)

class Study_Dashboard_Work: 
    @staticmethod
    def back(root):
        from studyViewW import WorkStudyDashboard
        for widget in root.winfo_children():
            widget.pack_forget()
        WorkStudyDashboard(root)
    
    def launch(root):
        from studyViewW import WorkStudyDashboard
        for widget in root.winfo_children():
            widget.pack_forget()
        WorkStudyDashboard(root)

class FlashCards_Work:
    @staticmethod
    def launch(root):
        from masterFlashW import FlashDash
        for widget in root.winfo_children():
            widget.pack_forget()
        FlashDash(root)
