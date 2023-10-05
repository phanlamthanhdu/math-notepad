import tkinter as tk
import components

def click(key):
    if(key.keycode == 13):
        print("you clicked")

def calculate(window):
    global calculation
    # global Ans

    try:
        calculation = str(eval(calculation))
        # Ans = calculation
        window.calculation.delete(1.0, 'end')
        window.result.insert(1.0, calculation)
    except:
        clear_field()
        window.calculation.insert(1.0, 'Error') 

def clear_field(window):
    pass