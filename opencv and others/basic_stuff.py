import  cv2
import numpy as np

#resim
resim = cv2.imread("5.jpg",0)#// önemli resmi okumak için kullan
cv2.imshow("yazdır",resim)# resmi yazdırmak için kullan
cv2.imwrite("5_gri.jpg",resim)# yeni resim oluşturup kaydeder 
cv2.waitKey(0)#0 herhangi bir tuş demek
a = cv2.waitKey(0)# ile a nın hangi tuşun ascii değeerini aldığını biliriz 
cv2.destroyAllWindows()

#video

yakala = cv2.videoCapture(0)# 0 pcnin kamerası
while 1:#video olduğundan  döngü ile almak gerekir
    değer, kare= yakala.read()
    cv2.imshow("ben",kare)
    a =cv2.waitkey(0)
    if a ==27:
        break

yakala.release()
cv2.destroyAllWindows()
