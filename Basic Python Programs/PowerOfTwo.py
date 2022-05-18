'''
@Author: Pappu Rathod
@Date: 16/05/2022
@Last Modified by: Pappu Rathod
@Title: This program takes a command-line argument N and prints a table of the
powers of 2 that are less than or equal to 2^N.
'''

print("enter the number : ")
num = int(input())
if (num >= 0) and (num<31):
    for i in range(num):
        #power = pow(2,(i+1))
        power = 2 ** (i+1)
        print("2 ^",i+1,"=",power)
else:
    print("Overflow")