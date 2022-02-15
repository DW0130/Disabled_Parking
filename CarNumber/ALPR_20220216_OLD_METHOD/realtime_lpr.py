import cv2
import imutils
import numpy as np
import pytesseract
from PIL import Image
from picamera.array import PiRGBArray
from picamera import PiCamera
import smtplib

import matplotlib.pyplot as plt #added
import re




DEV_SHOW = True

def denoiseImage(targetIMG):  #added
    img_denoised = cv2.fastNlMeansDenoising(targetIMG,None,12,7,21)

    if DEV_SHOW:
        plt.figure(figsize=(12, 10))
        plt.imshow(img_denoised, cmap='gray')
        plt.show()
        print("[2]DENOISE DONE")

    return img_denoised

def adaptivThresholding(targetIMG):  #added
    #[ADAPTIVE THRESHOLDING]
    targetIMG = cv2.GaussianBlur(targetIMG, ksize=(5, 5), sigmaX=0)

    targetIMG = cv2.adaptiveThreshold(
        targetIMG, 
        maxValue=255.0, 
        adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        thresholdType=cv2.THRESH_BINARY_INV, 
        blockSize=15,  #blockSize=17, 
        C=10 #C=10
    )

    if DEV_SHOW:
        plt.figure(figsize=(12, 10))
        plt.imshow(targetIMG, cmap='gray')
        print("[4]ADAPTIVE THRESHOLDING")
        plt.show()
    return targetIMG

def convertIMGtoGrayscale(targetIMG, threshold_value): #added
    #[CONVERT IMG TO GRAYSCALE]
    img_gray = cv2.cvtColor(targetIMG, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(img_gray, threshold_value, 255, cv2.THRESH_BINARY_INV)[1]
    img_threshed = 255 - thresh
    return img_threshed

def textDivider(lprText):
    hangul = re.compile('[^ㄱ-ㅣ가-힣]+') # 한글과 띄어쓰기를 제외한 모든 글자
    # hangul = re.compile('[^ \u3131-\u3163\uac00-\ud7a3]+')  # 위와 동일
    koreanLetter = hangul.sub('', lprText) # 한글과 띄어쓰기를 제외한 모든 부분을 제거
    print("Korean: ")
    print(koreanLetter)

    numbers = hangul.findall(lprText) # 정규식에 일치되는 부분을 리스트 형태로 저장
    num1 = numbers[0]
    num2 = numbers[1]
    
    print("Number1: " + num1)
    print("Number2: " + num2)

    return koreanLetter, numbers


IMG_WIDTH = 640 #1280
IMG_HEIGHT = 480 #720
WHITELIST_LPR_CHARS = '0123456789가나다라마거너더러머버서어저고노도로모보소오조구누두루무부수우주바사아자배하허호'
EMAIL_ID = "pmhking84@gmail.com"
EMAIL_PASS = "jicqhjgwaxmfkrub"
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(EMAIL_ID, EMAIL_PASS) #jicqhjgwaxmfkrub
camera = PiCamera()
camera.color_effects = (128,128) #ADDED BLACK AND WHITE
camera.resolution = (IMG_WIDTH, IMG_HEIGHT)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(IMG_WIDTH, IMG_HEIGHT))
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        cv2.imshow("Frame", image)
        key = cv2.waitKey(1) & 0xFF
        rawCapture.truncate(0)
        if key == ord("s"):
             gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #convert to grey scale
             gray = cv2.bilateralFilter(gray, 11, 17, 17) #Blur to reduce noise
             edged = cv2.Canny(gray, 30, 200) #Perform Edge detection
             cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE,              cv2.CHAIN_APPROX_SIMPLE)
             cnts = imutils.grab_contours(cnts)
             cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
             screenCnt = None
             for c in cnts:
                peri = cv2.arcLength(c, True)
                #approx = cv2.approxPolyDP(c, 0.018 * peri, True)
                approx = cv2.approxPolyDP(c, 0.018 * peri, True)
                if len(approx) == 4:
                  screenCnt = approx
                  break
             if screenCnt is None:
               detected = 0
               print ("No contour detected")
             else:
               detected = 1
             if detected == 1:
               cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 3)
             mask = np.zeros(gray.shape,np.uint8)
             new_image = cv2.drawContours(mask,[screenCnt],0,255,-1,)
             new_image = cv2.bitwise_and(image,image,mask=mask)
             (x, y) = np.where(mask == 255)
             (topx, topy) = (np.min(x), np.min(y))
             (bottomx, bottomy) = (np.max(x), np.max(y))
             Cropped = gray[topx:bottomx+2, topy:bottomy+2]
             #Cropped = gray[topx:bottomx-1, topy:bottomy-1]
             resized = cv2.resize(Cropped, None, fx=1.5, fy=1.5) #ADDED
             #denoised = denoiseImage(resized)        #ADDED
             Cropped = adaptivThresholding(resized) #ADDED
             #ORIG CODE
             #text = pytesseract.image_to_string(Cropped, config='--psm 11')
             #text = pytesseract.image_to_string(Cropped, lang='kor', config='--psm 7 --oem 0')
             text = pytesseract.image_to_string(Cropped, \
                                                lang='kor', \
                                                config='--dpi 200  \
                                                        --psm 6  \
                                                        --oem 0  \
                                                        -c tessedit_char_whitelist=' + WHITELIST_LPR_CHARS)
                              
             #pytesseract.image_to_string(img_result, lang='kor', config='--psm 7 --oem 0')
             print("Detected Number is:",text)
             textDivider(text)
             server.sendmail(EMAIL_ID,EMAIL_ID,text.encode('utf-8'))
             cv2.imshow("Frame", image)
             cv2.imshow('Cropped',Cropped)
             cv2.waitKey(0)
             break
cv2.destroyAllWindows()
