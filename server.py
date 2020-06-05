import argparse
import socket
import datetime

host = 'localhost'
port = 123


def calculate(offset):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        print('Server works')
        s.bind((host, port))
        while True:
            data, addr = s.recvfrom(1024)
            official_time = datetime.datetime.now()
            cheated_time = official_time + datetime.timedelta(0, offset)
            time = str(cheated_time)
            s.sendto(time.encode('utf-8'), addr)


def read_config_with_offset():
    with open('./config.txt', 'r') as config:
        try:
            return int(config.read())
        except ValueError:
            print('Invalid time format')
            return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Exact time server that can \"lie\" for the specified number of seconds')
    parser.add_argument('-off', '--offset', type=int, metavar='', help='The number of seconds to subtract or add')
    args = parser.parse_args()
    time_offset = args.offset
    if time_offset is None:
        time_offset = read_config_with_offset()
    calculate(time_offset)
