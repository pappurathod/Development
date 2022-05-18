'''
@Author: Pappu Rathod
@Date: 16/05/2022
@Last Modified by: Pappu Rathod
@Title: Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N
'''

print("Enter the number : ")
num = int(input())
value = 0
if num != 0:
    for i in range(num):
        value = value + (1/(i + 1))
        if (i+1) != num:
            print('1/%d' % (i + 1), "+", end=" ")
        else:
            print('1/%d' % (i + 1))

    print("Nth Harmonic value : ", value)
else:
    print("Zero is not allow")
