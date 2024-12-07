from tkinter import *
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
model_dir = os.path.join(current_dir, "../../MODEL/Energy")
sys.path.append(os.path.normpath(model_dir))

from controller import AppController

class ProblemSet:
    def on_mousewheel(self, event):
        self.canvas.yview_scroll(-1 * (event.delta // 120), "units")  # Scroll by units
    
    def __init__(self, root):
        self.root = root
        self.root.geometry("1440x1024")
        self.root.title("Watt's App")

        self.controller = AppController(self.root)

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
            self.bg = PhotoImage(file="trace/BG.png")
            self.tab = PhotoImage(file="UTILITY/tab.png")
            self.prob1 = PhotoImage(file="AssetsEnergy/probset1.png")
            self.prob2 = PhotoImage(file="AssetsEnergy/probset2.png")
            self.back = PhotoImage(file="UTILITY/backDash.png")
            

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
            command=self.controller.back_studyDash
        )
        self.canvas.create_window(414, 35, anchor=NW, window=backButton)
        
def win():
    root = Tk()
    ProblemSet(root)
    root.mainloop()

if __name__ == "__main__":
    win()