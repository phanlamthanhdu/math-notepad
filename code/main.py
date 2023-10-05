from tkinter import *
from tkinter.scrolledtext import ScrolledText
from ttkwidgets.autocomplete import AutocompleteEntry
from math import *
from functions import *


function_list = ['comb','pow','ceil','factorial','fabs','gcd','lcm','perm','cos','sin','tan','pi','sqrt','log10','cbrt','exp','exp2','degrees','radians', 's']
font_style = 'Helvetica 18 bold'
font_text = 15

window = Tk()
window.geometry('700x835')
window.title('Math Notepad')
window.config(bg="skyblue")
window.wm_maxsize(width=700, height=1000)

frame = Frame(window, width=615, height=750)
frame.place(relx=0.5, rely=0.5, anchor="c")

calculation_label = Label(window, text="Calculation",font=(font_style, font_text, 'bold'))
calculation_label.place(relx=0.258, rely=0.14, anchor='c')

calculation_text = AutocompleteEntry(window, width=40, font=(font_style, font_text), completevalues=function_list)
calculation_text.place(relx=0.5, rely=0.18, anchor='c')

def clear_field():
    note_text.delete('1.0', END)

note_label = Label(window, text="Note",font=(font_style, font_text, 'bold'))
note_label.place(relx=0.215, rely=0.266, anchor='c')

clear_button = Button(window, width=5, height=1,text='Clear', command=clear_field,font=(font_style, font_text-5))
clear_button.place(relx=0.78, rely=0.266, anchor='c')

note_text = ScrolledText(window, width=40, height=22, font=(font_style, font_text))
note_text.place(relx=0.51, rely=0.29, anchor='n')

def click(key):
    calculate()

def calculate():

    try:
        expression = calculation_text.get()
        result = str(eval(calculation_text.get()))
        note_text.insert(1.0, ' = ' + result + '\n')
        note_text.insert(1.0,  expression)

    except:
        calculation_text.delete(0, END)
        calculation_text.insert(0, 'Error!!!')

calculation_text.bind("<Control-Return>", click)
window.mainloop()

