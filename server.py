import threading
from socketserver import ThreadingMixIn
import http.server
import random
from prometheus_client import start_http_server
from prometheus_client import Counter

REQUESTS = Counter('requests_total',
        'Hello Worlds requested.')
EXCEPTIONS = Counter('request_exceptions_total',
        'Exceptions serving Hello World.')

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        REQUESTS.inc()
        with EXCEPTIONS.count_exceptions():
          if random.random() < 0.02:
            raise Exception
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello World")

class MultiThreadedHTTPServer(ThreadingMixIn, http.server.HTTPServer):
      pass

class Server(threading.Thread):
    def run(self):
        start_http_server(8000)
        server = http.server.HTTPServer(('localhost', 8001), MyHandler)
        server.serve_forever()
