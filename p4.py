from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as pt
from matplotlib.backends.backend_pdf import PdfPages

root=Tk()
root.title('Expenses Recorder')
root.geometry('1000x600+300+400')
f='Times New Roman',14, 'bold'

def calc():
    try:
        travel_exp = float(travel_entry.get())
        food_exp = float(food_entry.get())
        shopping_exp = float(shopping_entry.get())
        entertainment_exp = float(entertainment_entry.get())
        others_exp = float(others_entry.get())
        total = travel_exp + food_exp + shopping_exp + entertainment_exp + others_exp

        if total == 0:
            raise ValueError("Total expenses cannot be zero!")
        
        expenses=[travel_exp,food_exp,shopping_exp,entertainment_exp,others_exp]
        data=['travel','food','shopping','entertainment','others']

        fig,ax=pt.subplots()
        ax.pie(expenses,labels=data)
        ax.set_title(f'Expenses of {name_entry.get()}')
        
        filename=f'{name_entry.get()}_expenses.pdf'
        pdf=PdfPages(filename)
        pdf.savefig(fig)
        pdf.close()

        messagebox.showinfo('Success', f'Pie chart saved as {filename}')

        name_entry.delete(0, END)
        travel_entry.delete(0, END)
        food_entry.delete(0, END)
        shopping_entry.delete(0, END)
        entertainment_entry.delete(0, END)
        others_entry.delete(0, END)
        
    except ValueError:
        messagebox.showerror('Input Error','Enter correct numbers for all expenses')

name=Label(root,text='Enter Name',font=f)
name_entry=Entry(root)

expense=Label(root,text='Expenses',font=f)
travel=Label(root,text='Enter expenses for travel',font=f)
travel_entry=Entry(root)

food=Label(root,text='Enter expenses for food',font=f)
food_entry=Entry(root)

shopping=Label(root,text='Enter expenses for shopping',font=f)
shopping_entry=Entry(root)

entertainment=Label(root,text='Enter expenses for entertainment',font=f)
entertainment_entry=Entry(root)

others=Label(root,text='Enter other expenses',font=f)
others_entry=Entry(root)

calculate=Button(root,text='Calculate my expenses',font=f,command=calc)

name.pack(pady=5)
name_entry.pack(pady=10)
expense.pack(pady=5)
travel.pack(pady=10)
travel_entry.pack(pady=10)
food.pack(pady=10)
food_entry.pack(pady=10)
shopping.pack(pady=10)
shopping_entry.pack(pady=10)
entertainment.pack(pady=10)
entertainment_entry.pack(pady=10)
others.pack(pady=10)
others_entry.pack(pady=10)
calculate.pack(pady=10)

root.mainloop()
