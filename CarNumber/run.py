
import re
from typing import Tuple
from unittest import result

num = "자149우9815호1나"

print(num) # 입력된 번호판 값

string = num
#numbers = re.findall('\d+', string) # 문자열 -> 숫자만 
C_Num = re.findall('\w', string) # 문자열 -> 문자만 # re.findall('\w', string)  = 1개씩 분리

# print(numbers)
print(C_Num) # 번호판 쪼개기

    
for n in (1,2):
    
    if(n == 1):
        start_1 = 0
        start_2 = 1
        end_1 = 7
        end_2 = 8

    if(n == 2):
        start_1 = 1
        start_2 = 2
        end_1 = 8
        end_2 = 9

    for data in C_Num:
        if(data.isalpha()):
            data1 = C_Num[start_1:end_1]
            data2 = C_Num[start_2:end_2]

    print("=======================")
    print(n)
    print(data1)
    print(data2)
    print("=======================")    



# for data in C_Num:
#     if(data.isalpha()):
#         data_test = C_Num.index(data)
#         break

# print("=============================")
# print(data_test)

# print("=============================")


# data1 = num[0:7]
# data2 = num[0:8]
# print(data1)
# print(data2)

# for data in data1:
#     if(data.isalpha()):
#         Check_Data = data1.index(data)
#         break
# print(Check_Data)
# print("======================")
# if(Check_Data == 0):
#     data1 = num[1:8]
#     print(data1)
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




# n = 0
# while True:
#     n = n +1

#     for x in [1,2]:
        
#         if(n == 1):
#             start_1 = 0
#             start_2 = 1
#             end_1 = 7
#             end_2 = 9
#         if(n == 2):
#             start_1 = 1
#             start_2 = 2
#             end_1 = 8
#             end_2 = 9


#         if (x == 1):
#             data = C_Num[start_1:end_1]
#         if (x == 2):    
#             data = C_Num[start_2:end_2]

#     print(data)
