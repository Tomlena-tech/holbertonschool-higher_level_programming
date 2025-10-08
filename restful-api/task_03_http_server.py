#!/user/bin/env/python3
""" Develop a simple API using Python with the `http.server` module
that responds to GET requests with a JSON message."""


from http.server import BaseHTTPRequestHandler, HTTPServer
import json
class Simple_server(BaseHTTPRequestHandler):
    """Creta a subsclass of of BaseHTTPRequestHandler"""
    def do_GET(self):
        if self.path == "/" or self.path == "":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API")
         
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"version":"1.0", "description":"a simple API built with http.server"}).encode())    
            
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
            
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"undefined endpoint")
   

        
if __name__ == "__main__":
    PORT = 8000
    server = HTTPServer(('', PORT), Simple_server)
    print(f'Server running on port {PORT}')
    server.serve_forever()
