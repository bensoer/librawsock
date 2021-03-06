import socket
from struct import pack


class IPHeader:

    def __init__(self):
        self.ip_ihl = None
        self.ip_ver = None
        self.ip_tos = None
        self.ip_tot_len = 0 # Kernel will generate this itself
        self.ip_id = 54321
        self.ip_frag_off = 0
        self.ip_ttl = None
        self.ip_proto = None
        self.ip_check = 0 # Kernel will generate this itself
        self.ip_saddr = None
        self.ip_daddr = None

    def set_ip_header_length(self, ip_ihl: int):
        self.ip_ihl = ip_ihl

    def set_ip_version(self, ip_ver: int):
        self.ip_ver = ip_ver

    def set_ip_type_of_service(self, ip_tos: int):
        self.ip_tos = ip_tos

    def set_ip_time_to_live(self, ip_ttl: int):
        self.ip_ttl = ip_ttl

    def set_ip_protocol(self, ip_proto: int):
        self.ip_proto = ip_proto

    def set_source_ip(self, source_ip: str):
        # convert the string to network byte representation
        self.ip_saddr = socket.inet_aton(source_ip)

    def set_destination_ip(self, destination_ip: str):
        # convert the string to network byte representation
        self.ip_daddr = socket.inet_aton(destination_ip)

    def assemble_raw_header(self):

        ip_ihl_ver = (self.ip_ver << 4) + self.ip_ihl

        ip_header = pack(
            '!BBHHHBBH4s4s',
            ip_ihl_ver,
            self.ip_tos,
            self.ip_tot_len,
            self.ip_id,
            self.ip_frag_off,
            self.ip_ttl,
            self.ip_proto,
            self.ip_check,
            self.ip_saddr,
            self.ip_daddr
        )

        return ip_header