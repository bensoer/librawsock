import socket
from struct import pack


class TCPFlags:

    tcp_fin = 0
    tcp_syn = 0
    tcp_rst = 0
    tcp_psh = 0
    tcp_ack = 0
    tcp_urg = 0


class TCPHeader:

    def __init__(self):
        self.tcp_source = None
        self.tcp_dest = None
        self.tcp_seq = 454
        self.tcp_ack_seq = 0
        self.tcp_doff = 5 # DataOffset

        self.tcp_flags = None

        self.tcp_window = None
        self.tcp_check = None # Set to 0 as generation requires us to assemble a bit first
        self.tcp_urg_ptr = 0

    def set_tcp_source_port(self, source_port: int):
        self.tcp_source = source_port

    def set_tcp_destination_port(self, destination_port: int):
        self.tcp_dest = destination_port

    def set_tcp_sequence_number(self, sequence_number: int):
        self.tcp_seq = sequence_number

    def set_tcp_ack_number(self, ack_number: int):
        self.tcp_ack_seq = ack_number

    def set_tcp_flags(self, tcp_flags:TCPFlags):
        self.tcp_flags = tcp_flags

    def set_tcp_window(self, tcp_window: int):
        self.tcp_window = socket.htons(tcp_window)

    def set_tcp_checksum(self, tcp_checksum:int):
        self.tcp_check = tcp_checksum

    def set_tcp_urgent_pointer(self, tcp_urgent_ptr:int):
        self.tcp_urg_ptr = tcp_urgent_ptr

    def assemble_raw_header(self):

        tcp_offset_res = (self.tcp_doff << 4) + 0
        packed_tcp_flags = self.tcp_flags.tcp_fin + (self.tcp_flags.tcp_syn << 1 ) + (self.tcp_flags.tcp_rst << 2) + (self.tcp_flags.tcp_psh << 3) + (self.tcp_flags.tcp_ack << 4) + (self.tcp_flags.tcp_urg << 5)

        if self.tcp_check is None:
            return pack(
                '!HHLLBBHHH',
                self.tcp_source,
                self.tcp_dest,
                self.tcp_seq,
                self.tcp_ack_seq,
                tcp_offset_res,
                packed_tcp_flags,
                self.tcp_window,
                0,
                self.tcp_urg_ptr
            )
        else:
            return pack('!HHLLBBH',
                        self.tcp_source,
                        self.tcp_dest,
                        self.tcp_seq,
                        self.tcp_ack_seq,
                        tcp_offset_res,
                        packed_tcp_flags,
                        self.tcp_window
                        )\
                   + pack('H',
                          self.tcp_check
                        )\
                   + pack('!H',
                          self.tcp_urg_ptr
                          )

