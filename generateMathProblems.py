from random import *
import threading
import os
#make mode make time test
timePerProblem=10.0
timerLeft=True
numProb=3

#THIS WILL ONLY BE ON MACHINELEARN BRANCH

# Solution? make iterable of math problems

def timeUp():
    #os.system('clear')
    global timerLeft
    timerLeft=False
    print('times up!')
    print('the answer was ',problem[0]*problem[1])

def makeProb():
    global problem
    problem=(randint(1,12),randint(1,12))

def makeTimer():
    global timePerProblem
    return threading.Timer(timePerProblem,timeUp)

def testUserMulti():
    global timerLeft
    global problem
    makeProb()
    print(problem)
    print('product?')
    t=makeTimer()
    t.start()
    invalid=True
    while invalid:
        try:
            ans=''
            ans=int(input())
            invalid=False
        except ValueError:
            if ans=='':
                if timerLeft==False:
                    return
                else:
                    pass

    if timerLeft==True and ans==problem[0]*problem[1]:
        print('\nRighty-O!\n')
        global count
        count+=1
        t.cancel()
    else:
        print('\nsorry, but keep trying\n')
        print('the answer was ',problem[0]*problem[1],'\n')
        t.cancel()


count=0
print('you will have to solve',numProb,'problems\n')
for i in range(numProb):
    input('Hit any key when ready')
    testUserMulti()
    print('')

print('Your score was',str(count*100/numProb)+'%')
