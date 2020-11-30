import threading
import socket

class RequestSender():
    """
    The class that sends our requests to peer servers

    Implements threading for efficiency purposes
    """
    def __init__(self):
        #TODO get list of servers from DB instead
        self.server_list = [{'host': "localhost", 'port': 7123}]

    def send_request(self, data):
        for server in self.server_list:
            thread = threading.Thread(target=self.__peer_request, args=(server, data))
            thread.start()

    def __peer_request(self, server, data):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            print("**SENDER: sending {}".format(data))
            sock.connect((server['host'], server['port']))
            sock.sendall(bytes(data + "\n", "utf-8"))

            received = str(sock.recv(1024), "utf-8")
            print("**SENDER: received {}".format(received))