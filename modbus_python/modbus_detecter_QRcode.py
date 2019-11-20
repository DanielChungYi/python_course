
######################################################################
# this code is fork from yolov3-ultralytics detection                #
# using QRcode to identify camera id and send modbus command         #
######################################################################
import argparse
import time
from sys import platform

from models import *
from utils.datasets import *
from utils.utils import *

from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import numpy as np
import cv2
from PIL import ImageGrab

def detect(
        cfg,
        data_cfg,
        weights,
        images='data/samples',  # input folder
        output='output',  # output folder
        fourcc='mp4v',
        img_size=608,
        conf_thres=0.5,
        nms_thres=0.5,
        save_txt=False,
        save_images=True,
        webcam=True,
        num_cams=1,

):

    device0 = torch_utils.select_device()

    torch.backends.cudnn.benchmark = False  # set False for reproducible results
    if os.path.exists(output):
        shutil.rmtree(output)  # delete output folder
    os.makedirs(output)  # make new output folder

    # Initialize model
    if ONNX_EXPORT:
        s = (608, 352)  # (320, 192) or (416, 256) or (608, 352) onnx model image size (height, width)
        model = Darknet(cfg, s)
    else:
        model = Darknet(cfg, img_size)

    # Load weights
    if weights.endswith('.pt'):  # pytorch format
        model.load_state_dict(torch.load(weights, map_location=device0)['model'])
    else:  # darknet format
        _ = load_darknet_weights(model, weights)


    # Fuse Conv2d + BatchNorm2d layers
    model.fuse()

    # Eval mode
    model.to(device0).eval()


    if ONNX_EXPORT:
        img = torch.zeros((1, 3, s[0], s[1]))
        torch.onnx.export(model, img, 'weights/export.onnx', verbose=True)
        return

    # Set Dataloader
    caps = []
    for i in range(num_cams):
        caps.append(cv2.VideoCapture(i))

    # Get classes and colors
    classes = load_classes(parse_data_cfg(data_cfg)['names'])
    colors = [[random.randint(0, 255) for _ in range(3)] for _ in range(len(classes))]
    command = []
    count = 0
    t = time.time()
    for i in range(8):
        # if(i <=2):
        #     command.append(1)
        # else:
        #     command.append(0)
        command.append(0)
        print(bool(command[i]))
    while(True):
        for i in range(num_cams):
