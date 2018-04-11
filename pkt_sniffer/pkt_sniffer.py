import socket
import struct
import textwrap


def main():
    connection = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

    while True:
        raw_data, addr = connection.recv(65536)
        raw_data = str(raw_data, 'utf-8')
        des_mac, src_mac, eth_protocol, data = unpack_frame(raw_data)

        print('\nEthernet Frame:')
        print('Destination Mac: {}, Source Mac: {}, Protocol: {}'.format(des_mac, src_mac, eth_protocol))


# unpack frame to discover protocol (for classify), des mac add and src mac add
def unpack_frame(data):
    des_mac, src_mac, protocol = struct.unpack('! 6s 6s H', data[:14])
    return format_mac(des_mac), format_mac(src_mac), socket.htons(protocol), data[14:]


# format mac with AA:AA:AA:AA:AA:AA
def format_mac(bytes_addr):
    bytes_str = map('{:2x}'.format, bytes_addr)
    return ':'.join(bytes_str).upper()

main()