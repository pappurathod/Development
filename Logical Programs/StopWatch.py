'''
@Author: Pappu Rathod
@Date: 17/05/2022
@Last Modified by: Pappu Rathod
@Title: Write a Stopwatch Program for measuring the time that elapses between
the start and end clicks
'''

import time
def timeConvert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed is = {0}:{1}:{2}".format(int(hours),int(mins),sec))

input("Press Enter to start the StopWatch : ")
startTime = time.time()

input("Press Enter to stop the StopWatch : ")
endTime = time.time()

elapseTime = endTime - startTime
timeConvert(elapseTime)