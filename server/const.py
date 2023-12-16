from pathlib import Path

localhost = "127.0.0.1"
port = 3030

BASE_DIR = Path(__file__).resolve().parent.parent

headers_200 = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'.encode('utf-8')
headers_404 = 'HTTP/1.1 404 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'.encode('utf-8')
print(BASE_DIR)
