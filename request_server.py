import socketserver
import threading
import diagnosis_system

class RequestServer():
    """
    The controller for the server to listen to incoming
    requests

    Implements threading so that the server running is
    not blocking the rest of the program
    """

    def __init__(self, host, port):
        self.running = False
        self.__server = socketserver.TCPServer((host, port), RequestHandler)

    def start(self):
        if not self.running:
            #TODO replace this with logging
            print('**** Starting Server')
            self.running = True
            thread = threading.Thread(target=self.__start_server)
            thread.start()

    def __start_server(self):
        # called by thread created by start()
        # starts the TCP server
        with self.__server:
            self.__server.serve_forever()

    def stop(self):
        if self.running:
            #TODO replace this with logging
            print('**** Stopping Server')
            self.running = False
            self.__server.shutdown()


class RequestHandler(socketserver.BaseRequestHandler):
    """
    The request handler for incoming requests.

    This gets instantiated per incoming request and handle()
    handles the request appropriately.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("SERVER: {} wrote: {}".format(self.client_address[0], self.data))
        print("SERVER: Client has cancer: {}".format(diagnosis_system.diagnose()))
        self.request.sendall(self.data.upper())