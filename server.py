#!/usr/bin/env python3
import http.server
import socketserver
import os
import webbrowser
import time

os.chdir(r'C:\Users\ASUS\Desktop\personal portfolio')

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super().end_headers()

try:
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"✓ Server started at http://localhost:{PORT}/")
        print(f"✓ Opening portfolio in browser...")
        webbrowser.open(f'http://localhost:{PORT}/index.html')
        print("✓ Server running. Press Ctrl+C to stop.")
        httpd.serve_forever()
except OSError as e:
    print(f"Error: {e}")
    print("Port might be in use. Try a different port.")
