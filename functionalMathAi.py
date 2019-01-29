import tkinter as tk
from tkinter import font as tkfont
from PIL import Image, ImageTk
import random
import time

'''
    Project Plan:
    1) Working model - done 
    2) Pictures, sounds, bells, and whistles. Colors fun stuff
        -Font
        -font Colors
        -font size
        -TITLE FOR APP
    3) Extras
        -make list of problems into 2d array
        -read and write out to file for consistency 
        -timer display
        -Progress bar
'''

'''
    General Notes:
    -bind <return> to to grade button to do same thing as hitting button
    -when make file to store user data, make it private from them!
    
    -buttons can have images too!!!
    
    -reuse same image on all pages for ease of consistent size
    
    ! use pack and pady to move label down, 
'''

blackboard_green = "#2d4630"
name = "Productivity "


def display_background(controller, frame):
    chalkboard = controller.chalkboard
    background = tk.Label(frame, image=chalkboard)
    background.image = chalkboard
    background.place(x=0, y=0, relwidth=1, relheight=1)


class Application(tk.Tk):
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def get_page(self, page_class):
        return self.frames[page_class]

    def show_and_update_frame(self, page_name):
        '''Show and update a frame for the given page name'''
        frame = self.frames[page_name]
        frame.update()
        frame.tkraise()
        self.current_page = page_name

    def enter_key_progress(self):
        curr_index = self.index[self.current_page]
        curr_index += 1

        new_page = ""
        try:
            new_page = self.index[curr_index]
        except KeyError:
            new_page = "statistic_page"

        if new_page == "statistic_page":
            if answer_page.problem_count < problem_page.number_problems:
                new_page = "problem_page"

        self.show_and_update_frame(new_page)

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        self.chalkboard = ImageTk.PhotoImage(Image.open("chalkboard.jpg"))

        self.current_page = "start_page"

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.index = {}
        self.frames = {}

        # WHERE YOU PUT ALL PAGES
        counter = 0
        for F in (start_page, problem_page, answer_page, statistic_page):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            self.index[page_name] = counter
            self.index[counter] = page_name
            counter += 1

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(self.current_page)
        self.bind('<Return>', lambda anon: self.enter_key_progress())


class start_page(tk.Frame):
    chalkboard = 'reference to image'

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="saddle brown")
        self.controller = controller

        # chalkboard = controller.chalkboard
        # background = tk.Label(self, image=chalkboard)
        # background.image = chalkboard
        # background.place(x=0, y=0, relwidth=1, relheight=1)

        display_background(controller, self)

        intro = tk.Label(self, text="Welcome to " + name + "!", font=(controller.title_font, 40),
                         borderwidth=0, fg="white", bg=blackboard_green)
        intro.pack(side="top", pady=30)

        start_button = tk.Button(self, highlightbackground=blackboard_green, text="Ready!",
                                 command=lambda: controller.show_and_update_frame("problem_page"))

        start_button.pack(side="bottom", pady=25)


