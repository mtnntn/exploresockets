import os
import sys
import socket

# Verify input and exit with code 2 if input is bad
if len(sys.argv) != 3:
    print("usage: python3 my_server.py <address> <port_number>")
    sys.exit(os.EX_IOERR)

port = int(sys.argv[2])
host = socket.gethostbyname(sys.argv[1])
server = (host, port)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

sock.connect(server)
print("Successfully connected to Server: %s:%d" % server)

inputMex = "Insert a number or type 'quit': \t "
user_input = input("%s" % inputMex)
while user_input != "quit":
    try:
        int(user_input)
        sock.send(user_input.encode())
        resp = sock.recv(1024)
        print(resp.decode())
    except ValueError:
        print("\n invalid input ...")
    user_input = input(inputMex)

sock.close()
print("C u soon, goodbye :D ")
