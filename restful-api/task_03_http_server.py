#!/user/bin/env python3
""" Develop a simple API using Python with the `http.server` module
that responds to GET requests with a JSON message."""


from http.server import BaseHTTPRequestHandler, HTTPServer
import json
class Simple_server(BaseHTTPRequestHandler):
    """Creta a subsclass of of BaseHTTPRequestHandler"""
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple API!")
        
if __name__ == "__main__":
    PORT = 8000
    server = HTTPServer(('', PORT), Simple_server)
    print(f'Server running on port {PORT}')
    server.serve_forever()
