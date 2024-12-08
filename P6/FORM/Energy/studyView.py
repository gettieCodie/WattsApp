import os
import sys
from tkinter import *

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.extend([
    os.path.join(current_dir, "../../MODEL/Power"),
    os.path.join(current_dir, "../../MODEL/Energy"),
    os.path.join(current_dir, "../../MODEL/Work")
])

from controller_power import AppControllerPower
from controller_energy import AppControllerEnergy
from controller_work import AppControllerWork


class EnergyStudyDashboard:
    def on_mousewheel(self, event):
        self.canvas.yview_scroll(-1 * (event.delta // 120), "units")  # Scroll by units


    def on_enter(self, event, button, hover_image):
        button.config(image=hover_image)

    def on_leave(self, event, button, original_image):
        button.config(image=original_image)

    def __init__(self, root):
        self.root = root
        self.root.geometry("1440x1024")
        self.root.title("Watt's App")

        self.Pcontroller = AppControllerPower(self.root)
        self.Econtroller = AppControllerEnergy(self.root)
        self.Wcontroller = AppControllerWork(self.root)

        # Create a canvas
        self.canvas = Canvas(root, width=1440, height=1024, bg = "#f4f4f7")
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
            self.studySelected = PhotoImage(file="AssetsEnergy/studyS.png")
            self.bg = PhotoImage(file="trace/BG.png")
            self.tab = PhotoImage(file="UTILITY/tab.png")
            self.greeting = PhotoImage(file="AssetsEnergy/greeting.png")
            self.tagline = PhotoImage(file="AssetsEnergy/tagline.png")
            self.know = PhotoImage(file="AssetsEnergy/kmPower.png")
            self.definitions = PhotoImage(file="AssetsEnergy/definitions.png")
            self.formula = PhotoImage(file="AssetsEnergy/formula.png")
            self.problem = PhotoImage(file="AssetsEnergy/probButton.png")
            self.master_img = PhotoImage(file="AssetsEnergy/master.png")
            self.calcu = PhotoImage(file="AssetsEnergy/calcu.png")
            self.powerTab = PhotoImage(file="UTILITY/powerr.png")
            self.energyTab = PhotoImage(file="UTILITY/energyS.png")
            self.workTab = PhotoImage(file="UTILITY/work.png")
            self.powerHover = PhotoImage(file="UTILITY/powerS.png")
            self.energyHover = PhotoImage(file="UTILITY/energyS.png")
            self.workHover = PhotoImage(file="UTILITY/workS.png")

            # Create images on the canvas
            self.canvas_image = self.canvas.create_image(0, 0, anchor=NW, image=self.bg)
            self.tabID = self.canvas.create_image(52, 35, anchor=NW, image=self.tab)
            self.greetingID = self.canvas.create_image(414, 66, anchor=NW, image=self.greeting)
            self.taglineID = self.canvas.create_image(332, 67, anchor=NW, image=self.tagline)
            self.knowID = self.canvas.create_image(414, 502, anchor=NW, image=self.know)
            self.definitionsID = self.canvas.create_image(414, 880, anchor=NW, image=self.definitions)
            self.formulaID = self.canvas.create_image(414, 1508, anchor=NW, image=self.formula)
            # self.problemID = self.canvas.create_image(1026, 1820, anchor=NW, image=self.problem)

        except Exception as e:
            print(f"Error loading image: {e}")

        # Configure the scroll region to match the image height
        self.canvas.config(scrollregion=self.canvas.bbox(ALL))

        # Create buttons
        studyButton = Button(
            root, image=self.studySelected,
            borderwidth=0,
            background="#f4f4f7",
            activebackground="#f4f4f7",
            cursor="hand2"
        )
        self.canvas.create_window(414, 556, anchor=NW, window=studyButton)

        masterButton = Button(
            root, image=self.master_img,
            borderwidth=0,
            background="#f4f4f7",
            activebackground="#f4f4f7",
            cursor="hand2",
            command=self.Econtroller.open_masterDash
        )
        self.canvas.create_window(750, 556, anchor=NW, window=masterButton)

        calcuButton = Button(
            root, image=self.calcu,
            borderwidth=0,
            background="#f4f4f7",
            activebackground="#f4f4f7",
            cursor="hand2",
            command=self.Econtroller.open_calculatorKE
        )
        self.canvas.create_window(1085, 556, anchor=NW, window=calcuButton)

        problemButton = Button(
            root, image=self.problem,
            borderwidth=0,
            background="#f4f4f7",
            activebackground="#f4f4f7",
            cursor="hand2",
            command=self.Econtroller.open_problemSet
        )
        self.canvas.create_window(1026, 1905, anchor=NW, window=problemButton)

        powerButton = Button(
            root, image=self.powerTab,
            borderwidth=0,
            background="#ffffff",
            activebackground="#ffffff",
            cursor="hand2",
            command=self.Econtroller.open_studyDash
        )
        # Bind hover effects to masterButton
        powerButton.bind("<Enter>", lambda event: self.on_enter(event, powerButton, self.powerHover))
        powerButton.bind("<Leave>", lambda event: self.on_leave(event, powerButton, self.powerTab))
        self.powerButton_window = self.canvas.create_window(90, 230, anchor=NW, window=powerButton)

        energyButton = Button(
            root, image=self.energyTab,
            borderwidth=0,
            background="#ffffff",
            activebackground="#ffffff",
            cursor="hand2",
            # command=self.controller.open_problemSet
        )
        # Bind hover effects to masterButton
        energyButton.bind("<Enter>", lambda event: self.on_enter(event, energyButton, self.energyHover))
        energyButton.bind("<Leave>", lambda event: self.on_leave(event, energyButton, self.energyTab))
        self.energyButton_window = self.canvas.create_window(90, 310, anchor=NW, window=energyButton)

        workButton = Button(
            root, image=self.workTab,
            borderwidth=0,
            background="#ffffff",
            activebackground="#ffffff",
            cursor="hand2",
            command=self.Wcontroller.open_studyDash
        )
        # Bind hover effects to masterButton
        workButton.bind("<Enter>", lambda event: self.on_enter(event, workButton, self.workHover))
        workButton.bind("<Leave>", lambda event: self.on_leave(event, workButton, self.workTab))
        self.workButton_window = self.canvas.create_window(90, 390, anchor=NW, window=workButton)


def win():
    root = Tk()
    EnergyStudyDashboard(root)
    root.mainloop()

if __name__ == "__main__":
    win()
