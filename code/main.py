import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import components

font_style = 'Helvetica 18 bold'
font_text = 15

window = tk.Tk()
window.geometry('700x835')
window.title('Math Notepad')
window.config(bg="skyblue")
window.wm_maxsize(width=700, height=1000)

frame = tk.Frame(window, width=615, height=750)
frame.place(relx=0.5, rely=0.5, anchor="c")

calculation_label = tk.Label(window, text="Calculation",font=(font_style, font_text, 'bold'))
calculation_label.place(relx=0.258, rely=0.14, anchor='c')

calculation_text = tk.Entry(window, width=40, font=(font_style, font_text))
calculation_text.place(relx=0.5, rely=0.18, anchor='c')

# result_label = tk.Label(window, text="Result",font=(font_style, font_text, 'bold'))
# result_label.place(relx=0.227, rely=0.26, anchor='c')

# result_text = tk.Text(window, width=40, height=1, font=(font_style, font_text))
# result_text.place(relx=0.5, rely=0.3, anchor='c')
# result_text.configure(state="disabled")


note_label = tk.Label(window, text="Note",font=(font_style, font_text, 'bold'))
note_label.place(relx=0.215, rely=0.266, anchor='c')

clear_button = tk.Button(window, width=5, height=1,text='Clear', font=(font_style, font_text-5))
clear_button.place(relx=0.78, rely=0.266, anchor='c')

note_text = ScrolledText(window, width=40, height=22, font=(font_style, font_text))
note_text.place(relx=0.51, rely=0.29, anchor='n')

def click(key):
    if(key.keycode == 13):
        calculate()

def calculate():

    try:
        expression = calculation_text.get()
        result = str(eval(calculation_text.get()))
        note_text.insert(1.0, '\n= ' + result + '\n')
        note_text.insert(1.0,  expression)
        # Ans = calculation
        # calculation.delete(1.0, 'end')
        # result_text.configure(state="normal")
        # result_text.delete(1.0, 'end')
        # result_text.insert(1.0, result)
        # result_text.configure(state="disabled")


    except:
        clear_field()
        calculation_text.insert(1.0, 'Error')

def clear_field():
    pass

calculation_text.bind("<Key>", click)
window.mainloop()


