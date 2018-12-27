import random
import threading
import os
#make mode make time test
timePerProblem=5.0
timerLeft=True
numProb=10
upperBound=12
lowerBound=1
wrongProblems=[]
#initalize wrong problems to have on copy of every possibility
for i in range(lowerBound,upperBound+1):
    for j in range(lowerBound,upperBound+1):
        wrongProblems.append((i,j))

#time user to do all problems? or make timer for whole problem set?
#todo machine learn make dict and add pairs as needed
#after machine learn, write out to file and read in for user
#write out percents to file and extrapolate info from data

def timeUp():
    #os.system('clear')
    global timerLeft
    timerLeft=False
    print('times up!')
    print('the answer was ',problem[0]*problem[1])

def makeProb():
    return random.choice(wrongProblems)

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
        t.cancel()
        print('\nRighty-O!\n')
        global count
        count+=1
        try:
            wrongProblems.remove(problem)
        except:
            wrongProblems.append(problem)
    else:
        t.cancel()
        print('sorry, but keep trying')
        print('the answer was ',problem[0]*problem[1],'\n')
        wrongProblems.append(problem)


count=0
print('you will have to solve',numProb,'problems\n')
for i in range(numProb):
    #print(wrongProblems)
    input('Hit any key when ready\n')
    testUserMulti()
    print('')

print('Your score was',str(count*100/numProb)+'%')
