import socket
import cv2
import numpy
from PIL import ImageGrab
'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(True)

print("start~~~")

#ret, frame = capture.read()
encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
print("start~~~")

while True:
    conn, addr = s.accept()
    frame = ImageGrab.grab()
    result, imgencode = cv2.imencode('.jpg', frame, encode_param)
    data = numpy.array(imgencode)
    stringData = data.tostring()
    print("sended")

    #conn.send( str(len(stringData)).ljust(16));
    conn.send( stringData );

conn.close()
cv2.destroyAllWindows()
'''

capture = ImageGrab.grab()

#isinstance(capture, int)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(True)

conn, addr = s.accept()

#ret, frame = capture.read()
encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
while True:
    data = numpy.array(capture)
    print(data.shape)
    bgr = cv2.cvtColor(data, cv2.COLOR_RGB2BGR)
    result, imgencode = cv2.imencode('.jpg', bgr, encode_param)
    stringData = data.tostring()
    print(str(len(stringData)))
    #conn.send( str(len(stringData)).ljust(16));
    conn.send( stringData );
    print("sending \n")
    '''
    ret, frame = capture.read()
    decimg=cv2.imdecode(data,1)
    cv2.imshow('SERVER2',decimg)
    cv2.waitKey(30)
    '''
#conn.close()
#cv2.destroyAllWindows()
