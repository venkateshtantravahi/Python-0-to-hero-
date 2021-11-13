# this file demonstrate he basic usage of socket to get data from
# url and use it
import socket

# creates socket at specified parameters and what this socket used for
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# creates socket for specific server at specific port
mysock.connect(("data.pr4e.org", 80))
# sending the socket command it's something like hitting url without browser
cmd = "GET https://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n".encode()
mysock.send(cmd)

# retrieving data back and decoding so that it turns back to unicode string
# format as there will be some intermediate format that has been returned by server
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end="")

# as when you are opening socket there will be some memory occupied
# in loading things so it's always best practise to close connection
mysock.close()
