import socketserver
import threading
import diagnosis_system
from xml_processor import XmlProcessor
import logging


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
            try:
                logging.info(
                    f'Server - Starting server on host {self.host} port {port}')
                self.running = True
                thread = threading.Thread(target=self.__start_server)
                thread.start()
            except:
                self.running = False
                logging.error('Server - Error starting server')

    def __start_server(self):
        # called by thread created by start()
        # starts the TCP server
        with self.__server:
            self.__server.serve_forever()

    def stop(self):
        if self.running:
            logging.info(f'Server - Stopping server')
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
        logging.info("Server - Request received from {} \n\tData: \n\t{}".format(
            self.client_address[0], data))

        patient_data = xml_processor.parse_patient_data(data)
        classification = '4' if diagnosis_system.diagnose() else '2'
        patient_data.classification = classification
        response = xml_processor.patient_data_to_xml(patient_data)

        logging.info("Server - Responding to {} with \n\tData: \n\t{}".format(
            self.client_address[0], response))
        self.request.sendall(response)
