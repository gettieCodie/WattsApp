from tkinter import *
from masterDash import MasterDashboard

class Power():
    def on_mousewheel(self, event):
        self.canvas.yview_scroll(-1 * (event.delta // 120), "units")  # Scroll by units

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
            self.bg = PhotoImage(file="trace/CalPower.png")
            self.back = PhotoImage(file="UTILITY/backDash.png")
            self.title = PhotoImage(file="Cpower/what.png")
            self.powerSel = PhotoImage(file="Cpower/POWER.png")
            self.work = PhotoImage(file="Cpower/WORK1.png")
            self.time = PhotoImage(file="Cpower/time1.png")
            self.solveTable = PhotoImage(file="Cpower/solveTable.png")


            # Create images on the canvas
            self.canvas_image = self.canvas.create_image(0, 0, anchor=NW, image=self.bg)
            self.titleID = self.canvas.create_image(473, 90, anchor = NW, image = self.title)
            # self.solveID = self.canvas.create_image(139, 580, anchor=NW, image=self.solveTable)

            #Buttons---------------------------------------
            backButton = Button(
            root, image=self.back,
            borderwidth=0,
            background="#f4f4f7",
            activebackground="#f4f4f7",
            cursor="hand2",
            command=self.back_dash
            )
            self.back_Button_window = self.canvas.create_window(149, 70, anchor=NW, window=backButton)

            powerButton = Button(
            root, image=self.powerSel,
            borderwidth=0,
            background="#f4f4f7",
            activebackground="#f4f4f7",
            cursor="hand2"
            )
            self.power_Button_window = self.canvas.create_window(135, 158, anchor=NW, window=powerButton)

            workButton = Button(
            root, image=self.work,
            borderwidth=0,
            background="#f4f4f7",
            activebackground="#f4f4f7",
            cursor="hand2"
            )
            self.power_Button_window = self.canvas.create_window(550, 162, anchor=NW, window=workButton)

            timeButton = Button(
            root, image=self.time,
            borderwidth=0,
            background="#f4f4f7",
            activebackground="#f4f4f7",
            cursor="hand2"
            )
            self.power_Button_window = self.canvas.create_window(960, 162, anchor=NW, window=timeButton)

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
    Power(root)
    root.mainloop()

if __name__ == "__main__":
    win()
