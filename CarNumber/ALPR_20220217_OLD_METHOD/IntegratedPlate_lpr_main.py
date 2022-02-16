# _*_ Encoding:UTF-8 _*_#

#python -m cProfile -s time file.py
import time

import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt
import pytesseract
import os
import imutils
import smtplib
import matplotlib.pyplot as plt #added
import re
from PIL import Image
from picamera.array import PiRGBArray
from picamera import PiCamera

#from datetime import date

from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



#[GENERAL SETTING INSTANCES]
SW_NAME = 'LPR'
VERSION = '220216_00'
DEBUG = True #False #make it True to check logs
#DEV_ALL = True
DEV_ALL = False

DEV_SHOW_LOG = False
DEV_SHOW_LOG_DETAILED = False
DEV_SHOW_IMG = False
DEV_SHOW_TIME = True

if DEV_ALL:
    DEV_SHOW_LOG = True
    DEV_SHOW_LOG_DETAILED = True
    DEV_SHOW_IMG = True
    DEV_SHOW_TIME = True
    
#[PI CAM SETTING INSTANCES]
IMG_WIDTH = 1280
IMG_HEIGHT = 720
camera = PiCamera()
camera.color_effects = (128,128) #ADDED BLACK AND WHITE
camera.resolution = (IMG_WIDTH, IMG_HEIGHT)
camera.framerate = 30
FILE_IMG_PATH = ''

#[EMAIL SETTIN INSTANCESG]
#EMAIL_ID = "pmhking84@gmail.com"
#EMAIL_PASS = "jicqhjgwaxmfkrub"

EMAIL_ID = "dw010130@gmail.com"
EMAIL_PASS = "psuujvginbzrexzs"

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(EMAIL_ID, EMAIL_PASS) #jicqhjgwaxmfkrub

#[TESSERACT SETTING INSTANCES]
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
WHITELIST_LPR_CHARS = '0123456789가나다라마거너더러머버서어저고노도로모보소오조구누두루무부수우주바사아자배하허호'



#[LPR SETTING INSTANCES]
NUM_OF_TEXT_LENGTH_TO_DETECT = 4 #DETECT ONLY LAST N DIGITS
#NewPlate size: 520X110㎜
#OldPlate size: 335X170㎜

#[TEXT FILE PATH]
TEXT_FILE_PATH = '/home/pi/Desktop/Dnet_WEB_/Dnet_Photo-management/Web_server2/static/text/'
TEXT_FILE_NAME = 'PlateNumberList.txt'
ENLARGE_IMG_RATIO = 100
MIN_PLATE_RATIO = 150/80 #Good with numbers 4
MAX_PLATE_RATIO = 520/110 #Good with numbers 4.35
global MAX_DIAG_MULTIPLYER, MAX_ANGLE_DIFF, MAX_AREA_DIFF, MAX_WIDTH_DIFF, MAX_HEIGHT_DIFF
global MIN_N_MATCHED, MIN_AREA, MAX_AREA, MIN_WIDTH, MAX_WIDTH, MIN_HEIGHT, MAX_HEIGHT
global MIN_RATIO, MAX_RATIO, PLATE_WIDTH_PADDING, PLATE_HEIGHT_PADDING
global height, width, channel
global result_chars
global possible_contours


