#!/usr/bin/python3
import http.server
import socketserver
import json

PORT = 8000
sample = {
        "name": "John",
        "age": 30,
        "city": "New York"
        }
info = {
        "version": "1.0",
        "description": "A simple APU built with http.server"
        }

class Handler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print(self.path)
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(bytes(json.dumps(sample), 'utf-8'))
        elif self.path == '/status':
            self.send_response(200)
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(bytes(json.dumps(info), 'utf-8'))
        else:
            self.send_error(404, "Endpoint not found")
handler = Handler
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
