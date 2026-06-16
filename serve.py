#!/usr/bin/env python3
import http.server, socketserver, threading, time, os

PORT = 4899
DIR = os.path.dirname(os.path.abspath(__file__))

os.chdir(DIR)

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # silent

with socketserver.TCPServer(("", PORT), QuietHandler) as httpd:
    print(f"touch-the-stars running at http://127.0.0.1:{PORT}/  (Ctrl-C to stop)")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nstopped")
