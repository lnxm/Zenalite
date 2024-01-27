import http.server
import socketserver

# Define the port number
PORT = 8080

# Define the request handler class
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Specify the content type as HTML
        self.send_header('Content-type', 'text/html')
        # Call the base class method to process the request
        http.server.SimpleHTTPRequestHandler.do_GET(self)

# Set the directory where the HTML file is located
DIRECTORY = "."

# Create a TCP server
with socketserver.TCPServer(("", PORT), MyHttpRequestHandler) as httpd:
    print("Server running at port", PORT)
    # Change the current directory to the directory where the HTML file is located
    httpd.RequestHandlerClass.directory = DIRECTORY
    # Start the server
    httpd.serve_forever()