class problem_page(tk.Frame):
    def make_problem(set):
        return random.choice(set)

    def solve_problem(problem):
        # problem is a tuple
        return problem[0] * problem[1]

    def solve_problem(problem):
        # problem is a tuple
        return problem[0] * problem[1]

    def format_problem(problem):
        # problem is a tuple
        return str(problem[0]) + ' times ' + str(problem[1])

    user_answer = -1
    start_time = -1

    number_problems = 3
    time_per_problem = 5

    # bounds are inclusive

    lower_bound = 1
    upper_bound = 12

    # initalize wrong problems to have one copy of every possible problem
    # inclusive bounds
    wrong_problems = []
    for i in range(lower_bound, upper_bound + 1):
        for j in range(lower_bound, upper_bound + 1):
            wrong_problems.append((i, j))

    problem = 'tuple'
    correct_answer = 'integer product of tuple,problem, '

    prompt = 'Label'
    input_box = 'Entry'
    error_box = 'Label'

    def validate(self, name, mode):
        ans = problem_page.user_answer.get()
        try:
            if ans:
                int(ans)
            problem_page.error_box.config(text='')
        except ValueError:
            problem_page.error_box.config(text='invalid input')

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        display_background(controller, self)

        question = tk.Label(self, text="What is the product of", font=(controller.title_font, 40),
                            borderwidth=0, fg="white", bg=blackboard_green)
        question.pack(side="top", pady=12)

        '''
            One label is used to display all problems. The text on the label is
            changed every time to display the new problem
        '''
        problem_page.prompt = tk.Label(self, text='error:problem not displaying', font=controller.title_font)
        problem_page.prompt.pack(side="top", fill="x", pady=10)

        problem_page.error_box = tk.Label(self, text='', font=controller.title_font)
        problem_page.error_box.pack(side="top", fill="x", pady=10)

        problem_page.user_answer = tk.StringVar()
        user_answer = problem_page.user_answer
        user_answer.trace('w', problem_page.validate)

        problem_page.input_box = tk.Entry(self, textvariable=problem_page.user_answer)
        problem_page.input_box.pack(side="top", fill="x", pady=10)
        # problem_page.input_box.focus()

        '''
            i think i need to bind return to entry box and then grade. Question then
            becomes of how to repeat, but we'll figure that out later
        '''

        problem_page.prompt.config(text=problem_page.format_problem(problem_page.problem))

        problem_page.start_time = time.time()

        submit_button = tk.Button(self, text="Grade", command=lambda: controller.show_and_update_frame("answer_page"))
        submit_button.pack()

    def update(self):
        problem_page.user_answer = tk.StringVar()
        problem_page.user_answer.trace('w', problem_page.validate)

        problem_page.input_box.config(textvariable=problem_page.user_answer)
        problem_page.input_box.focus()

        problem_page.problem = problem_page.make_problem(problem_page.wrong_problems)
        problem_page.correct_answer = problem_page.solve_problem(problem_page.problem)

        problem_page.prompt.config(text=problem_page.format_problem(problem_page.problem))
        problem_page.start_time = time.time()


class answer_page(tk.Frame):
    response = 'Label'
    solution = 'Label'
    count_correct_solutions = 0
    repeat_button = 'Button'
    controller = 'Controller'
    problem_count = 0

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        statistic_page.controller = controller

        display_background(controller, self)

        # two labels
        answer_page.response = tk.Label(self, text="response")
        answer_page.response.pack()

        answer_page.solution = tk.Label(self, text="solution")
        answer_page.solution.pack()

        answer_page.repeat_button = tk.Button(self, text="Again",
                                              command=lambda: controller.show_and_update_frame("problem_page"))
        answer_page.repeat_button.pack()

    def update(self):
        problem = problem_page.format_problem(problem_page.problem)

        user_answer = None
        try:
            user_answer = int(problem_page.user_answer.get())
        except ValueError:
            pass

        correct_answer = problem_page.correct_answer
        start_time = problem_page.start_time
        time_elapsed = time.time() - start_time

        answer_page.problem_count += 1
        if answer_page.problem_count == problem_page.number_problems:
            answer_page.repeat_button.config(command=lambda:
            statistic_page.controller.show_and_update_frame('statistic_page'))

        if time_elapsed < problem_page.time_per_problem:
            if user_answer == correct_answer:
                # user gave correct solution
                answer_page.response.config(text="Correct!")
                answer_page.solution.config(text=problem + " is " + str(correct_answer))
                answer_page.count_correct_solutions += 1
            else:
                # user gave wrong solution
                answer_page.response.config(text="Sorry, that was not correct")
                answer_page.solution.config(text=problem + " is " + str(correct_answer))
        else:
            answer_page.response.config(text="You ran out of time")
            answer_page.solution.config(text=problem + " is " + str(correct_answer))


class statistic_page(tk.Frame):
    response = 'Label'

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        display_background(controller, self)

        statistic_page.response = tk.Label(self, text="score not displaying", font=controller.title_font)
        statistic_page.response.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def update(self):
        score = (answer_page.count_correct_solutions / problem_page.number_problems) * 100
        statistic_page.response.config(text="Your score is " + str(round(score, 2)) + "%")


if __name__ == "__main__":
    app = Application()

    app.geometry("599x400")
    app.resizable(False, False)
    app.title(name + "- the multiplication app")

    app.mainloop()
