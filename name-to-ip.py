import socket
from sys import argv

script, host = argv

server_ip = socket.gethostbyname(host)

print(server_ip)

