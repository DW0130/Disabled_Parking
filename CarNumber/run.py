
from itertools import count
from multiprocessing.sharedctypes import Value
import re

num = "1905다9437니1"

print(num) # 입력된 번호판 값

string = num
C_Num = re.findall('\w', string) # 문자열 -> 문자만 # re.findall('\w', string)  = 1개씩 분리

n = 0
exit = 0
while exit == 0:

    start_1 = 0 + n
    start_2 = 0 + n
    end_1 = 7 + n
    end_2 = 8 + n
    
    for data in C_Num:

        Check_data = 0
        if(data.isalpha()): # 기준이 되는 글자 검색

            Check_data = data
            data1 = C_Num[start_1:end_1]
            data2 = C_Num[start_2:end_2]

        if(Check_data != 0):
                
            i = 0
            for data in data1:
                if(data.isalpha()): # 7자리 번호, 기준글자와 중복방지
                    if (data != Check_data): i = 1

            if(i == 0): # 번호리스트에서 기준글자만 있는경우, 현 리스트에서 좌측 3번째 위치에 글자가 오도록 유도할것
                
                Value = start_1 + 2
                if Value == num.index(Check_data):
                    
                    print("==========================")
                    Result = ''.join(data1)
                    print(Result)
                    print("==========================")
                    exit = 1
                    

            i = 0
            for data in data2:
                if(data.isalpha()): # 8자리 번호, 기준글자와 중복방지
                    if (data != Check_data): i = 1

            if(i == 0): # 번호리스트에서 기준글자만 있는경우, 현 리스트에서 좌측 3번째 위치에 글자가 오도록 유도할것
                
                Value = start_2 + 3
                if Value == num.index(Check_data):
                    
                    print("==========================")
                    Result = ''.join(data2)
                    print(Result)
                    print("==========================")
                    exit = 1

        if(exit == 1): break
    
    n = n + 1
    if(exit == 1): break