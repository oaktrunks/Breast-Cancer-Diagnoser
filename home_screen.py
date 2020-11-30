import tkinter as tk
import request_manager

class HomeScreen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

        self.request_manager = request_manager.RequestManager()

    def create_widgets(self):
        """
        Function does the initial page setup
        """
        # Start / Stop server button
        self.server_button = tk.Button(self)
        self.server_button["text"] = "Start server"
        self.server_button["command"] = self.start_server
        self.server_button.pack(side="top", pady=20)

        # Send Request button
        self.send_request_button = tk.Button(self)
        self.send_request_button["text"] = "Send request"
        self.send_request_button["command"] = self.send_request
        self.send_request_button.pack(side="top", pady=20)

        # Quit button
        self.quit_button = tk.Button(self, text="QUIT", fg="red",
                              command=self.quit_action)
        self.quit_button.pack(side="top", pady=20)

    def quit_action(self):
        if self.request_manager.is_server_running():
            self.request_manager.stop_server()
        self.master.destroy()

    def start_server(self):
        self.request_manager.start_server()
        self.server_button["text"] = "Stop server"
        self.server_button["command"] = self.stop_server

    def stop_server(self):
        self.request_manager.stop_server()
        self.server_button["text"] = "Start server"
        self.server_button["command"] = self.start_server

    def send_request(self):
        self.request_manager.send_request('test')
