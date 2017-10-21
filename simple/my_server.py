import os
import sys
import socket

# Verify input and exit with code 2 if input is bad
if len(sys.argv) != 2:
    print("usage: python3 server.py <port_number>")
    sys.exit(os.EX_IOERR)
try:
    PORT = int(sys.argv[1])
except ValueError:
    print("usage: python3 my_server.py <port_number>\n <port_number> must be a number!")
    sys.exit(os.EX_IOERR)

# Request a socket to OS.
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

# Bind -> no need to use htons, bind method do it automatically.
HOST = socket.gethostname()
server = (HOST, PORT)

listen_socket.bind(server)

print("Server started at %s:%d, pid: %d" % (server[0], server[1], os.getpid()))

# (TCP -> Listen) and backlog queue with size 4
listen_socket.listen(4)
while 1:
    client_conn, client_addr = listen_socket.accept()
    tot = 0
    print("\n-----------------------------------------------------")
    print("\nServing client: ", client_conn, "at", client_addr)
    calculate = True
    while calculate:
        req = client_conn.recv(1024)
        print("\n Message from client: ", req)
        if len(req) == 0:
            client_conn.close()
            print("\nConnection closed\n")
            print("-----------------------------------------------------\n")
            calculate = False
        else:
            req = bytes(req)
            tot = str(int(tot) + int(req))
            resp = "Result: " + tot + " ;"
            client_conn.send(resp.encode())
