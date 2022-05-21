'''
@Author: Pappu Rathod
@Date: 17/05/2022
@Last Modified by: Pappu Rathod
@Title: Given N distinct Coupon Numbers, how many random numbers do you
need to generate distinct coupon number? This program simulates this random
process.
'''

import random
def coupounNumber(couponNum):
    count=0
    for i in range(100):
        randomNum=random.randint(1,100)
        if(randomNum==couponNum):
            count+=1
    print("The Coupon Number ",couponNum," has repeated ",count," times")
couponNum =int(input("Enter a Coupon Number : "))
coupounNumber(couponNum)