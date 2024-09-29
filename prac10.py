import socket
import ssl

hostname = 'www.python.org'
context = ssl.create_default_context()

with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(ssock.version())
        
        # Corrected the HTTP request format
        req = f"GET / HTTP/1.1\r\nHost: {hostname}\r\nConnection: close\r\n\r\n"
        ssock.send(req.encode())

        # Receiving the response
        res = ssock.recv(4096).decode()

        print("response")
        print(res)
        
        # Close the socket properly
        ssock.close()
