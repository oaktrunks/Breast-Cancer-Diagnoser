import tkinter as tk


class HomeScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.create_widgets()

    def create_widgets(self):
        """
        Function does the initial page setup
        """
        # Port input
        self.portLabel = tk.Label(self, text="Port")
        self.portLabel.pack(side="top")
        self.portInput = tk.Entry(self)
        self.portInput.pack(side="top", padx=50)

        # Start / Stop server button
        self.server_button = tk.Button(self)
        self.server_button["text"] = "Start server"
        self.server_button["command"] = self.start_server
        self.server_button.pack(side="top", pady=20)

        # Input Patient Data
        self.input_button = tk.Button(self)
        self.input_button["text"] = "Input Patient Data"
        self.input_button["command"] = self.input_data
        self.input_button.pack(side="top", pady=20)

        # Quit button
        self.quit_button = tk.Button(self, text="QUIT", fg="red",
                                     command=self.quit_action)
        self.quit_button.pack(side="top", pady=20)

    def quit_action(self):
        if self.controller.request_manager.is_server_running():
            self.controller.request_manager.stop_server()
        self.controller.quit()

    def start_server(self):
        self.controller.request_manager.start_server(int(self.portInput.get()))
        self.server_button["text"] = "Stop server"
        self.server_button["command"] = self.stop_server

    def stop_server(self):
        self.controller.request_manager.stop_server()
        self.server_button["text"] = "Start server"
        self.server_button["command"] = self.start_server

    def input_data(self):
        self.controller.show_frame("PatientDataEntryScreen")
