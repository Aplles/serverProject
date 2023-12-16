from server.socket_server import Server

COMMANDS = {
    "runserver": Server().process
}


def execute_command(command):
    try:
        COMMANDS[command]()
    except KeyError:
        print(f"Please, input correct command.\nSelect from: {' '.join([key for key in COMMANDS.keys()])}")
