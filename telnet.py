import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0',23))
server.listen(5)
print "[*] Listening on 0.0.0.0:23"

try:

    while 1:
        (client_socket, address) = server.accept()
        client_socket.send("login: ")
        client_socket.recv(4096)
        client_socket.send("Password: ")
        client_socket.recv(4096)
        while 1:
            response = client_socket.recv(4096)
            print response
            if response == "exit":
                server.close()
except KeyboardInterrupt:
    server.close()
    print "Bye!"



