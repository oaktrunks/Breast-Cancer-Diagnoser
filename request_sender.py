import threading
import socket
import time
from collections import defaultdict
from xml_processor import XmlProcessor


class RequestSender():
    """
    The class that sends our requests to peer servers

    Implements threading for efficiency purposes
    """

    def __init__(self):
        self.xml_processor = XmlProcessor()
        self.server_list = [{'host': "localhost", 'port': 7123}, {'host': "localhost", 'port': 7124}, {'host': "localhost", 'port': 7125}]

    def send_request(self, data):
        self.voteDict = defaultdict(int)
        patient_data = self.xml_processor.patient_data_to_xml(data)

        for server in self.server_list:
            thread = threading.Thread(
                target=self.__peer_request, args=(server, patient_data))
            thread.start()

        # Sleep for 5 seconds while we wait for responses
        time.sleep(5)

        # Count majority vote
        print(self.voteDict)
        vote = -1
        try:
            vote = max(self.voteDict, key=lambda key: self.voteDict[key])
        except:
            print("no votes")
        return vote

    def __peer_request(self, server, data):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            print("**SENDER: sending {}".format(data))
            sock.connect((server['host'], server['port']))
            sock.sendall(data)

            received = str(sock.recv(1024), "utf-8")
            print("**SENDER: received {}".format(received))

            patient_data = self.xml_processor.parse_patient_data(received)
            self.voteDict[int(patient_data.classification)] += 1
