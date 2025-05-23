from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        query = parse_qs(parsed_path.query)

        login = query.get('login', [''])[0]

        if login == 'is-34fiot-23-173': 
            response = '''
                <html>
                    <body>
                        <h1>Personal Information</h1>
                        <p><strong>Surname:</strong> Романюк</p>
                        <p><strong>Name:</strong> Діана</p>
                        <p><strong>Course:</strong> 2</p>
                        <p><strong>Group:</strong> ІС-34</p>
                    </body>
                </html>
            '''
        else:
            response = '<p>Cannot find or receive a login!</p>'

        print("Відправляю відповідь:")
        print(response)

        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=MyHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Сервер запущено на http://localhost:{port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
