import socket
import ssl

def fetch_https_content(hostname, port=443):
    # Create a default SSL context
    context = ssl.create_default_context()

    try:
        # Establish a TCP connection to the server
        with socket.create_connection((hostname, port)) as sock:
            # Wrap the socket in an SSL context for a secure connection
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                print(f"SSL protocol version: {ssock.version()}")

                # Send an HTTP GET request
                request = f"GET / HTTP/1.1\r\nHost: {hostname}\r\nConnection: close\r\n\r\n"
                ssock.send(request.encode())

                # Receive the server's response
                response = b""
                while True:
                    data = ssock.recv(4096)
                    if not data:
                        break
                    response += data
                
                # Decode and print the response
                print("Response from the server:")
                print(response.decode())

    except socket.error as e:
        print(f"Socket error: {e}")
    except ssl.SSLError as e:
        print(f"SSL error: {e}")
    except Exception as e:
        print(f"General error: {e}")

# Main execution
hostname = "www.python.org"
fetch_https_content(hostname)
