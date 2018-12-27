import random
import time
import os
import time

#ignore menu screen for now
#straight to problems

number_problems=3
time_per_problem=5
#bounds are inclusive
lower_bound=1
upper_bound=12

wrong_problems=[]
#initalize wrong problems to have one copy of every possibility
#inclusive bounds
for i in range(lower_bound,upper_bound+1):
    for j in range(lower_bound,upper_bound+1):
        wrong_problems.append((i,j))

def make_problem():
    return random.choice(wrong_problems)

def solve_problem(problem):
    #problem is a tuple
    return problem[0]*problem[1]

count_correct_solutions=0
for i in range(number_problems):
    #code to do each problem
    problem = make_problem()
    print(problem)
    print('product?')
    start_time=time.time()
    #test that input only consists of integer digits of any length
    #assume false input
    user_answer=1
    invalid=True
    while invalid:
        try:
            #cast input to integer
            #if fails, then contains non-integer character
            user_answer=int(input())
            invalid=False
        except ValueError:
            print('invalid input, please try again')

    #must check if timer has expired
    time_elapsed=time.time()-start_time

    if time_elapsed < time_per_problem:
        """
            user provided solution
            the amount of time elapsed is less then alloted time per problem
            check if user solution is correct
        """
        if user_answer==solve_problem(problem):
            #user gave correct solution
            print('righty-o')
            count_correct_solutions+=1
        else:
            #time left but user gave wrong solution
            print('sorry that isn\'t right')
            print('the answer was',solve_problem(problem))
    else:
        print('sorry but you ran out of time')
        if user_answer==solve_problem(problem):
            #user gave correct solution
            print('You were correct')
        else:
            #time left but user gave wrong solution
            print('sorry that isn\'t right')
            print('the answer was',solve_problem(problem))
    print('\n')

print('Final Score: {}%'.format( round( ( (
    count_correct_solutions/number_problems)*100.0),2) ) )
