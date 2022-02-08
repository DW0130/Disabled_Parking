import pymysql
import os
import time
import datetime
from datetime import date , datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

DBIP = '192.168.0.43'
NonText = 1

class Target:
    watchDir = "/home/pi/Desktop/Dnet_WEB_/Dnet_Photo-management/Web_server2/static/text"
    if NonText == 1:
            watchDir = "/home/pi/Desktop/Dnet_Photo_New/static/image"
    #watchDir에 감시하려는 디렉토리를 명시한다.

    def __init__(self):
        self.observer = Observer()   #observer객체를 만듦

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchDir, 
                                                       recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
            print("Error")
            self.observer.join()

class Handler(FileSystemEventHandler):
#FileSystemEventHandler 클래스를 상속받음.
#아래 핸들러들을 오버라이드 함

    #파일, 디렉터리가 move 되거나 rename 되면 실행
    def on_moved(self, event):
        print(event)

    def on_created(self, event): #파일, 디렉터리가 생성되면 실행
        print(event)
        print("-------event-------")
        if os.path.isfile(event.src_path):

            mydb = pymysql.connect(host=DBIP,user='root',password='1234',db='speeddb',charset='utf8')
            mycursor = mydb.cursor()

            mydb2 = pymysql.connect(host=DBIP,user='root',password='1234',db='speeddb',charset='utf8')
            mycursor2 = mydb2.cursor()

            FILE = (event.src_path)
            file = FILE
            speedTemp = FILE.split('[')
            Teamparr = FILE.split('/')
            timeTemp = Teamparr[9].split('[')

            speed = speedTemp[1].replace(']','').replace('KPH','')
            locat = Teamparr[7]
            date = Teamparr[8]
            time = timeTemp[0].replace('Time_','')
            dateString = date + ' ' + time
            dateFormatter = "%Y-%m-%d %H%M%S"
            datetimes =  datetime.strptime(dateString, dateFormatter)

            print(file)
            print(speed)
            print(locat)
            print(datetimes)


            sql = "INSERT IGNORE INTO CarDB (LCT,SPD,PHT,TME) VALUES (%s, %s, %s, %s)"
            sql2 = "INSERT IGNORE INTO CarDB_2 (LCT,SPD,PHT,TME) VALUES (%s, %s, %s, %s)"

            val = (locat,int(speed),file,datetimes)

            mycursor.execute(sql, val)
            mydb.commit()

            mycursor.execute(sql2, val)

            mydb.commit()



    def on_deleted(self, event): #파일, 디렉터리가 삭제되면 실행
        print(event)

    def on_modified(self, event): #파일, 디렉터리가 수정되면 실행
        print(event)

        
if __name__ == '__main__': #본 파일에서 실행될 때만 실행되도록 함
    w = Target()
    w.run()