def setCamSetting(cam_location):
    global MAX_DIAG_MULTIPLYER, MAX_ANGLE_DIFF, MAX_AREA_DIFF, MAX_WIDTH_DIFF, MAX_HEIGHT_DIFF
    global MIN_N_MATCHED, MIN_AREA, MAX_AREA, MIN_WIDTH, MAX_WIDTH, MIN_HEIGHT, MAX_HEIGHT
    global MIN_RATIO, MAX_RATIO, PLATE_WIDTH_PADDING, PLATE_HEIGHT_PADDING

    #[CHANGE SETTING FOR EACH CAM LOCATION]
    if cam_location == 'A':
        if DEV_SHOW_LOG:
            print('CAM Location A')
        MAX_DIAG_MULTIPLYER = 5
        MAX_ANGLE_DIFF = 10.0
        MAX_AREA_DIFF = 0.5 #0.7
        MAX_WIDTH_DIFF, MAX_HEIGHT_DIFF = 0.8, 0.2
        MIN_N_MATCHED = 4
        MIN_AREA, MAX_AREA  = 400, 2000
        MIN_WIDTH, MAX_WIDTH = 10, 40
        MIN_HEIGHT, MAX_HEIGHT = 30, 70
        MIN_RATIO, MAX_RATIO = 0.25, 0.61
        PLATE_WIDTH_PADDING, PLATE_HEIGHT_PADDING = 1.3, 1.58
    elif cam_location == 'B':
        if DEV_SHOW_LOG:
            print('CAM Location B')
        MAX_DIAG_MULTIPLYER = 5
        MAX_ANGLE_DIFF = 12.0
        MAX_AREA_DIFF = 0.7 #0.5
        MAX_WIDTH_DIFF, MAX_HEIGHT_DIFF = 0.8, 0.2
        MIN_N_MATCHED = 4
        MIN_AREA, MAX_AREA  = 300, 2900
        MIN_WIDTH, MAX_WIDTH = 10, 40
        MIN_HEIGHT, MAX_HEIGHT = 20, 90
        MIN_RATIO, MAX_RATIO = 0.19, 0.61
        PLATE_WIDTH_PADDING, PLATE_HEIGHT_PADDING = 1.3, 1.58
    elif cam_location == 'C':
        if DEV_SHOW_LOG:
            print('CAM Location C')
        MAX_DIAG_MULTIPLYER = 5
        MAX_ANGLE_DIFF = 12.0
        MAX_AREA_DIFF = 0.7 #0.5
        MAX_WIDTH_DIFF, MAX_HEIGHT_DIFF = 0.8, 0.2
        MIN_N_MATCHED = 4
        MIN_AREA, MAX_AREA  = 200, 3000
        MIN_WIDTH, MAX_WIDTH = 10, 45
        MIN_HEIGHT, MAX_HEIGHT = 24, 80
        MIN_RATIO, MAX_RATIO = 0.19, 0.61
        PLATE_WIDTH_PADDING, PLATE_HEIGHT_PADDING = 1.3, 1.58
    elif cam_location == 'D':
        if DEV_SHOW_LOG:
            print('CAM Location D')
        MAX_DIAG_MULTIPLYER = 5
        MAX_ANGLE_DIFF = 12.0
        MAX_AREA_DIFF = 0.5 #0.5
        MAX_WIDTH_DIFF, MAX_HEIGHT_DIFF = 0.8, 0.2
        MIN_N_MATCHED = 4
        MIN_AREA, MAX_AREA  = 350, 2200
        MIN_WIDTH, MAX_WIDTH = 10, 40
        MIN_HEIGHT, MAX_HEIGHT = 26, 60
        MIN_RATIO, MAX_RATIO = 0.19, 0.61
        PLATE_WIDTH_PADDING, PLATE_HEIGHT_PADDING = 1.3, 1.58
    elif cam_location == 'E':
        if DEV_SHOW_LOG:
            print('CAM Location E')
        MAX_DIAG_MULTIPLYER = 5
        MAX_ANGLE_DIFF = 12.0
        MAX_AREA_DIFF = 0.5 #0.5
        MAX_WIDTH_DIFF, MAX_HEIGHT_DIFF = 0.8, 0.2
        MIN_N_MATCHED = 4
        MIN_AREA, MAX_AREA  = 410, 4500
        MIN_WIDTH, MAX_WIDTH = 10, 52
        MIN_HEIGHT, MAX_HEIGHT = 26, 94
        MIN_RATIO, MAX_RATIO = 0.19, 0.70
        PLATE_WIDTH_PADDING, PLATE_HEIGHT_PADDING = 1.3, 1.58
    elif cam_location == 'F':
        if DEV_SHOW_LOG:
            print('CAM Location F')
        MAX_DIAG_MULTIPLYER = 5
        MAX_ANGLE_DIFF = 12.0
        MAX_AREA_DIFF = 0.5 #0.5
        MAX_WIDTH_DIFF, MAX_HEIGHT_DIFF = 0.8, 0.2
        MIN_N_MATCHED = 4
        MIN_AREA, MAX_AREA  = 500, 1400
        MIN_WIDTH, MAX_WIDTH = 10, 30
        MIN_HEIGHT, MAX_HEIGHT = 30, 60
        MIN_RATIO, MAX_RATIO = 0.19, 0.70
        PLATE_WIDTH_PADDING, PLATE_HEIGHT_PADDING = 1.3, 1.58
    else:
        if DEV_SHOW_LOG:
            print('CAM Location Unknown')
        MAX_DIAG_MULTIPLYER = 5
        MAX_ANGLE_DIFF = 12.0
        MAX_AREA_DIFF = 0.5 #0.5
        MAX_WIDTH_DIFF, MAX_HEIGHT_DIFF = 0.8, 0.2
        MIN_N_MATCHED = 4
        MIN_AREA, MAX_AREA  = 400, 40000
        MIN_WIDTH, MAX_WIDTH = 10, 100
        MIN_HEIGHT, MAX_HEIGHT = 40, 400
        MIN_RATIO, MAX_RATIO = 0.19, 0.70
        PLATE_WIDTH_PADDING, PLATE_HEIGHT_PADDING = 1.3, 1.58
#HEIGHT 740-680 = 60
#WIDTH  1274-1243 = 31
#plate_height:526 plate_width:113 plate ratio:4.654867256637168

