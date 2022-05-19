'''
@Author: Pappu Rathod
@Date: 18/05/2022
@Last Modified by: Pappu Rathod
@Title: -> Simulates a gambler who start with $stake and place fair $1 bets until
he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of
times he/she wins and the number of bets he/she makes. Run the experiment N
times, averages the results, and prints them out.
'''

import random

stake = 100
goal = 200
win = 0
loose = 0
while (stake > 0 and stake < goal):
    toss = random.randint(0, 1)

    if toss == 0:
        stake -= 1
        loose += 1
    else:
        stake += 1
        win += 1

if stake >=200:
    print('"Gambler has won"')
else:
    print('"Gambaler has broke"')

print("Number of wins: ", +win)
print("Number of loose: ", +loose)
winPercentage = (win * 100) / (win + loose)
losspercentage = 100 - winPercentage
print("Win percentage is : ", winPercentage)
print("Loss percentage is : ", losspercentage)