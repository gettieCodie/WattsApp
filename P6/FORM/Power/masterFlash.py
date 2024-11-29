from tkinter import *
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
model_dir = os.path.join(current_dir, "../../MODEL/Power")
sys.path.append(os.path.normpath(model_dir))

from controller import AppController
from masterDash import MasterDashboard

class FlashDash():
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
            self.bg = PhotoImage(file="UTILITY/BGhalf.png")
            self.back = PhotoImage(file="UTILITY/backDash.png")
            self.card = PhotoImage(file="FLASH/card.png")
            self.forr = PhotoImage(file="FLASH/for.png")
            self.prev = PhotoImage(file="FLASH/prev.png")

            # Create images on the canvas
            self.canvas_image = self.canvas.create_image(0, 0, anchor=NW, image=self.bg)
            self.cardID = self.canvas.create_image(141,200, anchor = NW, image=self.card)

            #Buttons
            backButton = Button(
                root, image=self.back,
                borderwidth=0,
                background="#f4f4f7",
                activebackground="#f4f4f7",
                cursor="hand2",
                command=self.controller.back_masterDash
            )
            self.canvas.create_window(149, 60, anchor=NW, window=backButton)

            prevButton = Button(
                root, image=self.prev,
                borderwidth=0,
                background="#f4f4f7",
                activebackground="#f4f4f7",
                cursor="hand2",
            )
            self.prev_Button_window = self.canvas.create_window(560, 820, anchor=NW, window=prevButton)

            forButton = Button(
                root, image=self.forr,
                borderwidth=0,
                background="#f4f4f7",
                activebackground="#f4f4f7",
                cursor="hand2",
            )
            self.prev_Button_window = self.canvas.create_window(790, 820, anchor=NW, window=forButton)


        except Exception as e:
            print(f"Error loading image: {e}")

        # Configure the scroll region to match the image height
        self.canvas.config(scrollregion=self.canvas.bbox(ALL))

def win():
    root = Tk()
    FlashDash(root)
    root.mainloop()

if __name__ == "__main__":
    win()
