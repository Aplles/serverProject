import signal
import keyboard
import socket
from datetime import datetime

from server.const import headers_200, localhost, port, BASE_DIR, headers_404
from server.static import static
from urls import urlpatterns
from .routing import render



def on_ctrl_s():
    print("Ctrl + S pressed")

keyboard.add_hotkey('ctrl+c', on_ctrl_s)

class Server:

    def __init__(self):
        self.shutdown_requested = False
        self.process()

    def process(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((localhost, port))
        server.listen(5)
        print(f"Starting development server at http://{localhost}:{port}/\nQuit the server with CTRL-BREAK.")

        signal.signal(signal.SIGINT, self.shutdown_handler)

        try:
            while not self.shutdown_requested:
                client_socket, address = server.accept()
                data = client_socket.recv(1024).decode('utf-8')
                response, code = self.routing(data)
                print(
                    f'[{datetime.now().strftime("%d/%b/%Y %H:%M:%S")}] "{data.split()[0]} {data.split()[1]} HTTP/1.1" {code}'
                )
                client_socket.send(response)
                client_socket.shutdown(socket.SHUT_WR)
                keyboard.wait()
        finally:
            print("Server is shutting down...")
            keyboard.unhook_all()
            server.close()

    def shutdown_handler(self, signum, frame):
        self.shutdown_requested = True

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

# server_client = Server()
# server_client.process()
