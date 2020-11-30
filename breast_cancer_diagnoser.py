import request_manager
import tkinter as tk
import home_screen

# class BreastCancerDiagnoser():
#     def __init__(self):


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")
    gui = home_screen.HomeScreen(master=root)

    gui.master.title("Breast Cancer Diagnoser")
    gui.size()

    gui.mainloop()
