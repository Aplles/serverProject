import socket
from server.const import headers_200, localhost, port, BASE_DIR, headers_404
from server.static import static
from urls import urlpatterns
from datetime import datetime


def start():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((localhost, port))
    server.listen(100)
    print(f"Starting development server at http://{localhost}:{port}/\nQuit the server with CTRL-BREAK.")
    while True:
        client_socket, address = server.accept()
        data = client_socket.recv(1024).decode('utf-8')
        response, code = routing(data)
        print(f'[{datetime.now().strftime("%d/%b/%Y %H:%M:%S")}] "{data.split()[0]} {data.split()[1]} HTTP/1.1" {code}')
        client_socket.send(response)
        client_socket.shutdown(socket.SHUT_WR)


def routing(request: str):
    template_name = ""
    for url, views in urlpatterns:
        if request.split()[1].startswith('/static/'):
            return headers_200 + static(request), 200
        if f"/{url}" == request.split()[1]:
            _, template_name = views(request)
    if not template_name:
        return headers_404 + html("404.html") + handler_404(), 404
    return headers_200 + html(template_name), 200


def html(template_name):
    with open(f"{BASE_DIR}\\templates\\{template_name}", 'rb') as file:
        response = file.read()
    return response


def handler_404():
    response = "<div>"
    for url, views in urlpatterns:
        response += f"<div class='url'><a href='/{url}'>/{url}\t---\t{views.__name__}</a></div>"
    response += "</div>"
    return response.encode('utf-8')
