from backend import *
from calculatePow import CalculatePower

class AppController:
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

    def open_calculator(self):
        Calculator.launchPower(self.root)
    
    def open_calcuWork(self):
        Calculator.launchWork(self.root)
    
    def open_calcuTime(self):
        Calculator.launchTime(self.root)
    
    def back_calcuDash(self):
        Calculator.back(self.root)

    def start_flashCard(self):
        FlashCards.launch(self.root)
    