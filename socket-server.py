
import socket

host = "127.0.0.1"  # Server Will Open LOCAL HOST.
port = 4040    # <- PORT

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # <- Socket Created.
server.bind((host, port))   # <- Socket connected host and port.
server.listen(4)    # <- MAX number of users.
try:

    while True:
        conn, addr = server.accept()   # <- Waiting For Users.
        print("[*] "+addr+" Connected")    # <- If someone connect to server

except socket.error as error_message:   # <- If Something Wrong...
    print(error_message)
