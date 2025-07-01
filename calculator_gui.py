#importing tkinter library
import tkinter as tk
window = tk.Tk()

window.configure(bg='black')  # Setting the window background to black

window.title("Simple GUI Calculator")

#setting the font,width etc of the widgets
display = tk.Entry(window, width=35, borderwidth=5, font=('Arial', 16))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

display.config(bg='#1c1c1c', fg='white', insertbackground='white')  # dark background, white text, white cursor

# Style dictionaries
button_style = {
    'font': ('Arial', 16),
    'fg': 'white',
    'bg': '#2e2e2e',  # dark gray for number buttons
    'activebackground': '#505050',
    'borderwidth': 0,
}

operator_style = {
    'font': ('Arial', 16),
    'fg': 'white',
    'bg': '#ff6700',  # orange for operators
    'activebackground': '#ff8c33',
    'borderwidth': 0,
}

clear_equal_style = {
    'font': ('Arial', 16),
    'fg': 'white',
    'bg': '#d32f2f',  # red for clear and equal buttons
    'activebackground': '#f55a5a',
    'borderwidth': 0,
}

# Button click function
def button_click(number):
    current = display.get()  # Gets current text in the display
    display.delete(0, tk.END)  # Deletes it
    display.insert(0, str(current) + str(number))  # Inserts old text + new number
    

# Operation functions
def button_clear():
    display.delete(0, tk.END)

def button_add():
    first_number = display.get()
    global f_num, math_op
    math_op = "add"
    f_num = float(first_number)
    display.delete(0, tk.END)

def button_subtract():
    first_number = display.get()
    global f_num, math_op
    math_op = "subtract"
    f_num = float(first_number)
    display.delete(0, tk.END)

def button_multiply():
    first_number = display.get()
    global f_num, math_op
    math_op = "multiply"
    f_num = float(first_number)
    display.delete(0, tk.END)

def button_divide():
    first_number = display.get()
    global f_num, math_op
    math_op = "divide"
    f_num = float(first_number)
    display.delete(0, tk.END)

def button_equal():
    second_number = display.get()
    display.delete(0, tk.END)
    try:
        if math_op == "add":
            display.insert(0, f_num + float(second_number))
        elif math_op == "subtract":
            display.insert(0, f_num - float(second_number))
        elif math_op == "multiply":
            display.insert(0, f_num * float(second_number))
        elif math_op == "divide":
            if float(second_number) == 0:
                display.insert(0, "Error: Div by 0")
            else:
                display.insert(0, f_num / float(second_number))
    except Exception as e:
        display.insert(0, "Error")

# Create number buttons with style
button_1 = tk.Button(window, text="1", padx=40, pady=20, command=lambda: button_click(1), **button_style)
button_2 = tk.Button(window, text="2", padx=40, pady=20, command=lambda: button_click(2), **button_style)
button_3 = tk.Button(window, text="3", padx=40, pady=20, command=lambda: button_click(3), **button_style)
button_4 = tk.Button(window, text="4", padx=40, pady=20, command=lambda: button_click(4), **button_style)
button_5 = tk.Button(window, text="5", padx=40, pady=20, command=lambda: button_click(5), **button_style)
button_6 = tk.Button(window, text="6", padx=40, pady=20, command=lambda: button_click(6), **button_style)
button_7 = tk.Button(window, text="7", padx=40, pady=20, command=lambda: button_click(7), **button_style)
button_8 = tk.Button(window, text="8", padx=40, pady=20, command=lambda: button_click(8), **button_style)
button_9 = tk.Button(window, text="9", padx=40, pady=20, command=lambda: button_click(9), **button_style)
button_0 = tk.Button(window, text="0", padx=40, pady=20, command=lambda: button_click(0), **button_style)

# Place number buttons
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

# Create operator buttons with style
button_add = tk.Button(window, text="+", padx=39, pady=20, command=button_add, **operator_style)
button_subtract = tk.Button(window, text="-", padx=41, pady=20, command=button_subtract, **operator_style)
button_multiply = tk.Button(window, text="*", padx=40, pady=20, command=button_multiply, **operator_style)
button_divide = tk.Button(window, text="/", padx=41, pady=20, command=button_divide, **operator_style)

# Place operator buttons
button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

# Create equal and clear buttons with style
button_equal = tk.Button(window, text="=", padx=88, pady=20, command=button_equal, **clear_equal_style)
button_clear = tk.Button(window, text="C", padx=88, pady=20, command=button_clear, **clear_equal_style)

# Place equal and clear buttons
button_equal.grid(row=4, column=1, columnspan=2)
button_clear.grid(row=5, column=0, columnspan=4)

window.mainloop()
