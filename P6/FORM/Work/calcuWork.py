from tkinter import *
import tkinter as tk
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
model_dir = os.path.join(current_dir, "../../MODEL/Work")
sys.path.append(os.path.normpath(model_dir))

from controller import AppController
from calculate import CalculateWork
from masterDash import MasterDashboard

class Work():
    def on_mousewheel(self, event):
        self.canvas.yview_scroll(-1 * (event.delta // 120), "units")  # Scroll by units

    def __init__(self, root):
        self.root = root
        self.root.geometry("1440x1024")
        self.root.title("Watt's App")

        self.controller = AppController(self.root)

        # Create a canvas
        self.canvas = Canvas(root, width=1440, height=1024)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Add a vertical scrollbar
        v_scroll = Scrollbar(root, orient=VERTICAL, command=self.canvas.yview)
        v_scroll.pack(side=RIGHT, fill=Y)
        self.canvas.configure(yscrollcommand=v_scroll.set)
        # Bind the mouse wheel to scroll vertically
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

        # Load images
        try:
            # Store image references as instance variables
            # self.bg = PhotoImage(file="trace/CalPower.png")
            self.bg = PhotoImage(file="UTILITY/BGhalf.png")
            self.back = PhotoImage(file="UTILITY/backDash.png")
            self.title = PhotoImage(file="AssetsWork/whattoCal.png")
            self.power = PhotoImage(file="AssetsWork/work.png")
            self.solveTable = PhotoImage(file="Cpower/solveTable.png")
            self.timeTXT = PhotoImage(file="AssetsWork/givenTxt.png")
            self.powerINPUT = PhotoImage(file="AssetsWork/angleInput.png")
            self.timeINPUT = PhotoImage(file="AssetsWork/forceInput.png")
            self.distanceINPUT = PhotoImage(file="AssetsWork/distance.png")
            self.resultWORK = PhotoImage(file="AssetsWork/result.png")
            self.calculate = PhotoImage(file="AssetsWork/calculate.png")
            self.reset = PhotoImage(file="AssetsWork/reset.png")

            # Create images on the canvas
            self.canvas_image = self.canvas.create_image(0, 0, anchor=NW, image=self.bg)
            self.titleID = self.canvas.create_image(473, 90, anchor = NW, image = self.title)
            self.solvetableID = self.canvas.create_image(139, 580, anchor=NW, image=self.solveTable)
            self.timeID = self.canvas.create_image(195,631, anchor=NW, image=self.timeTXT)
            self.powerInputID = self.canvas.create_image(430, 625, anchor=NW, image=self.powerINPUT)
            self.timeInputID = self.canvas.create_image(430, 700, anchor=NW, image=self.timeINPUT)
            self.distanceID = self.canvas.create_image(430, 775, anchor=NW, image=self.distanceINPUT)
            self.resultWorkID = self.canvas.create_image(970, 610, anchor=NW, image=self.resultWORK)

            # Create Entry widgets to accept user input
            self.angleEntry = tk.Entry(self.root, font=("Arial", 14), bd=0, highlightthickness=0,width=15)
            self.forceEntry = tk.Entry(self.root, font=("Arial", 14), bd=0, highlightthickness=0,width=15)
            self.distanceEntry = tk.Entry(self.root, font=("Arial", 14), bd=0, highlightthickness=0,width=15)
            
            self.resultLabel = Label(self.root, font=("Arial", 20), bg="#dee9ff", text="")

            # Place Entry widgets on the canvas where the images are
            self.angleEntry_window = self.canvas.create_window(455, 640, anchor=NW, window=self.angleEntry)
            self.forceEntry_window = self.canvas.create_window(455, 715, anchor=NW, window=self.forceEntry)
            self.distanceEntry_window = self.canvas.create_window(455, 790, anchor=NW, window=self.distanceEntry)
            self.resultLabel_window = self.canvas.create_window(1080, 760, anchor=NW, window=self.resultLabel)

            self.calculator = CalculateWork(self.root, self.resultLabel)

            #Buttons---------------------------------------
            backButton = Button(
                root, image=self.back,
                borderwidth=0,
                background="#f4f4f7",
                activebackground="#f4f4f7",
                cursor="hand2",
                command=self.controller.back_calcuDash
            )
            self.canvas.create_window(149, 70, anchor=NW, window=backButton)

            workButton = Button(
                root, image=self.power,
                borderwidth=0,
                background="#f4f4f7",
                activebackground="#f4f4f7",
                cursor="hand2",
                command=self.controller.open_calculator
            )
            self.canvas.create_window(550, 158, anchor=NW, window=workButton)

            calculateButton = Button(
                root, image=self.calculate,
                borderwidth=0,
                background="#ffffff",
                activebackground="#ffffff",
                cursor="hand2",
                command=lambda: self.calculator.calculate(self.angleEntry, self.forceEntry, self.distanceEntry)
            )
            self.canvas.create_window(435, 850, anchor=NW, window=calculateButton)

            resetButton = Button(
                root, image=self.reset,
                borderwidth=0,
                background="#ffffff",
                activebackground="#ffffff",
                cursor="hand2",
                command=lambda: [
                    self.angleEntry.delete(0, tk.END),
                    self.forceEntry.delete(0, tk.END),
                    self.distanceEntry.delete(0, tk.END),
                    self.resultLabel.config(text="")
                ]
            )
            self.canvas.create_window(560, 850, anchor=NW, window=resetButton)

        except Exception as e:
            print(f"Error loading image: {e}")

        # Configure the scroll region to match the image height
        self.canvas.config(scrollregion=self.canvas.bbox(ALL))

def win():
    root = Tk()
    Work(root)
    root.mainloop()

if __name__ == "__main__":
    win()
