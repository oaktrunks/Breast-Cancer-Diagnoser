import request_server
import request_sender
import logging

# Constants
HOST = "localhost"


class RequestManager:
    """
    Manages incoming and outgoing requests
    """

    def __init__(self):
        self.server = request_server.RequestServer(HOST)
        self.sender = request_sender.RequestSender()
        logging.basicConfig(filename='app.log', filemode='a', level=logging.INFO,
                            format='%(asctime)s %(levelname)s - %(message)s')

    def start_server(self, port):
        self.server.start(port)

    def stop_server(self):
        self.server.stop()

    def is_server_running(self):
        return self.server.running

    def send_request(self, data):
        """
        Sends our request to all peer servers in database
        """
        return self.sender.send_request(data)
