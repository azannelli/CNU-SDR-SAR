#**IMPORTS**
import serial #allows for serial communication to arduino
from serial.tools import list_ports #allows for listing of available ports
import subprocess #allows for running of GNU Radio flowgraphs
import time #allows for time.sleep() function

#**GLOBAL VARIABLES**
#file path will need to be changed
#signal duration will need to be adjusted based on testing
#grc_or_python will need to be adjusted based on the file being used
#arduino_start_key shouldnt need to be changed if using arduino code provided
file_path = 'placeholder.grc'
arduino_start_key = 1
signal_duration_seconds = 10
grc_or_python = False #true for python, false for grc

#**ARDUNIO CONNECTION FUNCTION**
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

#**GNU RADIO OPENING**
def execute_gnuradio_flowchart(flowchart_path, is_python_file=False):
    if is_python_file:
        # If it's a Python file, just run the Python file directly.
        gnuradio_command = ['python', flowchart_path]
    else:
        # If it's a GNU Radio flowchart, use the gnuradio-companion command to execute it.
        gnuradio_command = ['gnuradio-companion', '--execute', flowchart_path]
    
    # Launch the process
    process = subprocess.Popen(gnuradio_command)
    return process

if __name__ == "__main__":
    target_serial_number = '55431313338351610291'
    arduino = initialize_arduino_by_serial_number(target_serial_number)
    if arduino is None:
        exit()

    #starts arduino moving
    arduino.write(bytes(arduino_start_key, 'utf-8'))

    #make sure to update below with the path to the flowchart
    process = execute_gnuradio_flowchart(file_path, is_python_file=grc_or_python)

    #length of signal duration will prob need to be calculated through testing
    time.sleep(signal_duration_seconds)

    #close gnu radio flowgraph
    process.terminate()

    #close arduino and stop movement
    arduino.close()