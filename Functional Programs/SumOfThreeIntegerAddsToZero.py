'''
@Author: Pappu Rathod
@Date: 17/05/2022
@Last Modified by: Pappu Rathod
@Title: A program with cubic running time. Read in N integers and counts the
number of triples that sum to exactly 0.
'''

def findTriplets(arr,m):
    flag = 0
    for i in range(0,m):
        for j in range(i+1,m):
            for k in range(j+1,m):
                if (arr[i]+arr[j]+arr[k]==0):
                    print(arr[i],arr[j],arr[k])
                    flag = 1
    if (flag == 0):
        print("No Triplets found")

arr=[]
n = int(input("Enter the length of array : "))
for i in range(n):
    arr.append(int(input("Enter a number : ")))
print(arr)
m = len((arr))
findTriplets(arr, m)