import cv2
from playsound import playsound

bd = cv2.barcode.BarcodeDetector()
cap = cv2.VideoCapture(0)

detecciones = {}

while True:
    ret, frame = cap.read()
    if ret:
        (ret_bt,
         decode,

         _,
         puntos) = bd.detectAndDecode(frame)
        if ret_bc:
            frame = cv2.polylines(frame,
                                  puntos.astype(int),
                                  True,
                                  (0, 255, 0),
                                  3)