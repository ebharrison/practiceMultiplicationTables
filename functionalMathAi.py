import tkinter as tk
from tkinter import font  as tkfont
import random
import time

'''
    Project Plan:
    1) Working model
    2) Pictures, sounds, bells, and whistles. Colors fun stuff
        -Font
        -font Colors
        -font size
        -TITLE FOR APP
    3) Extras
        -timer display
        -Progress bar
'''

'''
    General Notes:
    -bind <return> to to grade button to do same thing as hitting button
'''


class Application(tk.Tk):
    def show_and_update_frame(self, page_name):
        '''Show and update a frame for the given page name'''
        frame = self.frames[page_name]
        frame.update()
        frame.tkraise()

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)


        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        #WHERE YOU PUT ALL PAGES
        for F in (StartPage, problem_page, answer_page, statistic_page):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

        self.bind('<Return>',lambda anon: self.show_and_update_frame('answer_page'))



    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def get_page(self,page_class):
        return self.frames[page_class]


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Problem One",
                            command=lambda: controller.show_and_update_frame("problem_page"))
        button1.pack()


class problem_page(tk.Frame):
    def make_problem(set):
        return random.choice(set)

    def solve_problem(problem):
        #problem is a tuple
        return problem[0]*problem[1]

    def solve_problem(problem):
        #problem is a tuple
        return problem[0]*problem[1]

    def format_problem(problem):
        #problem is a tuple
        return str(problem[0])+' times '+str(problem[1])

    user_answer=-1
    start_time=-1

    number_problems=3
    time_per_problem=5
    #bounds are inclusive
    lower_bound=1
    upper_bound=12

    #initalize wrong problems to have one copy of every possible problem
    #inclusive bounds
    wrong_problems=[]
    for i in range(lower_bound,upper_bound+1):
        for j in range(lower_bound,upper_bound+1):
            wrong_problems.append((i,j))

    problem = 'tuple'
    correct_answer = 'integer product of tuple,problem, '

    prompt='Label'
    input_box='Entry'
    error_box='Label'

    def validate(self,name,mode):
        ans=problem_page.user_answer.get()
        try:
            if ans:
                int(ans)
            problem_page.error_box.config(text='')
        except ValueError:
            problem_page.error_box.config(text='invalid input')

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        question = tk.Label(self, text='What is the product of', font=controller.title_font)
        question.pack(side="top", fill="x", pady=10)

        '''
            One label is used to display all problems. The text on the label is
            changed every time to display the new problem
        '''
        problem_page.prompt = tk.Label(self, text='error:problem not displaying', font=controller.title_font)
        problem_page.prompt.pack(side="top", fill="x", pady=10)

        problem_page.error_box = tk.Label(self, text='', font=controller.title_font)
        problem_page.error_box.pack(side="top", fill="x", pady=10)

        problem_page.user_answer=tk.StringVar()
        user_answer=problem_page.user_answer
        user_answer.trace('w', problem_page.validate)

        problem_page.input_box=tk.Entry(self,textvariable=problem_page.user_answer)
        problem_page.input_box.pack(side="top", fill="x", pady=10)
        #problem_page.input_box.focus()

        '''
            i think i need to bind return to entry box and then grade. Question then
            becomes of how to repeat, but we'll figure that out later
        '''

        problem_page.prompt.config(text=problem_page.format_problem(problem_page.problem))

        problem_page.start_time=time.time()

        # def update_answer_page():
        #     answer_page.update()
        #     controller.show_frame("answer_page")

        submit_button = tk.Button(self, text="Grade", command=lambda:controller.show_and_update_frame("answer_page"))
        submit_button.pack()

    def update(self):
        problem_page.user_answer=tk.StringVar()
        problem_page.user_answer.trace('w', problem_page.validate)

        problem_page.input_box.config(textvariable=problem_page.user_answer)
        problem_page.input_box.focus()

        problem_page.problem = problem_page.make_problem(problem_page.wrong_problems)
        problem_page.correct_answer = problem_page.solve_problem(problem_page.problem)

        problem_page.prompt.config(text=problem_page.format_problem(problem_page.problem))
        problem_page.start_time=time.time()


class answer_page(tk.Frame):

    response='Label'
    solution='Label'
    count_correct_solutions=0
    repeat_button='Button'
    controller='Controller'
    problem_count=0

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        statistic_page.controller = controller

        #two labels
        answer_page.response=tk.Label(self,text="response")
        answer_page.response.pack()

        answer_page.solution=tk.Label(self,text="solution")
        answer_page.solution.pack()

        answer_page.repeat_button=tk.Button(self,text="Again",
            command=lambda: controller.show_and_update_frame("problem_page"))
        answer_page.repeat_button.pack()

    def update(self):
        problem=problem_page.format_problem(problem_page.problem)
        user_answer=int(problem_page.user_answer.get())
        correct_answer=problem_page.correct_answer
        start_time=problem_page.start_time
        time_elapsed=time.time()-start_time

        #print('problem count',answer_page.problem_count)
        answer_page.problem_count+=1
        if answer_page.problem_count>=problem_page.number_problems:
            answer_page.repeat_button.config(command=lambda:
                statistic_page.controller.show_and_update_frame('statistic_page'))

        if time_elapsed<problem_page.time_per_problem:
            if user_answer==correct_answer:
                # user gave correct solution
                answer_page.response.config(text="Correct!")
                answer_page.solution.config(text=problem+" is "+str(correct_answer))
                answer_page.count_correct_solutions+=1
            else:
                #user gave wrong solution
                answer_page.response.config(text="Sorry, that was not correct")
                answer_page.solution.config(text=problem+" is "+str(correct_answer))
        else:
            answer_page.response.config(text="You ran out of time")
            answer_page.solution.config(text=problem+" is "+str(correct_answer))
            

class statistic_page(tk.Frame):

    response='Label'

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        statistic_page.response=tk.Label(self,text="score not displaying")
        statistic_page.response.pack()

    def update(self):
        score=answer_page.count_correct_solutions*100/problem_page.number_problems
        statistic_page.response.config(text="Your score is "+str( round(score,2) )+"%")

if __name__ == "__main__":
    app = Application()
    app.geometry("600x400")
    app.mainloop()
