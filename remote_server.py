import socket
from gpiozero import RotaryEncoder
from signal import pause

#testing boot 2

def send_command(host, port, command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sock.sendall(command.encode())
        response = sock.recv(1024)
        print(response.decode('utf-8'))

if __name__ == "__main__":
    host = '192.168.1.48'
    port = 5138

PIN_A = 17
PIN_B = 27

encoder = RotaryEncoder(PIN_A, PIN_B)

step_counter = 0

def value_changed():
    global step_counter
    if encoder.steps > 0:
        step_counter += 1
    else:
        step_counter -= 1
        
    if step_counter % 3 == 0:
        if encoder.steps > 0:
            send_command(host, port, 'off')
        else:
            send_command(host, port, 'on')
            
    encoder.steps = 0            
    print("Counter: ", step_counter)

encoder.when_rotated = value_changed

try:
    pause()
except KeyboardInterrupt:
    print("exiting..")


    
