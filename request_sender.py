import threading
import socket
import time
from collections import defaultdict
from xml_processor import XmlProcessor
import logging


class RequestSender():
    """
    The class that sends our requests to peer servers

    Implements threading for efficiency purposes
    """

    def __init__(self):
        self.xml_processor = XmlProcessor()

        # Process server_list.txt to get list of servers
        self.server_list = []
        with open('server_list.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                linesplit = line.strip().split(' ')
                self.server_list.append(
                    {'host': linesplit[0], 'port': int(linesplit[1])})

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
        logging.info(f"Client - Votes received: {self.voteDict}")
        vote = -1
        try:
            vote = max(self.voteDict, key=lambda key: self.voteDict[key])
        except:
            logging.warning(f"Client - No votes received")
        logging.info(f"Client - Classification: {vote} determined")
        return vote

    def __peer_request(self, server, data):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            logging.info(
                f'Client - Sending request to host {server["host"]} port {server["port"]} with\n\tData:\n\t{data}')

            try:
                sock.connect((server['host'], server['port']))
                sock.sendall(data)

                received = str(sock.recv(1024), "utf-8")
                logging.info(
                    f'Client - Received response from host {server["host"]} port {server["port"]} with\n\tData:\n\t{received}')

                patient_data = self.xml_processor.parse_patient_data(received)
                self.voteDict[int(patient_data.classification)] += 1
            except:
                logging.warning(
                    f'Client - Host {server["host"]} port {server["port"]} is unreachable')
