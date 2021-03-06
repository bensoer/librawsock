

def assemble_packet(ip_header: bytes, network_header: bytes, user_data: bytes = b'') -> str:

    return '' + ip_header + network_header + user_data
