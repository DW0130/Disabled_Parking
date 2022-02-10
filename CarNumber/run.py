

# 1. 인식된 번호를 좌측에서부터 7자리,8자리를 찾기
# 2. 번호의 기준이 되는 글자 찾기
# 3. 인식된 번호에서 기준이된 글자를 제외한 글자가 나오는지 확인후 기준이된 번호만 있다면 다음진행 아니면 다시 찾기
# 4. 기준이된 글자가 7자리번호의 글자위치인지, 8자리번호의 글자위치인지 확인
# 5. 결과값 출력

######## 함수사용

from itertools import count
from multiprocessing.sharedctypes import Value
import re
from tracemalloc import start

num = "1145가7711" #45가7711
#num = "1이305다9437나1" #305다9437
#num = "경기45바4456"
print("==========================")
print("입력된 정보: ", num) # 입력된 번호판 값
print("==========================")

string = num
C_Num = re.findall('\w', string) # 문자열 -> 문자만 # re.findall('\w', string)  = 1개씩 분리


def Num_list(): # 7자리의 번호의 좌측 첫번째 위치의 값이 숫자일 경우 실행
    i = 0
    for data in data2:
        if(data.isalpha()): # 8자리 번호, 기준글자와 중복방지
            if (data != Check_data): i = 1

    if(i == 0): # 번호리스트에서 기준글자만 있는경우, 현 리스트에서 좌측 3번째 위치에 글자가 오도록 유도할것
        
        Value = start_2 + 3
        if Value == num.index(Check_data):
            
            print("==========================")
            Result = ''.join(data2)
            print("8자리")
            print("결과 : ", Result)
            print("==========================")
            exit = 1


def DEV_SHOW_LOG():

    print("")


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
            print(n, "번 반복")
            print(Check_data)
            data1 = num[start_1:end_1]
            data2 = num[start_2:end_2]

            

        if(Check_data != 0):
                
            i = 0
            for data in data1:
                
                if(data.isalpha()): # 7자리 번호, 기준글자와 중복방지
                    
                    if (data != Check_data): i = 1


            val = start_1 - 1


            

            if(i == 0): # 번호리스트에서 기준글자만 있는경우, 현 리스트에서 좌측 3번째 위치에 글자가 오도록 유도할것
                
                Value = start_1 + 2
                val1 = start - 1
                # val = 
                print(Value)
                print(num.find(Check_data))
                if Value == num.find(Check_data):

                    
                    print("==========================")
                    Result = ''.join(data1)
                    print("7자리")
                    print("결과 : ", Result)
                    print("==========================")
                    exit = 1
                    

        if(exit == 1): break
    
    n = n + 1
    if(exit == 1): break