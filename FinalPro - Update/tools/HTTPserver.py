from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHTTPServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/hello':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            message = "Hello from MyHTTPServer....."
            self.wfile.write(message.encode())
        else:
            self.send_error(404, "Not Found")

def main():
    try:
        server = HTTPServer(('localhost', 8080), MyHTTPServer)
        print('Server is listening on port 8080')
        server.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down the server')
        server.socket.close()

if __name__ == '__main__':
    main()


#curl http://localhost:8080/hello
