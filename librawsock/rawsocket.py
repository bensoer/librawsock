import socket


class RawSocketSingletonFactory:

    __instance = None

    @staticmethod
    def get_instance():
        if RawSocketSingletonFactory.__instance is None:
            RawSocketSingletonFactory.__instance = RawSocket()

        return RawSocketSingletonFactory.__instance


class RawSocket:

    def __init__(self):
        self.raw_socket = socket.socket(
            family=socket.AF_INET,
            type=socket.SOCK_RAW,
            proto=socket.IPPROTO_UDP
        )

        # set socket so it can be reused
        self.raw_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # disable kernel from building packet headers
        self.raw_socket.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

        self.destination_address = None
        self.destination_port = None


    def set_destination_address(self, destination_address:str):
        self.destination_address = destination_address

    def set_destination_port(self, destination_port:int):
        self.destination_port = destination_port

    def send_raw_packet(self, packet):
        self.raw_socket.sendto(packet, (self.destination_address, self.destination_port))

