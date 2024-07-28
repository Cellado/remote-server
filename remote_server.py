import socket
import RPi.GPIO as GPIO
import time


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

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PIN_B, GPIO.IN, pull_up_down=GPIO.PUD_UP)

counter = 0
last_a = GPIO.input(PIN_A)
last_b = GPIO.input(PIN_B)

def rotary_callback(channel):
    global counter, last_a, last_b
    current_a = GPIO.input(PIN_A)
    current_b = GPIO.input(PIN_B)

    if current_a != last_a or current_b != last_b:
        if last_a == 0 and current_a == 1:
            if current_b == 0:
                counter -= 1
            else:
                counter += 1
        elif last_a == 1 and current_a == 0:
            if current_b == 1:
                counter -= 1
            else:
                counter += 1

        print("Counter:", counter)

    last_a = current_a
    last_b = current_b

GPIO.add_event_detect(PIN_A, GPIO.BOTH, callback=rotary_callback)
GPIO.add_event_detect(PIN_B, GPIO.BOTH, callback=rotary_callback)

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Exiting...")

# Cleanup GPIO
GPIO.cleanup()
