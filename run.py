from http.server import HTTPServer, SimpleHTTPRequestHandler
import socket
import os

HOST = 'localhost'  # Change this to your computer's IP address if it's not 'localhost'
PORT = 8000  # Specify the port number here

# Get the path to the home.html file
home_html_path = os.path.join(os.getcwd(), "home.html")

# Create the SimpleHTTPRequestHandler class
class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Check if the requested path is the home page
        if self.path == "/":
            self.path = home_html_path

        # Serve the requested file
        super().do_GET()

# Get the local IP address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
s.close()

# Start the server
server = HTTPServer((ip, PORT), MyHandler)
print(f"Serving on {HOST}:{PORT}")

# Start serving forever
server.serve_forever()
