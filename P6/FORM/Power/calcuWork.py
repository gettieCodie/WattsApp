from tkinter import *
import tkinter as tk
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
model_dir = os.path.join(current_dir, "../../MODEL/Power")
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
            self.title = PhotoImage(file="Cpower/what.png")
            self.power = PhotoImage(file="Cpower/powerNS.png")
            self.workSel = PhotoImage(file="Cpower/workS.png")
            self.time = PhotoImage(file="Cpower/time1.png")
            self.solveTable = PhotoImage(file="Cpower/solveTable.png")
            self.powerTXT = PhotoImage(file="Cpower/powerTXT.png")
            self.timeTXT = PhotoImage(file="Cpower/timeTXT.png")
            self.powerINPUT = PhotoImage(file="Cpower/powerINPUT.png")
            self.timeINPUT = PhotoImage(file="Cpower/timeINPUT.png")
            self.resultWORK = PhotoImage(file="Cpower/resultWORK.png")
            self.calculate = PhotoImage(file="Cpower/calculate.png")
            self.reset = PhotoImage(file="Cpower/reset.png")

            # Create images on the canvas
            self.canvas_image = self.canvas.create_image(0, 0, anchor=NW, image=self.bg)
            self.titleID = self.canvas.create_image(473, 90, anchor = NW, image = self.title)
            self.solvetableID = self.canvas.create_image(139, 580, anchor=NW, image=self.solveTable)
            self.timeID = self.canvas.create_image(250,651, anchor=NW, image=self.timeTXT)
            self.powerID = self.canvas.create_image(250,725, anchor=NW, image=self.powerTXT)
            self.powerInputID = self.canvas.create_image(435, 716, anchor=NW, image=self.powerINPUT)
            self.timeInputID = self.canvas.create_image(435, 645, anchor=NW, image=self.timeINPUT)
            self.resultWorkID = self.canvas.create_image(970, 610, anchor=NW, image=self.resultWORK)

            # Create Entry widgets to accept user input
            self.powerEntry = tk.Entry(self.root, font=("Arial", 14), bd=0, highlightthickness=0,width=15)
            self.timeEntry = tk.Entry(self.root, font=("Arial", 14), bd=0, highlightthickness=0,width=15)
            self.resultLabel = Label(self.root, font=("Arial", 27), bg="#fff6de", text="")

            # Place Entry widgets on the canvas where the images are
            self.powerEntry_window = self.canvas.create_window(455, 659, anchor=NW, window=self.powerEntry)
            self.timeEntry_window = self.canvas.create_window(455, 729, anchor=NW, window=self.timeEntry)
            self.resultLabel_window = self.canvas.create_window(1073, 765, anchor=NW, window=self.resultLabel)

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

            powerButton = Button(
                root, image=self.power,
                borderwidth=0,
                background="#f4f4f7",
                activebackground="#f4f4f7",
                cursor="hand2",
                command=self.controller.open_calculator
            )
            self.canvas.create_window(135, 158, anchor=NW, window=powerButton)

            calculateButton = Button(
                root, image=self.calculate,
                borderwidth=0,
                background="#ffffff",
                activebackground="#ffffff",
                cursor="hand2",
                command=lambda: self.calculator.calculate(self.powerEntry, self.timeEntry)
            )
            self.canvas.create_window(435, 800, anchor=NW, window=calculateButton)

            resetButton = Button(
                root, image=self.reset,
                borderwidth=0,
                background="#ffffff",
                activebackground="#ffffff",
                cursor="hand2",
                command=lambda: [
                    self.powerEntry.delete(0, tk.END),
                    self.timeEntry.delete(0, tk.END),
                    self.resultLabel.config(text="")
                ]
            )
            self.canvas.create_window(560, 800, anchor=NW, window=resetButton)

            workButton = Button(
                root, image=self.workSel,
                borderwidth=0,
                background="#f4f4f7",
                activebackground="#f4f4f7",
                cursor="hand2"
            )
            self.canvas.create_window(550, 162, anchor=NW, window=workButton)

            timeButton = Button(
                root, image=self.time,
                borderwidth=0,
                background="#f4f4f7",
                activebackground="#f4f4f7",
                cursor="hand2",
                command=self.controller.open_calcuTime
            )
            self.canvas.create_window(960, 162, anchor=NW, window=timeButton)

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
