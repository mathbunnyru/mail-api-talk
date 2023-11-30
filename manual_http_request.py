#!/usr/bin/env python3
import socket  # create connections

LINE_BREAK = b"\r\n"
address = "75.101.131.185"  # address of httpbin.org
port = 80

request = LINE_BREAK.join((b"GET /get HTTP/1.1", b"Host: httpbin.org")) + 2 * LINE_BREAK

with socket.socket(
    family=socket.AF_INET, type=socket.SOCK_STREAM  # Address Family INET  # TCP
) as sock:
    sock.connect((address, port))
    sock.sendall(request)
    response = sock.recv(1024)

print(response.decode("utf-8"))
