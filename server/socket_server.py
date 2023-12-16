import socket

from server.const import headers_200, localhost, port, BASE_DIR, headers_404
from server.static import static
from urls import urlpatterns
from datetime import datetime
from .routing import render


class Server:

    def process(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((localhost, port))
        server.listen(5)
        print(f"Starting development server at http://{localhost}:{port}/\nQuit the server with CTRL-BREAK.")
        while True:
            client_socket, address = server.accept()
            data = client_socket.recv(1024).decode('utf-8')
            response, code = self.routing(data)
            print(
                f'[{datetime.now().strftime("%d/%b/%Y %H:%M:%S")}] "{data.split()[0]} {data.split()[1]} HTTP/1.1" {code}'
            )
            client_socket.send(response)
            client_socket.shutdown(socket.SHUT_WR)

    def routing(self, request: str):
        if request.split()[1].startswith('/static/'):
            return headers_200 + static(request), 200
        template = ""
        for url, views in urlpatterns:
            if f"/{url}" == request.split()[1]:
                _, template = views(request)
        if not template:
            return self.handler_404(request)
        return headers_200 + template.encode('utf-8'), 200

    @staticmethod
    def html_server(template_name):
        with open(f"{BASE_DIR}\\server\\templates\\{template_name}", 'rb') as file:
            response = file.read()
        return response

    @staticmethod
    def handler_404(request):
        _, template = render(request, '404.html', context={
            'urlpatterns': urlpatterns
        })
        return headers_404 + template.encode('utf-8'), 404


server_client = Server()
server_client.process()
