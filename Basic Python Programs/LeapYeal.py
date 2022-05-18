'''
@Author: Pappu Rathod
@Date: 16/05/2022
@Last Modified by: Pappu Rathod
@Title: Leap Year
'''


print("Enter the Year : ")
year = int(input())
if (year > 999) and (year < 10000):
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        print(year,": is Leap Year")
    else:
        print(year,": is Not the Leap Year")
else:
    print("Invalid Year")