def sendEmail(licensePlateNumber, capturedImg, today, Car_Num, img_data):
    img_path = saveCapturedImage(capturedImg)
    img_path2 = saveCapturedImage2(img_data)
    #server.sendmail(EMAIL_ID, EMAIL_ID, licensePlateNumber.encode('utf-8'))
    
    text = "Time: " + today + "\nOriginal :" + licensePlateNumber + "\nReformatted :" + Car_Num
    
    subject = "What's News"              # Subject
    msg = MIMEMultipart()  
    msg['Subject'] = subject
    msg.attach(MIMEText(text))


    part = MIMEBase('application', "octet-stream")  
    part.set_payload(open(img_path, "rb").read())  
    encoders.encode_base64(part)  
    part.add_header('Content-Disposition', 'attachment; filename="image1.jpg"')   # File name and
    msg.attach(part)
    
    part = MIMEBase('application', "octet-stream")  
    part.set_payload(open(img_path2, "rb").read())  
    encoders.encode_base64(part)  
    part.add_header('Content-Disposition', 'attachment; filename="image2.jpg"')   # File name and
    msg.attach(part)

    server.sendmail(EMAIL_ID, EMAIL_ID, msg.as_string())
    server.quit()

    

def captureImageFromPiCam():
    global IMG_WIDTH
    global IMG_HEIGHT
    rawCapture = PiRGBArray(camera, size=(IMG_WIDTH, IMG_HEIGHT))
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array

        # NO_SHOW_VIDEO
        
        # cv2.imshow("Frame", image)
        # key = cv2.waitKey(1) & 0xFF
        # rawCapture.truncate(0)
        return image
    '''
        if key == ord("s"):
            return image
    '''

def saveCapturedImage(img):
    full_path = FILE_IMG_PATH + 'tmp_image.jpg'
    result = cv2.imwrite(full_path, img)
    if result:
        if DEV_SHOW_LOG:
            print('File saved successfully')
            return full_path
    else:
        if DEV_SHOW_LOG:
            print('Error in saving file')
            

def saveCapturedImage2(img):
    full_path = FILE_IMG_PATH + 'tmp_image2.jpg'
    result = cv2.imwrite(full_path, img)
    if result:
        if DEV_SHOW_LOG:
            print('File saved successfully')
            return full_path
    else:
        if DEV_SHOW_LOG:
            print('Error in saving file')

   
def saveCapturedImage3(img):
    full_path = FILE_IMG_PATH + 'tmp_image3.jpg'
    result = cv2.imwrite(full_path, img)
    if result:
        if DEV_SHOW_LOG:
            print('File saved successfully')
            return full_path
    else:
        if DEV_SHOW_LOG:
            print('Error in saving file')


def showSWVersion():
    print('{0}: Ver. {1}'.format(SW_NAME, VERSION))


def recordLicensePlateNumber(plateNum):
    global NUM_OF_TEXT_LENGTH_TO_DETECT
    funcName = 'recordLicensePlateNumber'
    today = str(date.today())
    
    if os.path.exists(imgFilePath):
        writeMode = 'a' #APPEND DATA IF THE FILE EXISTS        
    else:
        writeMode = 'w' #CREATE FILE IF THE FILE DOES NOT EXIST
        if DEV_SHOW_LOG:
            print("[DEBUG] {0}: {1}".format(funcName, '[NEW] No File Found. Create LPR Text File'))

    file_in_pi = open(TEXT_FILE_PATH + today + '.txt', writeMode)
    output = imgFilePath + ':' + plateNum + ':' + plateNum[-NUM_OF_TEXT_LENGTH_TO_DETECT:]

    file_in_pi.write(output)
    file_in_pi.write('\n')
    if DEV_SHOW_LOG:
        print("[DEBUG] {0}".format(output))

    file_in_pi.close()

def showResult(src, num):
    plt.figure(figsize=(12, 10))
    plt.imshow(src, cmap='gray')
    plt.show()
    print("[ {0} ]".format(num))

def debugLogger(funcName, contents):
    if DEV_SHOW_LOG:
        print("[DEBUG] {0}: {1}".format(funcName, contents))       

def imageThreshBasedOnBrightness(img):
    #[GET BRIGHTNESS OF THE IMAGE]
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hue, sat, val = cv2.split(hsv)           #brightness = np.median(val) #np.mean(val)
    brightness = np.around(np.mean(val), 3)
    std = np.around(np.std(val), 3)
    print('brightness: {0} / STD: {1}'.format(brightness, std))
    threshold_val = 255-(brightness+std)
    print('threshold_val: {0}'.format(threshold_val))
    return threshold_val

