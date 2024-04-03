#START BLOCK FOR GNU-RADIO ARDUINO CONNECTION PUT IN PYTHON SNIPPET BLOCK WITH AFTER START

import serial #allows for serial communication to arduino
from serial.tools import list_ports #allows for listing of available ports
import time #allows for time.sleep() function
def initialize_arduino_by_serial_number(target_serial_number, baudrate=9600, timeout=0.1):
    ports = list_ports.comports()
    for port in ports:
        if port.serial_number == target_serial_number:
            try:
                arduino = serial.Serial(port=port.device, baudrate=baudrate, timeout=timeout)
                print(f"Arduino connected on {port.device}")
                return arduino
            except serial.SerialException as e:
                print(f"Failed to connect to Arduino on {port.device}: {e}")
                return None
    print("Arduino with specified serial number not found. Please check your connection.")
    return None
target_serial_number = '55431313338351610291'
arduino = initialize_arduino_by_serial_number(target_serial_number)
time.sleep(2)
arduino.write(b'1')