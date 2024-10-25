import http.server
import socketserver
import os

# Set the directory you want to serve
DIRECTORY = "docs"  # Change this to the directory you want to serve

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Serve files from the specified directory
        path = super().translate_path(path)
        return os.path.join(DIRECTORY, os.path.relpath(path, os.path.dirname(path)))

def run(server_class=http.server.HTTPServer, handler_class=CustomHandler):
    port = 8080 # Change this to the port you want to use
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Serving on port {port} from directory: {DIRECTORY}')
    httpd.serve_forever()

if __name__ == "__main__":
    run()