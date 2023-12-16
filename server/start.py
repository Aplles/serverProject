from server.socket_server import start

COMMANDS = {
    "runserver": start
}


def execute_command(command):
    try:
        COMMANDS[command]()
    except KeyError:
        print(f"Please, input correct command.\nSelect from: {' '.join([key for key in COMMANDS.keys()])}")
