from backend import *

class AppControllerEnergy:
    def __init__(self, root):
        self.root = root
    
    def open_problemSet(self):
        Problem_Set.launch(self.root)
    
    def open_masterDash(self):
        Master_Dashboard.launch(self.root)
    
    def back_masterDash(self):
        Master_Dashboard.back(self.root)

    def open_studyDash(self):
        Study_Dashboard.launch(self.root)

    def back_studyDash(self):
        Study_Dashboard.back(self.root)

    def open_calculatorKE(self):
        Calculator.launchKE(self.root)
    
    def open_calculatorPE(self):
        Calculator.launchPE(self.root)
    
    def back_calcuDash(self):
        Calculator.back(self.root)
    
    def open_calcuDash(self):
        Calculator.launch(self.root)

    def start_flashCard(self):
        FlashCards.launch(self.root)
    