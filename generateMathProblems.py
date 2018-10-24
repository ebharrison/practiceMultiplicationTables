from random import *
import threading
import os
#make mode make time test
timePerProblem=5.0
timerLeft=True

#BUG WHEN TIME EXPIRE, PROGRAM TERMINATE
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

numProb=5
count=0
print('you will have to solve',numProb,'problems\n')
for i in range(numProb):
    testUserMulti()

print('Your score was',str(count*100/numProb)+'%')



# makeProb()
# timer=threading.Timer(6.0,timeUp)
# timer.start()
# while True:
#     print(problem)
#     ans=input('Enter the product\n')
#     print('got this as ans',ans)
#     try:
#         ans=input(ans)
#     except TypeError:
#         if ans=='':
#             pass
#         elif ans=='end':
#             break
#         else:
#             print('Invalid input')
#             continue
#     if ans==problem[0]*problem[1]:
#         print('Righty-O!')
#         timer.cancel()
#         makeProb()
#     else:
#         print('sorry ')
#         timer.cancel()
#         makeProb()

# while True:
#     global problem
#     problem=(randint(1,12),randint(1,12))
#
#     try:
#         print(problem)
#         timer=threading.Timer(5.0,timeUp)
#         timer.start()
#         ans=input('Enter the product\n')
#         if ans=='end':
#             break
#         ans=int(ans)
#     except ValueError:
#         print('')
#         print('That wasn\'t a integer\n')
#         print('')
#     else:
#         if timeLimit==True and ans==problem[0]*problem[1]:
#             timer.cancel()
#             print('')
#             print('Correct!')
#         else:
#             print('not quite. The answer is ',problem[0]*problem[1])
