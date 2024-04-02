#**IMPORTS**
import serial #allows for serial communication to arduino
from serial.tools import list_ports #allows for listing of available ports
import subprocess #allows for running of GNU Radio flowgraphs
import time #allows for time.sleep() function

#**VARIABLE DECLARATIONS** 



#**ARDUNIO CONNECTION FUNCTION**
def find_arduino_by_serial_number(target_serial_number):
    ports = list_ports.comports()
    for port in ports:
        if port.serial_number == target_serial_number:
            return port.device
    return None  # Return None if no matching Arduino found
target_serial_number = '55431313338351610291'
arduino_port = find_arduino_by_serial_number(target_serial_number)
if arduino_port:
    arduino = serial.Serial(port=arduino_port, baudrate=9600, timeout=.1)
else:
    print("Arduino with specified serial number not found. Please check your connection.")
    exit()

#**FUNCTION TO SEND COMMANDS TO ARDUINO**
def send_command(command):
    arduino.write(bytes(command, 'utf-8'))

if __name__ == '__main__':
    print("Hello World")