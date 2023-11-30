#!/usr/bin/env python3
# create connections
import socket

# address of httpbin.org
address = "75.101.131.185"
port = 80

request = b"\r\n".join((b"GET /get HTTP/1.1", b"Host: httpbin.org")) + b"\r\n\r\n"

with socket.socket(
    family=socket.AF_INET, type=socket.SOCK_STREAM  # Address Family INET  # TCP
) as sock:
    sock.connect((address, port))
    sock.sendall(request)
    response = sock.recv(1024)

print(response.decode("utf-8"))
