import tkinter as tk

font_style = 'Helvetica 18 bold'
font_text = 15


# def Running():
#     global window
    
#     window = tk.Tk()
#     window.geometry('700x835')
#     window.title('Math Notepad')
#     window.config(bg="skyblue")
#     window.wm_maxsize(width=700, height=1000)

#     frame = tk.Frame(window, width=615, height=750)
#     frame.place(relx=0.5, rely=0.5, anchor="c")

#     Calculation(window)
#     Result(window)
#     Note(window)

#     window.mainloop()

# def click(key):
#     if(key.keycode == 13):
#         pass

# def Calculation(window):
#     calculation_label = tk.Label(window, text="Calculation",font=(font_style, font_text, 'bold'))
#     calculation_label.place(relx=0.258, rely=0.14, anchor='c')

#     calculation = ''
#     calculation_text = tk.Entry(window, width=40, textvariable=calculation,font=(font_style, font_text))
#     calculation_text.bind("<Key>", click)
#     calculation_text.place(relx=0.5, rely=0.18, anchor='c')


# def Result(window):
#     result_label = tk.Label(window, text="Result",font=(font_style, font_text, 'bold'))
#     result_label.place(relx=0.227, rely=0.26, anchor='c')

#     result_text = tk.Entry(window, width=40, font=(font_style, font_text))
#     result_text.place(relx=0.5, rely=0.3, anchor='c')
#     result_text.configure(state="disabled")

# def Note(window):
#     note_label = tk.Label(window, text="Note",font=(font_style, font_text, 'bold'))
#     note_label.place(relx=0.215, rely=0.38, anchor='c')

#     clear_button = tk.Button(window, width=5, height=1,text='Clear', font=(font_style, font_text-5))
#     clear_button.place(relx=0.78, rely=0.38, anchor='c')

#     note_text = tk.Text(window, width=40, height=17, font=(font_style, font_text))
#     note_text.place(relx=0.5, rely=0.4, anchor='n')



font_style = 'Helvetica 18 bold'
font_text = 15

class math_notepad:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.geometry('700x835')
        self.window.title('Math Notepad')
        self.window.config(bg="skyblue")
        self.window.wm_maxsize(width=700, height=1000)

        self.frame = tk.Frame(self.window, width=615, height=750)
        self.frame.place(relx=0.5, rely=0.5, anchor="c")

        math_notepad.Calculation(self)
        math_notepad.Result(self)
        math_notepad.Note(self)

        self.window.mainloop()

    def click(key):
        print(key.char)
        if(key.keycode == 13):
            pass

    def Calculation(self):
        self.calculation_label = tk.Label(self.window, text="Calculation",font=(font_style, font_text, 'bold'))
        self.calculation_label.place(relx=0.258, rely=0.14, anchor='c')

        self.calculation = ''
        self.calculation_text = tk.Entry(self.window, width=40, textvariable=self.calculation,font=(font_style, font_text))
        self.calculation_text.bind("<Key>", math_notepad.click)
        self.calculation_text.place(relx=0.5, rely=0.18, anchor='c')


    def Result(self):
        self.result_label = tk.Label(self.window, text="Result",font=(font_style, font_text, 'bold'))
        self.result_label.place(relx=0.227, rely=0.26, anchor='c')

        self.result_text = tk.Entry(self.window, width=40, font=(font_style, font_text))
        self.result_text.place(relx=0.5, rely=0.3, anchor='c')
        self.result_text.configure(state="disabled")

    def Note(self):
        self.note_label = tk.Label(self.window, text="Note",font=(font_style, font_text, 'bold'))
        self.note_label.place(relx=0.215, rely=0.38, anchor='c')

        self.clear_button = tk.Button(self.window, width=5, height=1,text='Clear', font=(font_style, font_text-5))
        self.clear_button.place(relx=0.78, rely=0.38, anchor='c')

        self.note_text = tk.Text(self.window, width=40, height=17, font=(font_style, font_text))
        self.note_text.place(relx=0.5, rely=0.4, anchor='n')

