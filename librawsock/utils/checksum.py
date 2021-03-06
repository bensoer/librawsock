from struct import pack
import socket
import array


def checksum(packet: bytes) -> int:
    '''
    Generate a checksum
    :param packet:
    :return: int - checksum represented as an int. This is so that it is interpreted correctly by struct.pack
    '''
    if len(packet) % 2 != 0:
        packet += b'\0'
    res = sum(array.array("H", packet))
    res = (res >> 16) + (res & 0xffff)
    res += res >> 16

    return (~res) & 0xffff


def generate_tcp_checksum(source_ip: str, destination_ip: str, tcp_raw_header:bytes, raw_application_layer_data:bytes=b''):

    psh = pack(
        '!4s4sBBH',
        socket.inet_aton(source_ip),
        socket.inet_aton(destination_ip),
        0,
        socket.IPPROTO_TCP,
        len(tcp_raw_header) + len(raw_application_layer_data)
    )
    psh = psh + tcp_raw_header + raw_application_layer_data
    tcp_checksum = checksum(psh)

    return tcp_checksum
