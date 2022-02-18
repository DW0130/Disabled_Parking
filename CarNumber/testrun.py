'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime

import logging
from time import sleep
import traceback
import keyboard
'''

from datetime import time
import logging
from time import sleep
import traceback
from turtle import delay

import cv2
# n = 1
# m = 2
# today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# print(today)

# print(("Repeat: %s, %s Seconds"%(n, m)))
# check = ('%s_%s'%(n, m))
# print(check)


# Title = "What's News"
# Car_Num = "123가4567"

# text = "time: " + today + "\nplate_Number :" + Car_Num

# mail_data = Title + today + Car_Num
# print(today)
# print(Title)
# print(Car_Num)
# # 세션생성, 로그인
# s = smtplib.SMTP('smtp.gmail.com', 587)
# s.starttls()
# s.login('dw010130@gmail.com', 'psuujvginbzrexzs')


# # 제목, 본문 작성
# msg = MIMEMultipart()
# msg['Subject'] = '제목'
# # msg.attach(MIMEText("날짜 "+today+" \n번호"+Car_Num+""))
# msg.attach(MIMEText(text))

# # 메일 전송
# s.sendmail("dw010130@gmail.com", "dw010130@gmail.com", msg.as_string())
# s.quit()

# a = 0
# while True:
#     a = a + 1
#     print(str(a).zfill(4))

# logging.basicConfig(filename='./test1.log', level=logging.ERROR)

# def main():
#     print("TEST")

# if __name__ == '__main__':
#     try:
#         main()
#     except:
#         logging.error(traceback.format_exc())
'''
def run(repeat):
    data = "Repeat"
    try:
        print(repeat)
        if(repeat == 10):
            test()
    except:
        logging.debug("@@@---ERROR---@@@")
        logging.debug("+data+", repeat)
        logging.debug(traceback.format_exc())


logging.basicConfig(filename='./error.log', level=logging.ERROR)


n = 0
while True:
    run(n)
    n = n + 1
    delay(100)
    if(n == 11):
        break
'''
n = 0
while True:
    k = input('입력 : ')
    if k == '':
        break
    else:
        print(n)
        n = n + 1