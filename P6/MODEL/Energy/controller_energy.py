from backend_energy import *

class AppControllerEnergy:
    def __init__(self, root):
        self.root = root
    
    def open_problemSet(self):
        Problem_Set_Energy.launch(self.root)
    
    def open_masterDash(self):
        Master_Dashboard_Energy.launch(self.root)
    
    def back_masterDash(self):
        Master_Dashboard_Energy.back(self.root)

    def open_studyDash(self):
        Study_Dashboard_Energy.launch(self.root)

    def back_studyDash(self):
        Study_Dashboard_Energy.back(self.root)

    def open_calculatorKE(self):
        Calculator_Energy.launchKE(self.root)
    
    def open_calculatorPE(self):
        Calculator_Energy.launchPE(self.root)
    
    def back_calcuDash(self):
        Calculator_Energy.back(self.root)
    
    def open_calcuDash(self):
        Calculator_Energy.launch(self.root)

    def start_flashCard(self):
        FlashCards_Energy.launch(self.root)
    