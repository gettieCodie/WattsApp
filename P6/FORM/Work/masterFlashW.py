from tkinter import *
from masterDashW import MasterDashboard

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
        self.canvas = Canvas(root, width=600, height=600)
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
            self.forr = PhotoImage(file="FLASH/for.png")
            self.prev = PhotoImage(file="FLASH/prev.png")
            self.current_card = 0
            self.is_front = True
            self.flashcards = [
                    ("FLASH/WORK/Definitions/DWork 1.png", "FLASH/WORK/Terms/TWork 1.png"),
                    ("FLASH/WORK/Definitions/DWork 2.png", "FLASH/WORK/Terms/TWork 2.png"),
                    ("FLASH/WORK/Definitions/DWork 3.png", "FLASH/WORK/Terms/TWork 3.png"),
                    ("FLASH/WORK/Definitions/DWork4.png", "FLASH/WORK/Terms/TWork 4.png"),
                    ("FLASH/WORK/Definitions/DWork 5.png", "FLASH/WORK/Terms/TWork 5.png"),
                    ("FLASH/WORK/Definitions/DWork 6.png", "FLASH/WORK/Terms/TWork 6.png"),
                    ("FLASH/WORK/Definitions/DWork 7.png", "FLASH/WORK/Terms/TWork 7.png"),
                    ("FLASH/WORK/Definitions/DWork 8.png", "FLASH/WORK/Terms/TWork 8.png"),
                    ("FLASH/WORK/Definitions/DWork 9.png", "FLASH/WORK/Terms/TWork 9.png"),
                    ("FLASH/WORK/Definitions/DWork 10.png", "FLASH/WORK/Terms/TWork 10.png")
            ]
            self.front_image = PhotoImage(file=self.flashcards[self.current_card][0])
            self.back_image = PhotoImage(file=self.flashcards[self.current_card][1])

            # Create images on the canvas
            self.canvas_image = self.canvas.create_image(0, 0, anchor=NW, image=self.bg)
            
            # Flashcards as label 
            self.card_label = Label(
            root, image=self.front_image,
            width=1220,
            height=670,
            bg="#f4f4f7", 
            highlightthickness=0 

            )
            self.card_label.bind("<Button-1>", self.flip_card)
            self.card_window = self.canvas.create_window(120, 180, anchor=NW, window=self.card_label)
            

            #Buttons
            backButton = Button(
            root, image=self.back,
            borderwidth=0,
            background="#f4f4f7",
            activebackground="#f4f4f7",
            cursor="hand2",
            command=self.back_dash
            )
            self.back_Button_window = self.canvas.create_window(100, 100, anchor=NW, window=backButton)

            prevButton = Button(
            root, image=self.prev,
            borderwidth=0,
            background="#f4f4f7",
            activebackground="#f4f4f7",
            cursor="hand2",
            command=self.prev_card
            )
            self.prev_Button_window = self.canvas.create_window(560, 820, anchor=NW, window=prevButton)

            forButton = Button(
            root, image=self.forr,
            borderwidth=0,
            background="#f4f4f7",
            activebackground="#f4f4f7",
            cursor="hand2",
            command=self.next_card
            )
            self.prev_Button_window = self.canvas.create_window(790, 820, anchor=NW, window=forButton)

            

        except Exception as e:
            print(f"Error loading image: {e}")

        self.canvas.config(scrollregion=self.canvas.bbox(ALL))

        
    def back_dash(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()
        MasterDashboard(self.root)

    def flip_card(self, event):
        self._flip(0)
    
    def _flip(self, step):
        steps = 10  
        if step < steps:
            if step < steps / 2:
                self.card_label.config(image=self.front_image if self.is_front else self.back_image, bg = "#f4f4f7")
            else:
                self.card_label.config(image=self.back_image if self.is_front else self.front_image, bg = "#f4f4f7")
            self.root.after(50, self._flip, step + 1)
        else:
            self.is_front = not self.is_front

            if self.is_front:
                self.card_label.config(bg="f4f4f7")  # Front side color
            else:
                self.card_label.config(bg="f4f4f7")  # Back side color


    def next_card(self):
        self.current_card = (self.current_card + 1) % len(self.flashcards)
        self.is_front = True
        
        self.front_image = PhotoImage(file=self.flashcards[self.current_card][0])
        self.back_image = PhotoImage(file=self.flashcards[self.current_card][1])
        self.card_label.config(image=self.front_image)

        self.card_label.config(image=self.front_image, bg="#f4f4f7")
    
    def prev_card(self):
        self.current_card = (self.current_card - 1) % len(self.flashcards)
        self.is_front = True
        
        self.front_image = PhotoImage(file=self.flashcards[self.current_card][0])
        self.back_image = PhotoImage(file=self.flashcards[self.current_card][1])
        self.card_label.config(image=self.front_image)

        self.card_label.config(image=self.front_image, bg="#f4f4f7")

def win():
    root = Tk()
    FlashDash(root)
    root.mainloop()

if __name__ == "__main__":
    win()
