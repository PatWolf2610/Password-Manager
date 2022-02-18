from tkinter import *
from tkinter import messagebox # not a class
from random import choice, randint,shuffle

FONT = ('Arial',10,'bold')
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_passord():
    password_list = []

    password_letters = [choice(LETTERS) for _ in range(randint(8, 10))]
    password_symbols = [choice(SYMBOLS) for _ in range(randint(2, 4))]
    password_numbers = [choice(NUMBERS) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = ''.join(password_list)
    pass_entry.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_insert():
    web_insert = web_entry.get()
    eu_insert = eu_entry.get()
    pass_insert = pass_entry.get()
    if web_insert == '' or eu_insert == '' or pass_entry == '':
        messagebox.showerror(title='Invalid Input',message='Do not let any field empty')
    else:
        is_ok =messagebox.askokcancel(title=web_insert,message=f"Do you want to save: \nEmail: {eu_insert}\nPassword: {pass_insert}")
        if is_ok == True:
            with open('data.txt','a') as f:
                f.write(f"Website: {web_insert} | Email: {eu_insert} | Password: {pass_insert}"+'\n')
            web_entry.delete(0,END)
            pass_entry.delete(0,END) 
        else:
            pass
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50,pady=20)

# canvas
canvas = Canvas(width=200,height=200)
mypass_img = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=mypass_img)
canvas.grid(row=0,column=1)

#Website lable
web_label = Label(text='Website',font=FONT)
web_label.grid(row=1,column=0)


#E/U labe
eu_lable = Label(text='Email/Username',font=FONT)
eu_lable.grid(row=2,column=0)

#Password label
pass_label = Label(text='Password',font=FONT)
pass_label.grid(row=3,column=0)

#websit entry
web_entry = Entry(width=55)
web_entry.grid(row=1,column=1,columnspan=2)
web_entry.focus()
#e/u entry
eu_entry = Entry(width=55)
eu_entry.grid(row=2,column=1,columnspan=2)
eu_entry.insert(0,'@gmail.com')
# password entry
pass_entry = Entry(width=34,highlightthickness=0)
pass_entry.grid(row=3,column=1)

# generate button
gen_button = Button(text='Generate Password',highlightthickness=0,width=17,command=generate_passord)
gen_button.grid(row=3,column=2)
# add button
add_button = Button(text='Add',width=47,command=save_insert)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()
