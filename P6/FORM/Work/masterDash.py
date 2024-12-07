from tkinter import *
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
model_dir = os.path.join(current_dir, "../../MODEL/Work")
sys.path.append(os.path.normpath(model_dir))

from controller import AppController


class MasterDashboard():
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
            self.bg = PhotoImage(file="trace/MASTER.png")
            self.bg = PhotoImage(file="UTILITY/BGhalf.png")
            self.tab = PhotoImage(file="UTILITY/tab.png")
            self.greeting = PhotoImage(file="AssetsEnergy/greeting.png")
            self.tagline = PhotoImage(file="AssetsEnergy/tagline.png")
            self.know = PhotoImage(file="AssetsEnergy/kmPower.png")
            self.study = PhotoImage(file="AssetsEnergy/study.png")
            self.masterSelected = PhotoImage(file="AssetsEnergy/masterS.png")
            self.calcu = PhotoImage(file="AssetsEnergy/calcu.png")
            self.flashDef = PhotoImage(file="AssetsEnergy/def.png")
            self.flash_hover = PhotoImage(file="AssetsEnergy/hover.png")

            # Create images on the canvas
            self.canvas_image = self.canvas.create_image(0, 0, anchor=NW, image=self.bg)
            self.tabID = self.canvas.create_image(52, 35, anchor=NW, image=self.tab)
            self.greetingID = self.canvas.create_image(414, 66, anchor=NW, image=self.greeting)
            self.taglineID = self.canvas.create_image(332, 67, anchor=NW, image=self.tagline)
            self.knowID = self.canvas.create_image(414, 502, anchor=NW, image=self.know)
            
        except Exception as e:
            print(f"Error loading image: {e}")

        # Configure the scroll region to match the image height
        self.canvas.config(scrollregion=self.canvas.bbox(ALL))

        # Create buttons
        studyButton = Button(
            root, image=self.study,
            borderwidth=0,
            background="#f4f4f7",
            activebackground="#f4f4f7",
            cursor="hand2",
            command= self.controller.open_studyDash
        )
        self.canvas.create_window(414, 556, anchor=NW, window=studyButton)

        masterButton = Button(
            root, image=self.masterSelected,
            borderwidth=0,
            background="#f4f4f7",
            activebackground="#f4f4f7",
            cursor="hand2",
        )
        self.masterButton_window = self.canvas.create_window(750, 556, anchor=NW, window=masterButton)

        calcuButton = Button(
            root, image=self.calcu,
            borderwidth=0,
            background="#f4f4f7",
            activebackground="#f4f4f7",
            cursor="hand2",
            command=self.controller.open_calculator
        )
        self.canvas.create_window(1085, 556, anchor=NW, window=calcuButton)

        flashDefButton = Button(
            root, image=self.flashDef,
            borderwidth=0,
            background="#f4f4f7",
            activebackground="#f4f4f7",
            cursor="hand2",
            command=self.controller.start_flashCard
        )

        # Bind hover effects to masterButton
        flashDefButton.bind("<Enter>", lambda event: self.on_enter(event, flashDefButton, self.flash_hover))
        flashDefButton.bind("<Leave>", lambda event: self.on_leave(event, flashDefButton, self.flashDef))

        self.flashDefButton_window = self.canvas.create_window(710, 868, anchor=NW, window=flashDefButton)

def win():
    root = Tk()
    MasterDashboard(root)
    root.mainloop()

if __name__ == "__main__":
    win()
