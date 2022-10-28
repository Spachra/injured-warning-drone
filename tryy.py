import cv2


img = cv2.imread('1.png',cv2.IMREAD_GRAYSCALE) #เปิดอ่านรูป

cv2.imshow('image',img) #โชวภาพมาแสดง image เขียนบนหัวตอนเปิด
cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imwrite('img2.png',img)



#จะแสดงภาพ line 257 หลังโค้ดส่ง line
            cv2.imshow('image',im0) #โชวภาพมาแสดง image เขียนบนหัวตอนเปิด
            cv2.waitKey(0)
            #จบโค้ดแสดงภาพ


print('Type of d = ', type(d))

\\Type of d =  <class 'list'>
