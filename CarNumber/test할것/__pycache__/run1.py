
from itertools import count
from multiprocessing.sharedctypes import Value
import re

from run import Result

#num = "1이359부7846"
num = "1178호4459이1"
print("==========================")
print("입력된 정보: ", num) # 입력된 번호판 값
print("==========================")


def Confirm_location(data):
    
    Value = num.find(data) # 글자위치 찾기
    print(Value)

    data1 = num[Value -3]
    data2 = num[Value -2]
    data3 = num[Value -1]
    data4 = data
    data5 = num[Value +1]
    data6 = num[Value +2]
    data7 = num[Value +3]
    data8 = num[Value +4]

    if(data1 == 1):
        i = 1
        Result = data2 + data3 + data4 + data5 + data6 + data7 + data8
    else:
        i = 0
        Result = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8


    
    
    print("결과_test", Result)






for data in num:
    if(data.isalpha()): # 글자위치 확인
        
        # print(data)
        Confirm_location(data)
        if(Result == 0):
            confirmed_data = data

    
