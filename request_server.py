import socketserver
import threading
import diagnosis_system
from xml_processor import XmlProcessor


class RequestServer():
    """
    The controller for the server to listen to incoming
    requests

    Implements threading so that the server running is
    not blocking the rest of the program
    """

    def __init__(self, host):
        self.running = False
        self.host = host

    def start(self, port):
        self.__server = socketserver.TCPServer(
            (self.host, port), RequestHandler)
        if not self.running:
            # TODO replace this with logging
            print('**** Starting Server on port {}'.format(port))
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
            # TODO replace this with logging
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
        xml_processor = XmlProcessor()
        # self.request is the TCP socket connected to the client
        data = self.request.recv(1024).strip()
        print("SERVER: {} wrote: {}".format(self.client_address[0], data))

        patient_data = xml_processor.parse_patient_data(data)
        classification = '4' if diagnosis_system.diagnose() else '2'
        patient_data.classification = classification
        response = xml_processor.patient_data_to_xml(patient_data)
        print("SERVER: Responding : {}".format(response))
        self.request.sendall(response)
