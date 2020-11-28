import serial
import serial.tools.list_ports


def readLastLine(ser):
    data = ''
    while True:
        line = str(ser.readline())
        print("line is: {}".format(line))
        data += str(line)
        if "GetOk" in line:
            # print("data is: {}".format(data))
            return data

'''
https://stackoverflow.com/questions/12090503/listing-available-com-ports-with-python
'''
ports = serial.tools.list_ports.comports()

for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))
ser = serial.Serial('/dev/cu.usbmodem6D76249C49551')
print("serial port name is "+ser.name)
print("port is open or not {}".format(ser.is_open))
command = b'/?SP?'
ser.write(command)
print("sent command {}".format(command))
# s=ser.read(ser.inWaiting())
s = readLastLine(ser)
# print("output is {}".format(s))
ser.close()
print("port is open or not {}".format(ser.is_open))
# line = ser.readline()
# print("line is {}".format(line))
