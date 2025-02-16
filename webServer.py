# import socket module
from socket import *
# In order to terminate the program
import sys
def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Prepare a server socket
    serverSocket.bind(("", port))
    # Fill in start
    serverSocket.listen(1)
    # Fill in end
    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()  # Fill in start -are you accepting connections?     #Fill in end
        try:
            message = connectionSocket.recv(1024).decode()  # Fill in start -a client is sending you a message   #Fill in end
            filename = message.split()[1]
            # opens the client requested file.
            # Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
            f = open(filename[1:], 'rb')
            file_content = f.read()
            connectionSocket.send('HTTP/1.1 200 OK\r\n'.encode())
            connectionSocket.send('Content-Type: text/html\r\n'.encode())
            connectionSocket.send("\r\n".encode())
            connectionSocket.sendall(file_content)
            f.close()
        except FileNotFoundError:
            # If the file is not found, send a 404 response
            connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
            connectionSocket.send("Content-Type: text/html\r\n".encode())
            connectionSocket.send("\r\n".encode())
            connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>".encode())
        except Exception as e:
            # If an error occurs with the request, send a 400 Bad Request response
            connectionSocket.send("HTTP/1.1 400 Bad Request\r\n".encode())
            connectionSocket.send("Content-Type: text/html\r\n".encode())
            connectionSocket.send("\r\n".encode())
            connectionSocket.send("<html><body><h1>400 Bad Request</h1></body></html>".encode())
    # Send response message for invalid request due to the file not being found (404)
    # Remember the format you used in the try: block!
    # Close client socket
    # Fill in start
        connectionSocket.close()
    # Fill in end
    # Commenting out the below (some use it for local testing). It is not required for Gradescope, and some students have moved it erroneously in the While loop.
    # DO NOT PLACE ANYWHERE ELSE AND DO NOT UNCOMMENT WHEN SUBMITTING, YOU ARE GONNA HAVE A BAD TIME
    # serverSocket.close()
    # sys.exit()  # Terminate the program after sending the corresponding data
if __name__ == "__main__":
    webServer(13331)
