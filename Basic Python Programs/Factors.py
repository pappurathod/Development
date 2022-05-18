'''
@Author: Pappu Rathod
@Date: 16/05/2022
@Last Modified by: Pappu Rathod
@Title: -> Computes the prime factorization of N.
'''

num = int(input("Enter the number : "))
print("Prime Factors of",num, end=" is : ")
for i in range(1,num+1):
    if num%i == 0:  # check Factor or not
        count = 0
        for j in range(1,i+1):  # check prime or not from factors
            if i%j == 0:
                count += 1
        if (count == 2):
            print(i,end=", ")