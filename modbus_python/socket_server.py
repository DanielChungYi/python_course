#!/usr/bin/env python3
'''
import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
            
'''
#socket
import socket

TCP_IP = '' # this IP of my pc. When I want raspberry pi 2`s as a server, I replace it with its IP '169.254.54.195'
TCP_PORT = 5005
BUFFER_SIZE = 20 # Normally 1024, but I want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print ('Connection address:', addr)
while True:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print ("received data:", data)
    conn.send(data)  # echo
#modbus
'''    
#conn.close()
# --------------------------------------------------------------------------- #
# import the various server implementations
# --------------------------------------------------------------------------- #
from pymodbus.server.sync import StartTcpServer, ModbusTcpServer

from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

from twisted.internet.task import LoopingCall
from twisted.internet import reactor
import threading
# --------------------------------------------------------------------------- #
# configure the service logging
# --------------------------------------------------------------------------- #
import logging

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)


def run_server():
    # ----------------------------------------------------------------------- #
    # initialize your data store
    # ----------------------------------------------------------------------- #

    #   di=block, co=block, hr=block, ir=block
    #   block = ModbusSequentialDataBlock(0x00, [123]*0x20)
    #   store = ModbusSlaveContext(hr=block)

    block1 = ModbusSequentialDataBlock(0x00, [717] * 0x0F)
    block2 = ModbusSequentialDataBlock(0x10, [323] * 0x1F)
    store2 = ModbusSlaveContext(hr=block1, ir=block2)

    slaves = {
        0x01: store2,
    }

    context = ModbusServerContext(slaves=slaves, single=False)

    #   print(block1.values)
    #   print(block2.values)

    # ----------------------------------------------------------------------- #
    # initialize the server information
    # ----------------------------------------------------------------------- #
    # If you don't set this or any fields, they are defaulted to empty strings.
    # ----------------------------------------------------------------------- #
    identity = ModbusDeviceIdentification()
    identity.VendorName = 'Pymodbus'
    identity.ProductCode = 'PM'
    identity.VendorUrl = 'http://github.com/riptideio/pymodbus/'
    identity.ProductName = 'Pymodbus Server'
    identity.ModelName = 'Pymodbus Server'
    identity.MajorMinorRevision = '1.0'

    # ----------------------------------------------------------------------- #
    # run the server you want
    # ----------------------------------------------------------------------- #
    # Tcp:
    # server = StartTcpServer(context, identity=identity, address=('0.0.0.0', 255))

    # start server in a separate thread so that is not blocking
    # server.start_server()

    # to access the blocks for slave 1
    # store_1=server.context[1]

    # to read from the block
    # print("------")
    # print(store_1.getValues(4,0,32))

    # to write to the block
    # store_1.setValues(0x0F, 0, [111, 121, 122, 123, 124])

    # Type-2 Implementationt
    interval = 2
    # loop = LoopingCall(f=updatevalues, a=(context,))
    # loop.start(time, now=True)
    server = ModbusTcpServer(context, identity=identity,
                            address=('', 5020))
    t = threading.Thread(target=server.serve_forever, daemon=True)
    t.start()
    loop = LoopingCall(f=updatevalues, a=server)
    loop.start(interval, now=True)
    reactor.run()

def updatevalues(a):
    print("------------START----------")
    # contxt = a[1]
    rfuncode = 3
    wfuncode = 16
    slave_id = 0x01
    address = 0x00
    contxt = a.context[slave_id]
    values = contxt.getValues(rfuncode, address, count=32)
    print(values)
    values = [val+1 for val in values]
    contxt.setValues(wfuncode, address, values)
    print("-------------END-------------")


if __name__ == "__main__":
    run_server()
'''