def imageThreshBasedOnBrightnessForNight(img):
    NightVision = 60
    #[GET BRIGHTNESS OF THE IMAGE]
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hue, sat, val = cv2.split(hsv)           #brightness = np.median(val) #np.mean(val)
    brightness_mean = np.around(np.mean(val), 3)
    brightness_median = np.around(np.median(val), 3)
    
    std = np.around(np.std(val), 3)
    
    print('brightness_mean: {0} /  brightness_median: {1} / std: {2}'.format(brightness_mean, brightness_median, std))

    if brightness_mean < 100:
        threshold_val = brightness_mean * 2 - brightness_median + std  #good for nighttime
    else:
        threshold_val = brightness_mean * 2 - brightness_median - std
    
    print('threshold_val: {0}'.format(threshold_val))

    return threshold_val

def denoiseImage(targetIMG):
    img_denoised = cv2.fastNlMeansDenoising(targetIMG,None,12,7,21)
    if DEV_SHOW_IMG:
        plt.figure(figsize=(12, 10))
        plt.imshow(img_denoised, cmap='gray')
        plt.show()
        print("[2]DENOISE DONE")

    return img_denoised
    
def enlargeImage(targetIMG):
    global height, width, channel
    #[Enlarge image size]
    scale_percent = 150 # percent of original size
    width = int(targetIMG.shape[1] * scale_percent / ENLARGE_IMG_RATIO)
    height = int(targetIMG.shape[0] * scale_percent / ENLARGE_IMG_RATIO)
    dim = (width, height)
    img_enlarged = cv2.resize(targetIMG, dim, interpolation = cv2.INTER_AREA)
    height, width, channel = img_enlarged.shape
    return img_enlarged

