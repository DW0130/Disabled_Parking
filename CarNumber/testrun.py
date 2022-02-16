import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime


today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(today)



Title = "What's News"
Car_Num = "123가4567"

text = "time: " + today + "\nplate_Number :" + Car_Num

mail_data = Title + today + Car_Num
print(today)
print(Title)
print(Car_Num)
# 세션생성, 로그인
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login('dw010130@gmail.com', 'psuujvginbzrexzs')


# 제목, 본문 작성
msg = MIMEMultipart()
msg['Subject'] = '제목'
# msg.attach(MIMEText("날짜 "+today+" \n번호"+Car_Num+""))
msg.attach(MIMEText(text))

# 메일 전송
s.sendmail("dw010130@gmail.com", "dw010130@gmail.com", msg.as_string())
s.quit()