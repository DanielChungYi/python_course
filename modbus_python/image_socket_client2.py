import socket
import cv2
import numpy
'''
def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

TCP_IP = "127.0.0.1"
TCP_PORT = 9999

sock = socket.socket()
sock.connect((TCP_IP, TCP_PORT))

while 1:
    #length = recvall(sock,16)
    #stringData = recvall(sock, int(length))
    stringData = sock.recv()
    data = numpy.fromstring(stringData, dtype='uint8')
    decimg=cv2.imdecode(data,1)
    cv2.imshow('CLIENT2',decimg)
    cv2.waitKey(1)

sock.close()
cv2.destroyAllWindows()
'''
import socket
import cv2
import numpy

def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

TCP_IP = "127.0.0.1"
TCP_PORT = 9999

sock = socket.socket()
sock.connect(('127.0.0.1', 9999))
print("connecting \n")
while 1:
    #length = recvall(sock,16)
    #print(length)

    stringData = sock.recv(14860800)
    #data = numpy.fromstring(stringData, dtype='uint8')
    data = numpy.asarray(stringData, dtype='uint8')
    print(data.shape)
    decimg=cv2.imdecode(data,cv2.IMREAD_COLOR)
    RRR = numpy.array(decimg)
    print(RRR.shape)

    #cv2.imshow('CLIENT2',decimg)
    cv2.waitKey(1)

'''
url = 'http://www.pyimagesearch.com/wp-content/uploads/2015/01/google_logo.png'
resp = urllib.urlopen(url)
image =
np.asarray(bytearray(resp.read()), dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_COLOR)
'''

#sock.close()
#cv2.destroyAllWindows()
