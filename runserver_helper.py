import socket
import subprocess
import sys

def get_available_port():
    # Create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 0))  # Bind to any available port
    sock.listen(1)      # Listen for connections
    _, port = sock.getsockname()
    sock.close()
    return port

def runserver(port):
    # Construct the command to run
    command = [sys.executable, 'manage.py', 'runserver', str(port)]

    try:
        # Start the server process
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Print the output
        for line in iter(process.stdout.readline, b''):
            print(line.decode().strip())

        # Wait for the process to finish
        process.wait()
    except Exception as e:
        print("An error occurred while starting the server:", str(e))
        sys.exit(1)
