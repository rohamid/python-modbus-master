import serial
import time
import binascii

ser = serial.Serial(port='/dev/ttyUSB0',baudrate=9600,timeout=0.1,
                    parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS)

packet = bytearray()
packet.append(0x02)
packet.append(0x03)
packet.append(0x00)
packet.append(0x21)
packet.append(0x00)
packet.append(0x01)
packet.append(0xD4)
packet.append(0x33)

# packet.append(0x00)
# packet.append(0x03)
# packet.append(0x00)
# packet.append(0x00)
# packet.append(0x00)
# packet.append(0x01)
# packet.append(0x85)
# packet.append(0xDB)

print(packet)
# counter = 0
# while counter < 1:
#     counter = counter + 1
#     ser.write(packet)
#     data_raw = ser.readline()
#     print(data_raw)
#     data = binascii.hexlify(data_raw)
#     print("Response 1 ", data)

ser.write(packet)
data_raw = ser.readline()
print(data_raw)
data = binascii.hexlify(data_raw)
print("Response 1 ", data)
