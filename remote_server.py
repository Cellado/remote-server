import socket
from gpiozero import RotaryEncoder
from signal import pause



# def send_command(host, port, command):
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#         sock.connect((host, port))
#         sock.sendall(command.encode())
#         response = sock.recv(1024)
#         print(response.decode('utf-8'))

# if __name__ == "__main__":
#     host = '192.168.1.48'
#     port = 5138

PIN_A = 17
PIN_B = 18

encoder = RotaryEncoder(PIN_A, PIN_B)

def value_changed():
    print("Counter:", encoder.steps)

encoder.when_rotated = value_changed

try:
    pause()
except KeyboardInterrupt:
    print("exiting..")