def convertIMGtoGrayscale(targetIMG, threshold_value):
    #[CONVERT IMG TO GRAYSCALE]
    img_gray = cv2.cvtColor(targetIMG, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(img_gray, threshold_value, 255, cv2.THRESH_BINARY_INV)[1]
    img_threshed = 255 - thresh
    return img_threshed

def maximizeContrast(targetIMG):
    #[MAXIMIZE CONTRAST]
    structuringElement = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    imgTopHat = cv2.morphologyEx(targetIMG, cv2.MORPH_TOPHAT, structuringElement)
    imgBlackHat = cv2.morphologyEx(targetIMG, cv2.MORPH_BLACKHAT, structuringElement)
    imgGrayscalePlusTopHat = cv2.add(targetIMG, imgTopHat)
    targetIMG = cv2.subtract(imgGrayscalePlusTopHat, imgBlackHat)

    if DEV_SHOW_IMG:
        plt.figure(figsize=(12, 10))
        plt.imshow(targetIMG, cmap='gray')
        print("[3]MAXIMIZE CONTRAST")
        plt.show()
        
    return targetIMG

def adaptivThresholding(targetIMG):
    #[ADAPTIVE THRESHOLDING]
    targetIMG = cv2.GaussianBlur(targetIMG, ksize=(5, 5), sigmaX=0)

    targetIMG = cv2.adaptiveThreshold(
        targetIMG, 
        maxValue=255.0, 
        adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        thresholdType=cv2.THRESH_BINARY_INV, 
        blockSize=17, 
        C=10
    )

    if DEV_SHOW_IMG:
        plt.figure(figsize=(12, 10))
        plt.imshow(targetIMG, cmap='gray')
        print("[4]ADAPTIVE THRESHOLDING")
        plt.show()
    return targetIMG

def findContours(targetIMG):
    #[FIND CONTOURS]
    contours, _ = cv2.findContours(
    #cnts, contours, _ = cv2.findContours(
    #_, contours, _ = cv2.findContours(
        targetIMG, 
        mode=cv2.RETR_LIST, 
        method=cv2.CHAIN_APPROX_SIMPLE
    )
    tmp_result = np.zeros((height, width, channel), dtype=np.uint8)
    cv2.drawContours(tmp_result, contours=contours, contourIdx=-1, color=(255, 255, 255))

    if DEV_SHOW_IMG:
        plt.figure(figsize=(12, 10))
        plt.imshow(tmp_result)
        print("[5]FIND CONTOURS")
        plt.show()
    return tmp_result, contours

def prepareData(tmp_result, contours):
    #[PREPARE DATA]
    tmp_result = np.zeros((height, width, channel), dtype=np.uint8)
    contours_dict = []

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(tmp_result, pt1=(x, y), pt2=(x+w, y+h), color=(255, 255, 255), thickness=2)
    
        # insert to dict
        contours_dict.append({
            'contour': contour,
            'x': x,
            'y': y,
            'w': w,
            'h': h,
            'cx': x + (w / 2),
            'cy': y + (h / 2)
        })
    if DEV_SHOW_IMG:
        plt.figure(figsize=(12, 10))
        plt.imshow(tmp_result, cmap='gray')
        print("[6]PREPARE DATA")
        plt.show()
    return contours_dict


def selectCandidates(tmp_result, contours_dict):
    #[SELECT CANDIDATES BY CHAR SIZE]
    possible_contours = []

    cnt = 0
    for d in contours_dict:
        area = d['w'] * d['h']
        ratio = d['w'] / d['h']
        if DEV_SHOW_LOG_DETAILED:
            print('MIN_AREA: {0} MAX_AREA: {1} area: {2} width: {3} / height: {4} / ratio: {5} / '.format(MIN_AREA, MAX_AREA, area, d['w'], d['h'], ratio))

        if MIN_AREA < area < MAX_AREA \
        and MIN_WIDTH < d['w'] < MAX_WIDTH \
        and MIN_HEIGHT < d['h'] < MAX_HEIGHT \
        and MIN_RATIO < ratio < MAX_RATIO:
            d['idx'] = cnt
            cnt += 1
            possible_contours.append(d)
            if DEV_SHOW_LOG_DETAILED:
                print('MIN_AREA: {0} MAX_AREA: {1} area: {2} width: {3} / height: {4} / ratio: {5} / '.format(MIN_AREA, MAX_AREA, area, d['w'], d['h'], ratio))
    if DEV_SHOW_IMG:
        plt.figure(figsize=(12, 10))
        plt.imshow(tmp_result, cmap='gray')
        print("[7]SELECT CANDIDATES BY CHAR SIZE")
        plt.show()

    return possible_contours


def visualizePossibleContours(possible_contours):
    #[VISUALIZE POSSIBLE CONTOURS]
    tmp_result = np.zeros((height, width, channel), dtype=np.uint8)

    for d in possible_contours:
        cv2.drawContours(tmp_result, d['contour'], -1, (255, 255, 255))
        cv2.rectangle(tmp_result, \
                      pt1=(d['x'], d['y']), \
                      pt2=(d['x']+d['w'], d['y']+d['h']), \
                      color=(255, 255, 255), \
                      thickness=2)

    if DEV_SHOW_IMG:
        plt.figure(figsize=(12, 10))
        plt.imshow(tmp_result, cmap='gray')
        print("[8]VISUALIZE POSSIBLE CONTOURS")
        plt.show()

#[SELECT CANDIDATES BY ARRANGEMENT OF CONTOURS]
def find_chars(contour_list):
    global possible_contours
    matched_result_idx = []
    
    for d1 in contour_list:
        matched_contours_idx = []
        for d2 in contour_list:
            if d1['idx'] == d2['idx']:
                continue

            dx = abs(d1['cx'] - d2['cx'])
            dy = abs(d1['cy'] - d2['cy'])

            diagonal_length1 = np.sqrt(d1['w'] ** 2 + d1['h'] ** 2)

            distance = np.linalg.norm(np.array([d1['cx'], d1['cy']]) - np.array([d2['cx'], d2['cy']]))
            if dx == 0:
                angle_diff = 90
            else:
                angle_diff = np.degrees(np.arctan(dy / dx))
            area_diff = abs(d1['w'] * d1['h'] - d2['w'] * d2['h']) / (d1['w'] * d1['h'])
            width_diff = abs(d1['w'] - d2['w']) / d1['w']
            height_diff = abs(d1['h'] - d2['h']) / d1['h']              
                
            if distance < diagonal_length1 * MAX_DIAG_MULTIPLYER \
            and angle_diff < MAX_ANGLE_DIFF and area_diff < MAX_AREA_DIFF \
            and width_diff < MAX_WIDTH_DIFF and height_diff < MAX_HEIGHT_DIFF:
                matched_contours_idx.append(d2['idx'])

        # append this contour
        matched_contours_idx.append(d1['idx'])

        if len(matched_contours_idx) < MIN_N_MATCHED:
            continue

        matched_result_idx.append(matched_contours_idx)

        unmatched_contour_idx = []
        for d4 in contour_list:
            if d4['idx'] not in matched_contours_idx:
                unmatched_contour_idx.append(d4['idx'])

        unmatched_contour = np.take(possible_contours, unmatched_contour_idx)
        
        # recursive
        recursive_contour_list = find_chars(unmatched_contour)
        
        for idx in recursive_contour_list:
            matched_result_idx.append(idx)

        break

    return matched_result_idx

#[COLLECT MATCHED RESULT]
def collectMatchedResult(result_idx, possible_contours):
    matched_result = []
    for idx_list in result_idx:
        matched_result.append(np.take(possible_contours, idx_list))

    return matched_result


def rotatePlateImages(matched_result, img_adapted):
    #[ROTATE PLATE IMAGES]
    plate_imgs = []
    plate_infos = []

    for i, matched_chars in enumerate(matched_result):
        sorted_chars = sorted(matched_chars, key=lambda x: x['cx'])

        plate_cx = (sorted_chars[0]['cx'] + sorted_chars[-1]['cx']) / 2
        plate_cy = (sorted_chars[0]['cy'] + sorted_chars[-1]['cy']) / 2
        plate_width = (sorted_chars[-1]['x'] + sorted_chars[-1]['w'] - sorted_chars[0]['x']) * PLATE_WIDTH_PADDING

        sum_height = 0
        for d in sorted_chars:
            sum_height += d['h']

        plate_height = int(sum_height / len(sorted_chars) * PLATE_HEIGHT_PADDING)
        
        triangle_height = sorted_chars[-1]['cy'] - sorted_chars[0]['cy']
        triangle_hypotenus = np.linalg.norm(
            np.array([sorted_chars[0]['cx'], sorted_chars[0]['cy']]) - 
            np.array([sorted_chars[-1]['cx'], sorted_chars[-1]['cy']])
        )
    
        if triangle_hypotenus != 0: #[DNET] SKIP TO NEXT INDEX IF triangle_hypotenus IS ZERO
            angle = np.degrees(np.arcsin(triangle_height / triangle_hypotenus))
            rotation_matrix = cv2.getRotationMatrix2D(center=(plate_cx, plate_cy), angle=angle, scale=1.0)
        else:
            continue

        img_rotated = cv2.warpAffine(img_adapted, M=rotation_matrix, dsize=(width, height))
    
        img_cropped = cv2.getRectSubPix(
            img_rotated, 
            patchSize=(int(plate_width), int(plate_height)), 
            center=(int(plate_cx), int(plate_cy))
        )
    
        if img_cropped.shape[1] / img_cropped.shape[0] < MIN_PLATE_RATIO \
           or img_cropped.shape[1] / img_cropped.shape[0] < MIN_PLATE_RATIO > MAX_PLATE_RATIO:
            continue
        if DEV_SHOW_LOG: print('plate_height:{0} plate_width:{1} plate ratio:{2}'.format(img_cropped.shape[1], img_cropped.shape[0], img_cropped.shape[1] / img_cropped.shape[0]))
        
        plate_imgs.append(img_cropped)
        plate_infos.append({
            'x': int(plate_cx - plate_width / 2),
            'y': int(plate_cy - plate_height / 2),
            'w': int(plate_width),
            'h': int(plate_height)
        })
        if DEV_SHOW_IMG:
            plt.subplot(len(matched_result), 1, i+1)
            plt.imshow(img_cropped, cmap='gray')
            plt.show()

    return plate_imgs


    #img_cropped
################################# 





def anotherThresholdToFindChars(plate_imgs):
    #def anotherThresholdToFindChars(plate_imgs, PATH_IMG):
    #[ANOTHER THRESHOLDING TO FIND CHARS]
    longest_idx, longest_text = -1, 0
    plate_chars = []

    for i, plate_img in enumerate(plate_imgs):
        digit_cnt=0
        #plate_img = cv2.resize(plate_img, dsize=(0, 0), fx=1.6, fy=1.6)
        #plate_img = cv2.resize(plate_img, dsize=(0, 0), fx=1.8, fy=1.8)
        _, plate_img = cv2.threshold(plate_img, \
                                     thresh=10.0, \
                                     maxval=255.0, \
                                     type=cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
        # find contours again (same as above)
        contours, _ = cv2.findContours(plate_img, \
        #_, contours, _ = cv2.findContours(plate_img, \
                                       mode=cv2.RETR_LIST, \
                                       method=cv2.CHAIN_APPROX_SIMPLE)
    
        plate_min_x, plate_min_y = plate_img.shape[1], plate_img.shape[0]
        plate_max_x, plate_max_y = 0, 0

        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
        
            area = w * h
            ratio = w / h
            
            if MAX_AREA > area > MIN_AREA \
            and MAX_WIDTH > w > MIN_WIDTH \
            and MAX_HEIGHT > h > MIN_HEIGHT \
            and MIN_RATIO < ratio < MAX_RATIO:
                if DEV_SHOW_LOG_DETAILED:
                    print('area:{0} width:{1} Height:{2} Ratio: {3}'.format(area, w, h, ratio))
            
                if x < plate_min_x:
                    plate_min_x = x
                if y < plate_min_y:
                    plate_min_y = y
                if x + w > plate_max_x:
                    plate_max_x = x + w
                if y + h > plate_max_y:
                    plate_max_y = y + h

        img_result = plate_img[plate_min_y:plate_max_y, plate_min_x:plate_max_x]
        #img_result = cv2.GaussianBlur(img_result, ksize=(1, 1), sigmaX=0)
        _, img_result = cv2.threshold(img_result, \
                                      thresh=1.0, \
                                      maxval=255.0, \
                                      type=cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        img_result = cv2.copyMakeBorder(img_result, \
                                        top=10, \
                                        bottom=10, \
                                        left=10, \
                                        right=10, \
                                        borderType=cv2.BORDER_CONSTANT, \
                                        value=(0,0,0))

        chars = pytesseract.image_to_string(img_result, \
                                            lang='kor', \
                                            config='--dpi 200  \
                                                    --psm 7  \
                                                    --oem 0  \
                                                    -c tessedit_char_whitelist=' + WHITELIST_LPR_CHARS)
                                                
        result_chars = ''
        has_digit = False
        for c in chars:                
            if ord('가') <= ord(c) <= ord('힣') or c.isdigit():
                if c.isdigit():
                    has_digit = True
                    digit_cnt = digit_cnt+1
                result_chars += c
        #FILTER THE BAD FORMAT RESULT
        if digit_cnt < 4:
            if DEV_SHOW_LOG:
                print("digit_cnt: {0}. Skip to next result".format(digit_cnt))
            continue
    
        result_len = len(result_chars)
        plate_chars.append(result_chars)

        if len(result_chars) < 4:
            result_chars = "0000"
        if DEV_SHOW_LOG:
            print('LPR: ' +result_chars)

        if result_len > 3 and result_len < 9: # IGNORE NUMBER IF OUT OF RANGE 7~9
            if DEV_SHOW_LOG:
                print("Result: {0} / Digit Count: {1} / Last 4 Digits: {2}".format(result_chars, digit_cnt, result_chars[-NUM_OF_TEXT_LENGTH_TO_DETECT:]))
            #recordLicensePlateNumber(result_chars)
            #recordLicensePlateNumber(PATH_IMG, result_chars)
        #else:
        #    if DEV_SHOW_LOG: recordLicensePlateNumber(PATH_IMG, "NO LICENSE DETECTED")
    
        if has_digit and len(result_chars) > longest_text:
            longest_idx = i
        if DEV_SHOW_IMG:
            plt.subplot(len(plate_imgs), 1, i+1)
            plt.imshow(img_result, cmap='gray')
            plt.show()

        return result_chars, img_result




        # img_result
    ######################################3

def isValidLP(result_chars):
    digit_cnt=0
    #for c in result_chars[-4:]:
    print(result_chars)
    for c in result_chars:
        if c.isdigit():
            digit_cnt = digit_cnt+1

    if digit_cnt < 4:
        return False

    return True


def findChar(lp):
    for idx, content in enumerate(lp):
        if not content.isdigit() and idx > 2:
            if DEV_SHOW_LOG:
                print('[findChar] FOUND Korean letter at [{0}] {1}'.format(idx, content))
            break
    return idx, content


def reformattingLP(result_chars):
    index, koreanChar = findChar(result_chars)
    if DEV_SHOW_LOG:
        print('[reformattingLP] FOUND Korean letter at [{0}/{1}] {2}'.format(index, len(result_chars), koreanChar))
        
    
def rerun():
    print('rerun')


def validateOldNum(num):

    for n in range(10):
        
        start = 0 + n
        end = 7 + n

        exit = 0
        Result = ''
        for data1 in num:

            Check_data = 0
            if(data1.isalpha()):
                Check_data = data1
                main_data = num[start:end]
                
                i = 0
                for data2 in main_data:
                    if(data2.isalpha()):
                        if(data2 != Check_data): i = 1

                Text_Val = start + 2
                if Text_Val == num.index(Check_data):
                    if (i == 0):

                        exit = 1
                        Result = main_data
            if(exit == 1): break
                
        if(exit == 1): break
    return Result, exit


def validateNewNum(num):

    for n in range(10):

        start = 0 + n
        end = 8 + n

        exit = 0
        Result = ''
        for data1 in num:

            Check_data = 0
            if(data1.isalpha()):
                Check_data = data1
                main_data = num[start:end]
                
                i = 0
                for data2 in main_data:
                    if(data2.isalpha()):
                        if(data2 != Check_data): i = 1
                if(i == 0):
                    Text_Val = start + 3
                    if Text_Val == num.index(Check_data):
                        
                        Result = main_data
                        exit = 1
            
            if(exit == 1): break
    
        if(exit == 1): break
    return Result, exit


def validateBusinessNum(num):

    for data3 in num:

        exit = 0
        Result = ''
        if(data3.isalpha()):
            location_data = num.find(data3)
            text1 = num[location_data]
            text2 = num[location_data +1]
            if(text1.isalpha() and text2.isalpha()):

                for n in range(10):
                    start = num.find(text1) + n      
                    end = start + 7
                    
                    for data1 in num:

                        Check_data = 0
                        if(data1.isalpha()):
                            Check_data = data1
                            main_data = num[start:end]
                            
                            i = 0
                            for data2 in main_data:
                                if(data2.isalpha()):
                                    if(data2 != Check_data): i = 1

                            Text_Val = start + 2
                            if Text_Val == num.index(Check_data):
                                if (i == 0):
                                    
                                    Result = text1 + text2 + main_data
                                    exit = 1
        
                        if(exit == 1): break
                
                    if(exit == 1): break
        if(exit == 1): break
    return Result, exit

def runtimeChecker(funcName, prevEndTime):
    if DEV_SHOW_TIME:
        print("[END TIME][%s]--- %s seconds ---" % (funcName, time.time() - prevEndTime))
        return time.time()
    else:
        return 0
    

def run():
    global result_chars
    global possible_contours
    #[ S T A R T ]=============================================================================================
    showSWVersion()
    plt.style.use('dark_background')
    #[READ INPUT IMG]
    #PATH_IMG = str(sys.argv[1]) #USE argv[1] TO READ ONLY FILEPATH
    #cam_location = PATH_IMG.split('/')[9] #get cam location from file path
    cam_location = 'TEST'
    #[LOAD IMAGE]
    #img_orig = readImage(PATH_IMG)
    img_orig = captureImageFromPiCam()
    
    #[SET UP CAMERAS]
    setCamSetting(cam_location)
    #[GET BRIGHTNESS AND RETURN THRESHOLD VALUE]
    #threshold_val = imageThreshBasedOnBrightness(img_orig
    threshold_val = imageThreshBasedOnBrightnessForNight(img_orig)
    prevFuncEndTime = start_time
    prevFuncEndTime = runtimeChecker("[imageThreshBasedOnBrightnessForNight]", prevFuncEndTime)
    #[DENOISE IMAGE]
    img_denoised = denoiseImage(img_orig)
    prevFuncEndTime = runtimeChecker("[denoiseImage]", prevFuncEndTime)
    #[ENLARGE IMAGE]
    img_enlarged = enlargeImage(img_denoised)
    img_threshed = convertIMGtoGrayscale(img_enlarged, threshold_val)
    #[MAXIMIZE CONTRAST]
    img_contrasted = maximizeContrast(img_threshed)
    #[ADAPTIVE THRESHOLDING]
    img_adapted = adaptivThresholding(img_contrasted)
    #[FIND CONTOURS]
    temp_result, contours = findContours(img_adapted)
    #[PREPARE DATA]
    contours_dict = prepareData(temp_result, contours)
    #[SELECT CANDIDATES BY CHAR SIZE]
    possible_contours = selectCandidates(temp_result, contours_dict)
    visualizePossibleContours(possible_contours)
    #[FIND CHARS FROM POSSIBLE CONTOURS
    result_idx = find_chars(possible_contours)
    matched_result = collectMatchedResult(result_idx, possible_contours)
    plate_imgs = rotatePlateImages(matched_result, img_adapted)
    #result_chars = anotherThresholdToFindChars(plate_imgs, PATH_IMG)
    #result_chars = anotherThresholdToFindChars(plate_imgs)
    data = anotherThresholdToFindChars(plate_imgs)


    img_data = data[1]
    Original_Num = data[0]
    
    
    today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')    
    # Result = ''
    Result = validateBusinessNum(Original_Num)
    if(Result[1] == 0): Result = validateNewNum(Original_Num)
    if(Result[1] == 0): Result = validateOldNum(Original_Num)
    
    final_result_chars = reformattingLP(Original_Num)
    print('[LP Found] Time: {0}'. format(today))
    print('[LP Found] Original: {0}'.format(Original_Num))
    print('[LP Found] Reformatted: {0}'.format(final_result_chars))
    print('[LP Found] Send Email to {0}'.format(EMAIL_ID))
    # sendEmail(Original_Num, img_orig, today, Result[0], img_data)


'''
start_time = time.time()
run()
tm = time.localtime(time.time() - start_time)
print("[END TIME]--- %s seconds ---" % tm.tm_sec)

'''

n = 0
while True:
    start_time = time.time()
    print("repeat :", n)
    run()
    n = n + 1
    tm = time.localtime(time.time() - start_time)
    print("--- %s seconds ---" % tm.tm_sec)

# exit()









'''
import cv2

img = cv2.imread("image.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (7, 7), 1.5)
gray = cv2.Canny(gray, 0, 50)
cv2.imshow("edges", gray)
cv2.waitKey();


import cv2

img = cv2.UMat(cv2.imread("image.jpg", cv2.IMREAD_COLOR))
imgUMat = cv2.UMat(img)

gray = cv2.cvtColor(imgUMat, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (7, 7), 1.5)
gray = cv2.Canny(gray, 0, 50)
cv2.imshow("edges", gray)
cv2.waitKey();

'''
