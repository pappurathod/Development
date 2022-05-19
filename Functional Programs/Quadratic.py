'''
@Author: Pappu Rathod
@Date: 18/05/2022
@Last Modified by: Pappu Rathod
@Title: Quadratic
'''

import cmath

def Quadratic(a, b, c):
    delta = (b * b) - (4 * a * c)
    root1 = (-b + cmath.sqrt(delta)) / (2 * a)
    root2 = (-b - cmath.sqrt(delta)) / (2 * a)
    print(root1)
    print(root2)

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))
Quadratic(a, b, c)
