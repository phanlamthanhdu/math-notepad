from tkinter import *
from  tkinter import ttk
from tkinter.scrolledtext import ScrolledText


font_style = 'Helvetica 18 bold'
font_text = 13

# def Docs():
docs_window = Tk()
docs_window.geometry('500x635')
docs_window.title('Documents')
docs_window.config(bg="skyblue")
# docs_window.wm_maxsize(width=500, height=635)
frame = Frame(docs_window, width=415, height=550)
frame.pack(padx=20, pady=45, anchor="c")

label_frame = Frame(frame, width=415, height=550)
label_frame.pack(padx=20, pady=45, anchor="c")

docs_label = Label(label_frame, text="Documents",font=(font_style, font_text+2, 'bold'))
docs_label.pack(padx=20, pady=45, anchor='c')

# table_scroll = Scrollbar(frame, orient='horizontal')
# table_scroll.pack(side=BOTTOM, fill=X)
# table_scroll = Scrollbar(frame, orient='vertical')
# table_scroll.pack(side=RIGHT, fill=Y)

# docs_table = ttk.Treeview(frame,yscrollcommand=table_scroll.set, xscrollcommand =table_scroll.set)
# docs_table.pack(fill=BOTH,side=BOTTOM)

# docs_table['columns'] = ['Category','Functions']
# docs_table.column("#0", width=0,  stretch=NO)
# docs_table.column('Category',anchor=CENTER, width=80)
# docs_table.column('Functions',anchor=CENTER,width=80)

docs_window.mainloop()
