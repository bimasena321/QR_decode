import cv2
import pyzbar.pyzbar as scan

cam = cv2.VideoCapture(0)
while True:
    a, cap = cam.read()
    QR_code = scan.decode(cap)
    for QR in QR_code:
        (a,b,c,d) = QR.rect
        cv2.rectangle(cap, (a,b),(a + c, b + d),(0,0,255), 2)
        cv2.putText(cap, str(QR.data),(100,100), cv2.FONT_HERSHEY_PLAIN,2,(255,0,0), 3)
    cv2.imshow("Scannerw QR CODE Test",cap)
    if cv2.waitKey(1) & 0xff == ord("w"):
        break
cam.release()
cam.destroyAllWindows()