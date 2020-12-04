import request_manager
import tkinter as tk
import request_manager
from home_screen import HomeScreen
from patient_data_entry_screen import PatientDataEntryScreen


class BreastCancerDiagnoser(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title = "Breast Cancer Diagnoser"

        # Container setup
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Set up all of the app's screens
        self.frames = {}
        self.frames["HomeScreen"] = HomeScreen(
            parent=container, controller=self)
        self.frames["PatientDataEntryScreen"] = PatientDataEntryScreen(
            parent=container, controller=self)

        self.frames["HomeScreen"].grid(row=0, column=0, sticky="nsew")
        self.frames["PatientDataEntryScreen"].grid(
            row=0, column=0, sticky="nsew")

        # Start screen
        self.show_frame("HomeScreen")

        self.request_manager = request_manager.RequestManager()

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def quit(self):
        self.destroy()


if __name__ == "__main__":
    app = BreastCancerDiagnoser()

    app.mainloop()
