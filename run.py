from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

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

# Start the server
server = HTTPServer(("", PORT), MyHandler)
print(f"Server started on port {PORT}")

# Start serving forever
server.serve_forever()
