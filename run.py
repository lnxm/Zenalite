import http.server
import socketserver
import socket
import os

# Set the port number you want to use
PORT = 8000

# Get the local IP address of the machine
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Change directory to where your HTML file is located
os.chdir(current_dir)

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = 'home.html'  # Specify the file to be served
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Check if home.html file exists
if os.path.exists("home.html"):
    # Print the IP address
    print(f"Server started at http://{local_ip}:{PORT}")

    # Create a TCP server
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Serving HTTP on", httpd.server_address)
        # Serve indefinitely
        httpd.serve_forever()
else:
    print("Error: 'home.html' file not found in the current directory.")
