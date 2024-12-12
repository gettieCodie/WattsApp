from backend_work import *

class AppControllerWork:
    def __init__(self, root):
        self.root = root
    
    def open_problemSet(self):
        Problem_Set_Work.launch(self.root)
    
    def open_masterDash(self):
        Master_Dashboard_Work.launch(self.root)
    
    def back_masterDash(self):
        Master_Dashboard_Work.back(self.root)

    def open_studyDash(self):
        print("Work Study Dashboard opened.")
        Study_Dashboard_Work.launch(self.root)

    def back_studyDash(self):
        Study_Dashboard_Work.back(self.root)

    def open_calculator(self):
        Calculator_Work.launchWork(self.root)
    
    def back_calcuDash(self):
        Calculator_Work.back(self.root)

    def open_calcuDash(self):
        Calculator_Work.launch(self.root)

    def start_flashCard(self):
        FlashCards_Work.launch(self.root)
    