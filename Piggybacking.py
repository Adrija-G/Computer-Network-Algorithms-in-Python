import time
import random

class NetworkNode:
    def __init__(self, name):
        self.name = name
        self.buffer = []
        self.sequence_number = 1
        self.expected_sequence_number = 1
        self.timer_start_time = None
        self.timeout_duration = 2.0

    def send_data(self, receiver, data):
        packet = {
            'type': 'data',
            'sequence_number': self.sequence_number,
            'data': data
        }
        self.sequence_number += 1
        self.expected_sequence_number += 1
        receiver.receive_packet(packet)

        # Start the timer
        self.timer_start_time = time.time()

    def send_ack(self, receiver):
        packet = {
            'type': 'ack',
            'ack_number': self.expected_sequence_number - 1
        }
        receiver.receive_packet(packet)

    def handle_timeout(self):
        if self.expected_sequence_number > self.sequence_number:
            print(f"{self.name} Timeout: Resending data with sequence number {self.sequence_number}")
            self.send_data(network_nodes[1], f"Resent Data with Seq {self.sequence_number}")

    def receive_packet(self, packet):
        if packet['type'] == 'data':
            print(f"{self.name} received data with sequence number {packet['sequence_number']}: {packet['data']}")
            if packet['sequence_number'] == self.expected_sequence_number:
                self.expected_sequence_number += 1
                self.send_ack(network_nodes[1])
                self.timer_start_time = None
        elif packet['type'] == 'ack':
            print(f"{self.name} received ACK for sequence number {packet['ack_number']}")
            if packet['ack_number'] == self.sequence_number - 1:
                print(f"{self.name} acknowledged data with sequence number {packet['ack_number']}")
                self.timer_start_time = None

def main():
    node_names = ["Sender", "Receiver"]
    global network_nodes
    network_nodes = [NetworkNode(name) for name in node_names]

    while True:
        sender_input = input("Enter the message to send (or 'exit' to quit): ")
        if sender_input.lower() == 'exit':
            break

        network_nodes[0].send_data(network_nodes[1], sender_input)

        # Check for timeout in sender
        if network_nodes[0].timer_start_time is not None and \
           time.time() - network_nodes[0].timer_start_time > network_nodes[0].timeout_duration:
            network_nodes[0].handle_timeout()

if __name__ == "__main__":
    main()

