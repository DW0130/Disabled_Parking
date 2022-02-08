import pymysql

conn = None
cur = None


data1 = ""
data2 = ""
data3 = ""
data4 = ""

row  = None

conn = pymysql.connect(host='192.168.*.***',user='*****',password='*********', db='Sensor',charset='utf8') 
cur = conn.cursor()

def DBselect(data):
    cur.execute('select * from ACTION_PATTERN') #DB 데이터 조회
    dbdata[4] = [""]
    while (True):
        row = cur.fetchone()
        if row == None:
            break
        dbdata[0] = row[0]
        dbdata[1] = row[1]
        dbdata[2] = row[2]
        dbdata[3] = row[3] #조회 데이터 배열 저장
        if dbdata[1] == data[1]:#조회한 데이터가 받은 데이터와 같을경우
            dbdata = data #리턴 변수에 DB값을넣고 함수 중단
            break
    return dbdata

def action(setdata):
    DBdata[] = DBselect(setdata)
    if DBdata[0] == setdata[0]: #입력 데이터 DB값과 일치
        INTRUSION(setdata,DBdata) #인자 출력

def speedsize(speed,size,movedata):
    global INTRUSIONs
    if float(speed) > 0.1 and float(size) > 0.75: #속도와 크기가 칩입자로 판단되었을때
        action(movedata) #DB비교 함수에 인자 전달
        INTRUSIONs = 1 #1차 감지 신호 송출

def Sensor():
    global RADARSENSOR 
    global THRML_INSNS 
    global INTRUSIONs
    radarSensor[] = RADARSENSOR 
    thrmlInsns[] = THRML_INSNS #센서들로부터 감지 정보를 받아옴

    if radarSensor[0] != null and thrmlInsns[0] == null : #만약 레이더만 감지가 됬을시
        speedsize(radarSensor[0],radarSensor[1],radarSensor[3])##속도와 크기 비교 함수로 인자 전달
    elif radarSensor[0] == null and thrmlInsns[0] != null and INTRUSIONs != 1: #적외선만 감지됬을시
        speedsize(thrmlInsns[0],thrmlInsns[1],thrmlInsns[3]) 
    else radarSensor[0] == null and thrmlInsns[0] == null: # 둘다 감지됬을시
            detadt()
            INTRUSIONs = 1