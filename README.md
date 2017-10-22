# Readme

## Scope
The project has the scope to help me understand how to play with sockets using *python3* language.
It's a simple client-server protocol implementation that allows client to contact the server, ask to execute sums and have a result back.

## Dependencies
- *python3*

## Base Structure:
There are different folders for different variation of the protocol.
The simple structure common to each version provide 2 python files: *my_client.py* and  *my_server.py*.
Obviously *my_server.py* is the server implementation, while *my_client.py* the client.

## Run
#### Server
The server *my_server.py* takes in input the port number where will be listening.
So, assuming you're using Bash, it can be launched this way:
```Bash
python3 my_server.py 2000
``` 
#### Client
The client *my_client.py* takes in input the server IP or name and the port number where the server is listening.
So, assuming you're using Bash, it can be launched this way:
```Bash
python3 my_client.py localhost 2000
``` 
Or alternatively:
```Bash
python3 my_client.py 127.0.0.1 2000
``` 

## Versions
#### Simple
This is the first and simplest version.
In this version the server works with only one client per-time: only when a client has finished his calculation the server can accept a connection from another one. 