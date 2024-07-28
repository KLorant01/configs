import serial

# Replace 'COMx' with the correct serial port (e.g., COM3 on Windows or /dev/ttyUSB0 on Linux)
ser = serial.Serial('COMx', baudrate=9600)

with open('output.txt', 'w') as file:
    while True:
        data = ser.readline().decode('utf-8')
        print(data, end='')  # Optional: Print the data to console
        file.write(data)