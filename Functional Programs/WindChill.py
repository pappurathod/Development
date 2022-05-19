'''
@Author: Pappu Rathod
@Date: 18/05/2022
@Last Modified by: Pappu Rathod
@Title: WindChill
'''

def WindCalculation(t,v):
        w=35.74+(0.6215*t)+((0.4275*t)-35.75)*pow(v,0.16)  # calculation formula
        print("calculated windchill is : ",w)

t= int(input("Enter the temperature in Fahrenheit is less then 50 : "))
v= int(input("Enter wind speed in miles per/hour from 3 to 120 : "))

if(v > 120 or v < 3 or t > 50 ):
    print("Enter value in range")
else:
    WindCalculation(t,v)
