from tkinter import *
import tkinter as tk
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
model_dir = os.path.join(current_dir, "../../MODEL/Energy")
sys.path.append(os.path.normpath(model_dir))
form_dir = os.path.abspath(os.path.join(current_dir, '../../')) 
sys.path.append(form_dir)

from controller_energy import AppControllerEnergy
from calculate import CalculatePotentialEnergy
from masterDash import MasterDashboard

class PotentialEnergy():
    def on_mousewheel(self, event):
        self.canvas.yview_scroll(-1 * (event.delta // 120), "units")  # Scroll by units

    def __init__(self, root):
        self.root = root
        self.root.geometry("1440x1024")
        self.root.title("Watt's App")

        self.Econtroller = AppControllerEnergy(self.root)

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
            self.title = PhotoImage(file="AssetsEnergy/chooseCal.png")
            self.power = PhotoImage(file="AssetsEnergy/ke.png")
            self.workSel = PhotoImage(file="AssetsEnergy/peS.png")
            self.solveTable = PhotoImage(file="Cpower/solveTable.png")
            self.timeTXT = PhotoImage(file="AssetsEnergy/peGiven.png")
            self.powerINPUT = PhotoImage(file="AssetsEnergy/inputMass.png")
            self.timeINPUT = PhotoImage(file="AssetsEnergy/inputHeight.png")
            self.resultWORK = PhotoImage(file="AssetsEnergy/result.png")
            self.calculate = PhotoImage(file="AssetsEnergy/calculate.png")
            self.reset = PhotoImage(file="AssetsEnergy/reset.png")

            # Create images on the canvas
            self.canvas_image = self.canvas.create_image(0, 0, anchor=NW, image=self.bg)
            self.titleID = self.canvas.create_image(473, 90, anchor = NW, image = self.title)
            self.solvetableID = self.canvas.create_image(139, 580, anchor=NW, image=self.solveTable)
            self.timeID = self.canvas.create_image(235,651, anchor=NW, image=self.timeTXT)
            self.powerInputID = self.canvas.create_image(430, 712, anchor=NW, image=self.powerINPUT)
            self.timeInputID = self.canvas.create_image(430, 638, anchor=NW, image=self.timeINPUT)
            self.resultWorkID = self.canvas.create_image(970, 610, anchor=NW, image=self.resultWORK)

            # Create Entry widgets to accept user input
            self.heightEntry = tk.Entry(self.root, font=("Arial", 14), bd=0, highlightthickness=0,width=15)
            self.massEntry = tk.Entry(self.root, font=("Arial", 14), bd=0, highlightthickness=0,width=15)
            self.resultLabel = Label(self.root, font=("Arial", 20), bg="#e8f6e0", text="")

            # Place Entry widgets on the canvas where the images are
            self.heightEntry_window = self.canvas.create_window(455, 659, anchor=NW, window=self.heightEntry)
            self.massEntry_window = self.canvas.create_window(455, 729, anchor=NW, window=self.massEntry)
            self.resultLabel_window = self.canvas.create_window(1085, 760, anchor=NW, window=self.resultLabel)

            self.calculator = CalculatePotentialEnergy(self.root, self.resultLabel)

            #Buttons---------------------------------------
            backButton = Button(
                root, image=self.back,
                borderwidth=0,
                background="#f4f4f7",
                activebackground="#f4f4f7",
                cursor="hand2",
                command=self.Econtroller.back_calcuDash
            )
            self.canvas.create_window(149, 70, anchor=NW, window=backButton)

            calculateButton = Button(
                root, image=self.calculate,
                borderwidth=0,
                background="#ffffff",
                activebackground="#ffffff",
                cursor="hand2",
                command=lambda: self.calculator.calculate(self.heightEntry, self.massEntry)
            )
            self.canvas.create_window(435, 800, anchor=NW, window=calculateButton)

            resetButton = Button(
                root, image=self.reset,
                borderwidth=0,
                background="#ffffff",
                activebackground="#ffffff",
                cursor="hand2",
                command=lambda: [
                    self.heightEntry.delete(0, tk.END),
                    self.massEntry.delete(0, tk.END),
                    self.resultLabel.config(text="")
                ]
            )
            self.canvas.create_window(560, 800, anchor=NW, window=resetButton)

            keButton = Button(
                root, image=self.power,
                borderwidth=0,
                background="#f4f4f7",
                activebackground="#f4f4f7",
                cursor="hand2",
                command=self.Econtroller.open_calculatorKE
            )
            self.canvas.create_window(295, 158, anchor=NW, window=keButton)

            peButton = Button(
                root, image=self.workSel,
                borderwidth=0,
                background="#f4f4f7",
                activebackground="#f4f4f7",
                cursor="hand2",
                command=self.Econtroller.open_calculatorPE
            )
            self.canvas.create_window(760, 162, anchor=NW, window=peButton)

        except Exception as e:
            print(f"Error loading image: {e}")

        # Configure the scroll region to match the image height
        self.canvas.config(scrollregion=self.canvas.bbox(ALL))

def win():
    root = Tk()
    PotentialEnergy(root)
    root.mainloop()

if __name__ == "__main__":
    win()
