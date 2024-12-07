class CalculatePower:
    def __init__(self, root):
        self.root = root

    def calculate_power(self):
        # Get input values
        work = self.workEntry.get()
        time = self.timeEntry.get()

        # Instantiate backend CalculatePower class
        calc = CalculatePower()

        try:
            # Call the backend logic to calculate power
            power = calc.calcuPow(work, time)

            # Display the result (you can adjust this to show in a label or popup)
            messagebox.showinfo("Result", f"The calculated power is {power} Watts.")

        except ValueError as ve:
            messagebox.showerror("Error", f"Input error: {ve}")
        except ZeroDivisionError as zde:
            messagebox.showerror("Error", f"Time cannot be zero: {zde}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

    def reset_fields(self):
        # Reset the input fields and any result display
        self.workEntry.delete(0, END)
        self.timeEntry.delete(0, END)
