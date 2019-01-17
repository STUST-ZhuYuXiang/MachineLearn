import cv2

#設定一個變數im存入指定位置的圖片，並且顯示出來
im = cv2.imread("Lena.png")
#cv2.imshow("img_test", im)

#將圖片水平翻轉  im_h = cv2.flip(im, 1)

#將圖片上下翻轉  im_v = cv2.flip(im, 0)

#將圖片上下左右都翻轉
im_hv = cv2.flip(im, -1)
cv2.imshow("img_test", im_hv)

#按下任意鍵可將圖片關閉
cv2.waitKey(0)
cv2.destoryAllWindows()