# =============================================================================
#             t = time.time()
# =============================================================================
            ret_val, im0 = caps[i].read()
            assert ret_val, 'Webcam Error'
            img, *_ = letterbox(im0, new_shape=img_size)

            # Normalize RGB
            img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB
            img = np.ascontiguousarray(img, dtype=np.float32)  # uint8 to float32

            #QR code
            qrDecoder = cv2.QRCodeDetector()
            inputImage = im0[949:, 1789:, :]
            data,bbox,rectifiedImage = qrDecoder.detectAndDecode(inputImage)
            camera_id = 0
            if len(data)>0:
                #print("Decoded Data : {}".format(data))
                camera_id = int(data)
                print(camera_id)
                #display(inputImage, bbox)
                rectifiedImage = np.uint8(rectifiedImage);
                #cv2.imshow("Rectified QRCode", rectifiedImage);
            else:
                print("QR Code not detected")
                camera_id = 3
                #cv2.imshow("Results", inputImage)
            # if(camera_id <= 2 ):
            #     camera_id = 2
            # Normalize RGB
            img /= 255.0  # 0 - 255 to 0.0 - 1.0
            # Get detections
            img = torch.from_numpy(img).unsqueeze(0).to(device0)
            pred, _ = model(img)
            det = non_max_suppression(pred, conf_thres, nms_thres)[0]

            if det is not None and len(det) > 0:
                # Rescale boxes from 416 to true image size
                det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()
                #modbus
                if(camera_id > 2 and camera_id <= 10):
                    command[int(camera_id-3)] = True
                    rq = client.write_coils(0, command, unit=1)
                    rr = client.read_coils(0, 8, unit=1)
                else:
                    rq = client.write_coils(0, command, unit=1)
                    rr = client.read_coils(0, 8, unit=1)
                # '''
                # if camera_id == 3:
                #     rq = client.write_coils(0, , unit=1)
                # elif camera_id == 4:
                #     rq = client.write_coils(0, [True]*10, unit=1)
                # elif camera_id == 5:
                #     rq = client.write_coils(0, [True]*10, unit=1)
                # elif camera_id == 6:
                #     rq = client.write_coils(0, [True]*10, unit=1)
                # elif camera_id == 7:
                #     rq = client.write_coils(0, [True]*10, unit=1)
                # elif camera_id == 8:
                #     rq = client.write_coils(0, [True]*10, unit=1)
                # else camera_id == 9:
                #     rq = client.write_coils(0, [True]*10, unit=1)
                # '''
                # Print results to screen
                print('%gx%g ' % img.shape[2:], end='')  # print image size
                for c in det[:, -1].unique():
                    n = (det[:, -1] == c).sum()
                    print('%g %ss' % (n, classes[int(c)]), end=', ')
                print('\n')

                # Draw bounding boxes and labels of detections
                for *xyxy, conf, cls_conf, cls in det:
                    if classes[int(cls)] == 'person':
                        # Add bbox to the image
                        label = '%s %.2f' % (classes[int(cls)], conf)
                        plot_one_box(xyxy, im0, label=label, color=colors[int(cls)])
            else:
                #modbus
                if(camera_id > 2 and camera_id <= 10):
                    command[int(camera_id-3)] = False
                    rq = client.write_coils(0, command, unit=1)
                    rr = client.read_coils(0, 8, unit=1)
                else:
                    rq = client.write_coils(0, command, unit=1)
                    rr = client.read_coils(0, 8, unit=1)

            count +=1
            print('FPS: (%.3f fps)' % (count / (time.time() - t)))
# =============================================================================
#             cv2.imwrite('output/img{}.png'.format(count), im0)
# =============================================================================
            cv2.imshow('Webcam{}'.format(i), im0)
            if cv2.waitKey(1) == 27:  # esc to quit
                cv2.destroyAllWindows()
def display(im, bbox):
    n = len(bbox)
    for j in range(n):
        cv2.line(im, tuple(bbox[j][0]), tuple(bbox[ (j+1) % n][0]), (255,0,0), 3)

    # Display results
    cv2.imshow("Results", im)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--cfg', type=str, default='cfg/yolov3-1cls.cfg', help='cfg file path')
    parser.add_argument('--data-cfg', type=str, default='data/coco_1cls.data', help='coco.data file path')
    parser.add_argument('--weights', type=str, default='weights/last.pt', help='path to weights file')
    parser.add_argument('--images', type=str, default='data/samples', help='path to images')
    parser.add_argument('--img-size', type=int, default=608, help='inference size (pixels)')
    parser.add_argument('--conf-thres', type=float, default=0.5, help='object confidence threshold')
    parser.add_argument('--nms-thres', type=float, default=0.5, help='iou threshold for non-maximum suppression')
    parser.add_argument('--fourcc', type=str, default='mp4v', help='fourcc output video codec (verify ffmpeg support)')
    parser.add_argument('--output', type=str, default='output', help='specifies the output path for images and videos')
    parser.add_argument('--num-cams', type=int, default=1, help='how many cams used for this instance')
    opt = parser.parse_args()
    print(opt)
    client = ModbusClient('192.168.0.1', 502)
    client.connect()



    with torch.no_grad():
        detect(opt.cfg,
               opt.data_cfg,
               opt.weights,
               images=opt.images,
               img_size=opt.img_size,
               conf_thres=opt.conf_thres,
               nms_thres=opt.nms_thres,
               fourcc=opt.fourcc,
               output=opt.output,
               num_cams=opt.num_cams)
