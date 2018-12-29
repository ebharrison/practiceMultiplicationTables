import tkinter as tk
from tkinter import font  as tkfont
import random
import time


#cosmetics later
#for now get it working

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
        for F in (StartPage, problem_page):
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


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("problem_page"))
        # button2 = tk.Button(self, text="Go to Page Two",
        #                     command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        # button2.pack()


class problem_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


        number_problems=3
        time_per_problem=5
        #bounds are inclusive
        lower_bound=1
        upper_bound=12

        wrong_problems=[]
        #initalize wrong problems to have one copy of every possible problem
        #inclusive bounds
        for i in range(lower_bound,upper_bound+1):
            for j in range(lower_bound,upper_bound+1):
                wrong_problems.append((i,j))

        def make_problem():
            return random.choice(wrong_problems)

        def solve_problem(problem):
            #problem is a tuple
            return problem[0]*problem[1]

        def format_problem(problem):
            return str(problem[0])+' times '+str(problem[1])


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
            try:
                if user_answer.get():
                    int(user_answer.get())
                error_box.config(text='')
            except ValueError:
                error_box.config(text='invalid input')

        user_answer=tk.StringVar()
        user_answer.trace('w', validate)

        input_box=tk.Entry(self,textvariable=user_answer)
        input_box.pack(side="top", fill="x", pady=10)
        input_box.focus()
        '''
            Code to do all problems. Each iteration of the for loop represents
            one problem set. A set consists of prompting the user for an answer,
            then grading and returning feedback to the user, returning whether
            the user input was accurate or not for the given problem.
        '''

        '''
            i think i need to bind return to entry box and then grade. Question then
            becomes of how to repeat, but we'll figure that out later
        '''

        count_correct_solutions=0
        for i in range(number_problems):
            problem = make_problem()

            prompt.config(text=format_problem(problem))

            start_time=time.time()

            prompt.config(text="grading"+user_answer.get())

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



if __name__ == "__main__":
    app = Application()
    app.geometry("600x400")
    app.mainloop()
