import tkinter as tk
from tkinter import messagebox

def check_upper(input):
    uppers = 0 
    upper_list = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
    for char in input:
        if char in upper_list:
            uppers += 1
    return uppers > 0

def check_lower(input):
    lowers = 0
    lower_list = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    for char in input:
        if char in lower_list:
            lowers += 1
    return lowers > 0

def check_number(input):
    numbers = 0
    number_list = "1 2 3 4 5 6 7 8 9 0".split()
    for char in input:
        if char in number_list:
            numbers += 1
    return numbers > 0

def check_special(input):
    specials = 0
    special_list = "! @ $ % ^ & * ( ) _ - + = { } [ ] | \ , . > < / ? ~ ` \" ' : ;".split()
    for char in input:
        if char in special_list:
            specials += 1
    return specials > 0

def check_len(input):
    return len(input) >= 8

def validate_password(input):
    check_dict = {
        'upper': check_upper(input),
        'lower': check_lower(input),
        'number': check_number(input),
        'special': check_special(input),
        'len' : check_len(input)
    }
    if all(check_dict.values()):
        messagebox.showinfo("Success", "Password meets all requirements and may be used.")
    else:
        error_message = "Invalid password! Review below and change your password accordingly!\n\n"
        if not check_dict['upper']:
            error_message += "Password needs at least one upper-case character.\n"
        if not check_dict['lower']:
            error_message += "Password needs at least one lower-case character.\n"
        if not check_dict['number']:
            error_message += "Password needs at least one number.\n"
        if not check_dict['special']:
            error_message += "Password needs at least one special character.\n"
        if not check_dict['len']:
            error_message += "Password needs to be at least 8 characters in length.\n"
        messagebox.showerror("Error", error_message)

def validate_and_exit():
    password = password_entry.get()
    validate_password(password)
    root.destroy()

# Create the GUI window
root = tk.Tk()
root.title("Password Validator")

# Create and place the password entry widget
password_label = tk.Label(root, text="Enter Password:")
password_label.pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

# Create and place the validate button
validate_button = tk.Button(root, text="Validate", command=validate_and_exit)
validate_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()

