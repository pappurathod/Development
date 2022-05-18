'''
@Author: Pappu Rathod
@Date: 14/05/2022
@Last Modified by: Pappu Rathod
@Title: Flip Coin and print percentage of Heads and Tails
'''

import random
tails=0
heads=0
print("Enter the number of times to Flip Coin : ")
num = input()
num= int(num)
if num > 0:
    for i in range(num):
        x = random.uniform(0, 1)
        if x<0.5:
            tails = tails+1
        else:
            heads = heads+1

    TailPer = (tails/num)*100
    HeadPer=(heads/num)*100
    print("Tails Percentage :",TailPer)
    print("Heads Percentage : ",HeadPer)
else:
    print("Enter Positive numbers")