'''
@Author: Pappu Rathod
@Date: 17/05/2022
@Last Modified by: Pappu Rathod
@Title: A library for reading in 2D arrays of integers, doubles, or booleans from
standard input and printing them out to standard output.
'''

def PrintArray(R, C):   # function defination
    arr = []

    for i in range(R):  # add in array
        tmp = []
        for j in range(C):
            tmp.append(input("Enter element : "))
        arr.append(tmp)

    for i in range(R):      # print array
        for j in range(C):
            print(arr[i][j], end=" ")
        print()

print("enter number of row : ")
row = int(input())
print("enter number of column : ")
col = int(input())

PrintArray(row, col)    # call function