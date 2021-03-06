from librawsock.headers.ip import IPHeader
from librawsock.headers.tcp import TCPHeader, TCPFlags
import librawsock.utils.checksum as checksum
import socket

if __name__ == '__main__':

    source_ip = "192.168.10.1"
    destination_ip = "10.1.0.12"

    ip_header = IPHeader()
    ip_header.set_ip_header_length(5) # 5 bytes long
    ip_header.set_ip_version(4)
    ip_header.set_ip_type_of_service(0)
    ip_header.set_destination_ip(destination_ip)
    ip_header.set_source_ip(source_ip)
    ip_header.set_ip_protocol(socket.IPPROTO_TCP)
    ip_header.set_ip_time_to_live(255) # How many hops to the destination before giving up - 255 is max

    # Get the IP Raw Header
    ip_raw_header = ip_header.assemble_raw_header()

    tcp_header = TCPHeader()
    tcp_header.set_tcp_ack_number(0)
    tcp_header.set_tcp_sequence_number(0)
    tcp_header.set_tcp_destination_port(8080)
    tcp_header.set_tcp_source_port(80)
    tcp_header.set_tcp_window(5840) # Max size
    tcp_header.set_tcp_flags(TCPFlags())

    # Get the TCP Raw Header
    tcp_raw_header = tcp_header.assemble_raw_header()

    # Generate TCP Checksum
    tcp_checksum = checksum.generate_tcp_checksum(source_ip, destination_ip, tcp_raw_header)
    tcp_header.set_tcp_checksum(tcp_checksum)

    # Regenerate TCP Raw Header With Checksum
    tcp_raw_header = tcp_header.assemble_raw_header()

