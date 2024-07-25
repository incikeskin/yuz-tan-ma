import matplotlib.pyplot as plt
import cv2
img= cv2.imread("takim.jpg",0)
plt.figure(), plt.imshow(img, cmap= "gray"), plt.axis("off"), plt.show()

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

face_rect= face_cascade.detectMultiScale(img, minNeighbors=9)

for(x,y,w,h) in face_rect:
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,255), 10 )
plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off"), plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
