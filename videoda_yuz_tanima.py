import time

import cv2
#video ismi
video_name="videom1.mp4"

#video içe aktar: capture, cap
cap= cv2.VideoCapture(video_name)

#videonun genişliği ve yüksekliği 3. parametre genişlik ,4. yüksekliktir
print("genislik", cap.get(3))
print("yukseklik", cap.get(4))

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#video acılabilmis mi diye kesinlikle kontrol etmelisin
if cap.isOpened()== False :
    print("hata")
while True:
    #videoyu nasıl okuyacağız:
    ret , frame= cap.read()
    #ret basarılı olup olmadıgı , frame okudugu resim
    if ret== True:
        time.sleep(0.01)# bunu yapmazsak çok hızlı akar
        face_rect = face_cascade.detectMultiScale(frame, minNeighbors=7)
        for (x, y, w, h) in face_rect:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 10)

        cv2.imshow("video:",frame)
    else:
        break
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release() # videoyu serbest bırakıyoruz,videoyu almayı bırakıyoruz
cv2.destroyAllWindows()
