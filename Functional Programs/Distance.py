'''
@Author: Pappu Rathod
@Date: 17/05/2022
@Last Modified by: Pappu Rathod
@Title: Distance
'''
import math

def Distance(x, y):
    distance = math.sqrt(pow(x, 2) + pow(y, 2))
    print(distance)

x = int(input('Enter the value of X: '))
y = int(input('Enter the value of Y: '))
Distance(x, y)
