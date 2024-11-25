from tkinter import *
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
            self.bg = PhotoImage(file="trace/FCBACK.png")
            self.back = PhotoImage(file="UTILITY/backDash.png")
            

            # Create images on the canvas
            self.canvas_image = self.canvas.create_image(0, 0, anchor=NW, image=self.bg)
            
            backButton = Button(
            root, image=self.back,
            borderwidth=0,
            background="#f4f4f7",
            activebackground="#f4f4f7",
            cursor="hand2",
            command=self.back_dash
            )
            self.back_Button_window = self.canvas.create_window(414, 35, anchor=NW, window=backButton)
        except Exception as e:
            print(f"Error loading image: {e}")

        # Configure the scroll region to match the image height
        self.canvas.config(scrollregion=self.canvas.bbox(ALL))

        
    def back_dash(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()
        MasterDashboard(self.root)


def win():
    root = Tk()
    FlashDash(root)
    root.mainloop()

if __name__ == "__main__":
    win()
