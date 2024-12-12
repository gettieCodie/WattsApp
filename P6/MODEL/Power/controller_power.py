from backend_power import *

class AppControllerPower:
    def __init__(self, root):
        self.root = root
    
    def open_problemSet(self):
        Problem_Set_Power.launch(self.root)
    
    def open_masterDash(self):
        Master_Dashboard_Power.launch(self.root)
    
    def back_masterDash(self):
        Master_Dashboard_Power.back(self.root)

    def open_studyDash(self):
        Study_Dashboard_Power.launch(self.root)

    def back_studyDash(self):
        Study_Dashboard_Power.back(self.root)

    def open_calculator(self):
        Calculator_Power.launchPower(self.root)
    
    def open_calcuWork(self):
        Calculator_Power.launchWork(self.root)
    
    def open_calcuTime(self):
        Calculator_Power.launchTime(self.root)
    
    def open_calcuKE(self):
        Calculator_Power.launchKE(self.root)
    
    def open_calcuPE(self):
        Calculator_Power.launchPE(self.root)
    
    def back_calcuDash(self):
        Calculator_Power.back(self.root)

    def start_flashCard(self):
        FlashCards_Power.launch(self.root)
    