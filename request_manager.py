import request_server
import request_sender

#Constants
PORT = 7123
HOST = "localhost"

class RequestManager:
    """
    Manages incoming and outgoing requests
    """
    def __init__(self):
        self.server = request_server.RequestServer(HOST, PORT)
        self.sender = request_sender.RequestSender()
    
    def start_server(self):
        self.server.start()

    def stop_server(self):
        self.server.stop()

    def is_server_running(self):
        return self.server.running

    def send_request(self, data):
        """
        Sends our request to all peer servers in database
        """
        self.sender.send_request(data)

