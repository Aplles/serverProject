from sys import argv

from server.start import execute_command


def main():
    execute_command(argv[1])


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
