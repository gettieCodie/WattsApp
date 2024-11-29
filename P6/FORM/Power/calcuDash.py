from tkinter import *
# from main import ButtonFunctions

class CalcuDashboard():
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
            self.bg = PhotoImage(file="trace/MASTER.png")
            self.bg = PhotoImage(file="UTILITY/BGhalf.png")
            self.tab = PhotoImage(file="UTILITY/tab.png")
            self.greeting = PhotoImage(file="DASH/greeting.png")
            self.tagline = PhotoImage(file="DASH/TAGLINE.png")
            self.know = PhotoImage(file="DASH/know.png")
            self.study = PhotoImage(file="DASH/studyns.png")
            self.master = PhotoImage(file="DASH/master.png")
            self.calcuSelected = PhotoImage(file="DASH/calcuS.png")
            self.flashDef = PhotoImage(file="MASTER/def.png")
            self.flash_hover = PhotoImage(file="MASTER/hover.png")

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
            command=self.open_studyDash
        )
        self.studyButton_window = self.canvas.create_window(414, 556, anchor=NW, window=studyButton)

        masterButton = Button(
            root, image=self.master,
            borderwidth=0,
            background="#f4f4f7",
            activebackground="#f4f4f7",
            cursor="hand2",
        )
        self.masterButton_window = self.canvas.create_window(750, 556, anchor=NW, window=masterButton)

        calcuButton = Button(
            root, image=self.calcuSelected,
            borderwidth=0,
            background="#f4f4f7",
            activebackground="#f4f4f7",
            cursor="hand2",

        )
        self.calcuButton_window = self.canvas.create_window(1085, 556, anchor=NW, window=calcuButton)


    def open_studyDash(self):
        from studyView import StudyDashboard
        for widget in self.root.winfo_children():
            widget.pack_forget()
        StudyDashboard(self.root)

def win():
    root = Tk()
    CalcuDashboard(root)
    root.mainloop()

if __name__ == "__main__":
    win()