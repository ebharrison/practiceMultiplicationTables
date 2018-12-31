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


class Application(tk.Tk):

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
        for F in (StartPage, problem_page, answer_page):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

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
                            command=lambda: controller.show_frame("problem_page"))
        button1.pack()

        # button2 = tk.Button(self, text="Go to Page Two",
        #                     command=lambda: controller.show_frame("PageTwo"))
        # button2.pack()


class problem_page(tk.Frame):
    def make_problem(set):
        return random.choice(set)

    def solve_problem(problem):
        #problem is a tuple
        return problem[0]*problem[1]

    def solve_problem(problem):
        #problem is a tuple
        return problem[0]*problem[1]

    user_answer=-1
    start_time=0

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

    problem = make_problem(wrong_problems)


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        question = tk.Label(self, text='What is the product of', font=controller.title_font)
        question.pack(side="top", fill="x", pady=10)

        '''
            One label is used to display all problems. The text on the label is
            changed every time to display the new problem
        '''
        prompt = tk.Label(self, text='error:problem not displaying', font=controller.title_font)
        prompt.pack(side="top", fill="x", pady=10)

        error_box = tk.Label(self, text='', font=controller.title_font)
        error_box.pack(side="top", fill="x", pady=10)

        def validate(self,name,mode):
            ans=user_answer.get()
            try:
                if ans:
                    int(ans)
                error_box.config(text='')
            except ValueError:
                error_box.config(text='invalid input')
        problem_page.user_answer=tk.StringVar()
        user_answer=problem_page.user_answer
        user_answer.trace('w', validate)

        input_box=tk.Entry(self,textvariable=user_answer)
        input_box.pack(side="top", fill="x", pady=10)
        input_box.focus()

        '''
            i think i need to bind return to entry box and then grade. Question then
            becomes of how to repeat, but we'll figure that out later
        '''

        count_correct_solutions=0

        def format_problem(problem):
            #problem is a tuple
            return str(problem[0])+' times '+str(problem[1])

        prompt.config(text=format_problem(problem_page.problem))

        start_time=time.time()

        def update_answer_page():
            answer_page.grade()
            controller.show_frame("answer_page")

        # submit_button = tk.Button(self, text="Grade",
        #                    command=lambda: controller.show_frame("answer_page"))

        submit_button = tk.Button(self, text="Grade", command=update_answer_page)
        submit_button.pack()


        # #must check if timer has expired
        # time_elapsed=time.time()-start_time
        #
        # if time_elapsed < time_per_problem:
        #     """
        #         user provided solution
        #         the amount of time elapsed is less then alloted time per problem
        #         check if user solution is correct
        #     """
        #     if user_answer==solve_problem(problem):
        #         #user gave correct solution
        #         print('righty-o')
        #         count_correct_solutions+=1
        #     else:
        #         #time left but user gave wrong solution
        #         print('sorry that isn\'t right')
        #         print('the answer was',solve_problem(problem))
        # else:
        #     print('sorry but you ran out of time')
        #     if user_answer==solve_problem(problem):
        #         #user gave correct solution
        #         print('You were correct')
        #     else:
        #         #time left but user gave wrong solution
        #         print('sorry that isn\'t right')
        #         print('the answer was',solve_problem(problem))



        # button = tk.Button(self, text="Go to the start page",
        #                    command=lambda: controller.show_frame("StartPage"))
        # button.pack()

class answer_page(tk.Frame):

    response='label'
    solution='label'

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


        #two labels
        response=tk.Label(self,text="response")
        response.pack()

        solution=tk.Label(self,text="solution")
        solution.pack()


    def grade():
        print(problem_page.user_answer.get())

if __name__ == "__main__":
    app = Application()
    app.geometry("600x400")
    app.mainloop()
