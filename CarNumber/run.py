
import re
from unittest import result

num = "자149우9815호1나"

print(num) # 입력된 번호판 값

string = num
#numbers = re.findall('\d+', string) # 문자열 -> 숫자만 
C_Num = re.findall('\w', string) # 문자열 -> 문자만 # re.findall('\w', string)  = 1개씩 분리

# print(numbers)
print(C_Num) # 번호판 쪼개기

data1 = num[0:7]
data2 = num[0:8]
print(data1)
print(data2)

for data in data1:
    if(data.isalpha()):
        Check_Data = data1.index(data)
        break
print(Check_Data)
print("======================")
if(Check_Data == 0):
    data1 = num[1:8]
    print(data1)
# for문사용하여 1번째 for문은 번호판이 7개 기준, 2번째 for문은 8개 기준으로 계산


# for data in C_Num:
#     if(data.isalpha()): # 문자가 있는지 판별
#         Check_Data = C_Num.index(data)
            
        
#         # data1 = data
        
#         break
# print(Check_Data)
# in_data = C_Num.index(data1) # 좌측에서 첫번째 글자 위치


# data2 = C_Num[in_data -1]
# data3 = C_Num[in_data -2]
# data4 = C_Num[in_data +1]
# data5 = C_Num[in_data +2]
# data6 = C_Num[in_data +3]
# data7 = C_Num[in_data +4]

# Car_Number = data3 + data2 + data1 + data4 + data5 + data6 + data7

# print(Car_Number)