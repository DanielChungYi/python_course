import socket
#HOST = '169.254.66.181'  # The server's hostname or IP address
#HOST = '127.0.0.1'  # The server's hostname or IP address
HOST = '169.254.118.177'  # The server's hostname or IP address
PORT = 5005        # The port used by the server
Message = "Hello"
BUFFSIZE = 1024


'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
s.send((Message).encode())
data = s.recv(BUFFSIZE)
s.close()
print(data)
'''

from pymodbus3.client.sync import ModbusTcpClient

client = ModbusTcpClient('169.254.118.177',5005)
client.write_coil(1, True)
result = client.read_coils(1,1)
print(result.bits[0])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
s.send((Message).encode())
data = s.recv(BUFFSIZE)
print(data)
client.close()
