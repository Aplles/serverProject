from server.const import BASE_DIR


def static(request):
    with open(f"{BASE_DIR}\\{request.split()[1]}", 'rb') as file:
        response = file.read()
    return response
