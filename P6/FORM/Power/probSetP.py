from tkinter import *
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
model_dir = os.path.join(current_dir, "../../MODEL/Power")
sys.path.append(os.path.normpath(model_dir))
form_dir = os.path.abspath(os.path.join(current_dir, '../../')) 
sys.path.append(form_dir)

from controller_power import AppControllerPower

class ProblemSet:
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
            self.bg = PhotoImage(file="trace/BG.png")
            self.tab = PhotoImage(file="UTILITY/tab.png")
            self.prob1 = PhotoImage(file="PROBSET/1.png")
            self.prob2 = PhotoImage(file="PROBSET/2.png")
            self.back = PhotoImage(file="UTILITY/backDash.png")
            self.powerTab = PhotoImage(file="UTILITY/powerS.png")
            self.energyTab = PhotoImage(file="UTILITY/energy.png")
            self.workTab = PhotoImage(file="UTILITY/work.png")
            self.powerHover = PhotoImage(file="UTILITY/powerS.png")
            self.energyHover = PhotoImage(file="UTILITY/energyS.png")
            self.workHover = PhotoImage(file="UTILITY/workS.png")

            # Create images on the canvas
            self.canvas_image = self.canvas.create_image(0, 0, anchor=NW, image=self.bg)
            self.tabID = self.canvas.create_image(52, 35, anchor=NW, image=self.tab)
            self.prob1ID = self.canvas.create_image(414, 140, anchor=NW, image=self.prob1)
            self.prob2ID = self.canvas.create_image(414, 910, anchor=NW, image=self.prob2)
            
        except Exception as e:
            print(f"Error loading image: {e}")

        # Configure the scroll region to match the image height
        self.canvas.config(scrollregion=self.canvas.bbox(ALL))
        
        backButton = Button(
            root, image=self.back,
            borderwidth=0,
            background="#f4f4f7",
            activebackground="#f4f4f7",
            cursor="hand2",
            command=self.Pcontroller.back_studyDash
        )
        self.canvas.create_window(414, 35, anchor=NW, window=backButton)
        
        powerButton = Button(
            root, image=self.powerTab,
            borderwidth=0,
            background="#ffffff",
            activebackground="#ffffff",
            cursor="hand2",
            command=self.launch_PowerStudyDash
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
            command=self.launch_EnergyStudyDash
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
            command=self.launch_WorkStudyDash
        )
        # Bind hover effects to masterButton
        workButton.bind("<Enter>", lambda event: self.on_enter(event, workButton, self.workHover))
        workButton.bind("<Leave>", lambda event: self.on_leave(event, workButton, self.workTab))
        self.workButton_window = self.canvas.create_window(90, 390, anchor=NW, window=workButton)

    def launch_PowerStudyDash(self):
        from FORM.Power.studyViewP import StudyDashboard
        from controller_power import AppControllerPower  # Ensure to use the Power controller
        self.Pcontroller = AppControllerPower(self.root)  # Switch to Power controller
        for widget in self.root.winfo_children():
            widget.pack_forget()
        StudyDashboard(self.root)

    def launch_EnergyStudyDash(self):
        from FORM.Energy.studyViewE import EnergyStudyDashboard
        from controller_energy import AppControllerEnergy  # Ensure to use the Energy controller
        self.Econtroller = AppControllerEnergy(self.root)  # Switch to Energy controller
        for widget in self.root.winfo_children():
            widget.pack_forget()
        EnergyStudyDashboard(self.root)
    
    def launch_WorkStudyDash(self):
        from FORM.Work.studyViewW import WorkStudyDashboard
        from controller_work import AppControllerWork  # Ensure to use the Work controller
        self.Wcontroller = AppControllerWork(self.root)  # Switch to Work controller
        for widget in self.root.winfo_children():
            widget.pack_forget()
        WorkStudyDashboard(self.root)


def win():
    root = Tk()
    ProblemSet(root)
    root.mainloop()

if __name__ == "__main__":
    win()
