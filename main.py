from enum import Flag
import json
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
import time
from tkinter.messagebox import showerror, showinfo

import pyperclip

splash_root = Tk()
splash_root.title("Splash Sc")

app_width = 600
app_height= 400
screen_width = splash_root.winfo_screenwidth()
screen_height = splash_root.winfo_screenheight()
x = (screen_width/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)

splash_root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
img = PhotoImage(file="main1.png")
splash_root.geometry("600x400")
splash_root.overrideredirect(True)
splash_label = Label(splash_root, image=img)
splash_label.pack()

def hide_pass():
    op_img = PhotoImage(file='open.png')
    e2.config(show="•")
    # sb.config(image=op_img)
    sb = Button(window1, image=op_img,relief=FLAT,bg='white',activebackground='white',border=0,command=show_pass,cursor='hand2')
    sb.place(x=360,y=313)
    mainloop()
def show_pass():
    clo_img = PhotoImage(file='close.png')
    e2.config(show='')
    # sb.config(image=clo_img)
    sb = Button(window1, image=clo_img,relief=FLAT,bg='white',activebackground='white',border=0,command=hide_pass,cursor='hand2')
    sb.place(x=360,y=313)
    mainloop()

def hide_pass1():
    eye_open = PhotoImage(file='open.png')
    ps.config(show='•')
    Button(creator, image=eye_open,relief=FLAT,bg='white',activebackground='white',border=0,cursor='hand2',command=show_pass1).place(x=342,y=263)
    mainloop()
def show_pass1():
    eye_close = PhotoImage(file='close.png')
    ps.config(show='')
    Button(creator, image=eye_close,relief=FLAT,bg='white',activebackground='white',border=0,cursor='hand2',command=hide_pass1).place(x=342,y=263)
    mainloop()

def show_pass2():
    eye_close = PhotoImage(file='close.png')
    re_ps.config(show='')
    Button(creator, image=eye_close,relief=FLAT,bg='white',activebackground='white',border=0,cursor='hand2',command=hide_pass2).place(x=342,y=328)
    mainloop()
def hide_pass2():
    eye_open = PhotoImage(file='open.png')
    re_ps.config(show='•')
    Button(creator, image=eye_open,relief=FLAT,bg='white',activebackground='white',border=0,cursor='hand2',command=show_pass2).place(x=342,y=328)
    mainloop()

def show_pass3():
    eye_close = PhotoImage(file='close.png')
    Button(my_frame2, image=eye_close,relief=FLAT,bg='white',activebackground='white',border=0,command=hide_pass3,cursor='hand2').place(x=252,y=220)
    ent2.config(show='')
    mainloop()
    # pass
def hide_pass3():
    eye_open = PhotoImage(file='open.png')
    Button(my_frame2, image=eye_open,relief=FLAT,bg='white',activebackground='white',border=0,command=show_pass3,cursor='hand2').place(x=252,y=220)
    sbmt.config(image=eye_open)
    ent2.config(show='•')
    mainloop()
    # pass

def onClick(e):
    my_font2 = Font(family="Arial", size=10, weight='normal', underline=1)
    submit.config(fg='#36009c',text='Login',activebackground='white',font=my_font2)
def onLeave(e):
    my_font2 = Font(family="Arial", size=10, weight='normal')
    submit.config(fg='#6c22f5',text='Login',activebackground='white',font=my_font2)

def closeClick(e):
    my_font2 = Font(family="Times New Roman", size=10, weight='normal', underline=1)
    cbtn.config(text="Close",font=my_font2)
def closeLeave(e):
    my_font2 = Font(family="Times New Roman", size=10, weight='normal')
    cbtn.config(text="Close",font=my_font2)

def newOnClick(e):
    my_font2 = Font(family="arial", size=10, weight='normal', underline=1)
    cr_new.config(fg='#36009c',font=my_font2)
def newOnClose(e):
    my_font2 = Font(family="arial", size=10, weight='normal')
    cr_new.config(fg='#6c22f5',font=my_font2)

def createOnHover(e):
    btn_font = Font(family="Times New Roman", size=13, weight='bold', underline=1)
    save_new_user.config(fg='#36009c',font=btn_font)
def createOffHover(e):
    btn_font = Font(family="Times New Roman", size=13, weight='bold')
    save_new_user.config(fg='#6c22f5',font=btn_font)

def onClickNewHover(e):
    my_font1 = Font(family="Courier", size=15, weight='bold',underline=1)
    submit1.config(font=my_font1,fg="yellow")
def onLeaveNewHover(e):
    my_font1 = Font(family="Courier", size=15, weight='normal')
    submit1.config(font=my_font1,fg="#6c22f5")

def closeOnClickHover(e):
    my_font2 = Font(family="Times New Roman", size=10, weight='normal',underline=1)
    clsbtn.config(font=my_font2)
def closeOnLeaveHover(e):
    my_font2 = Font(family="Times New Roman", size=10, weight='normal')
    clsbtn.config(font=my_font2)

def second_login():
    f = open(file='data.json', mode='r')
    my_file = f.read()
    onj = json.loads(my_file)
    list1 = onj['Pass']
    ls = list1[0].get('User')
    l = list1[0].get('Password')
    # print(str(onj['Password']))
    if ent1.get() == '' or ent1.get() == '@':
        showerror("Error", "Please Enter Your User-Id.")
    elif ent2.get() == '':
        showerror("Error", "Please Enter Your Password.")
    elif ent1.get() in ls:
        if len(ls) == len(ent1.get()):
            print('User Found')
            if ent2.get() in l:
                if len(l) == len(ent2.get()):
                # print("User found.")
                    print("Password Matched.")
                else:
                    print("Password Not Matched.")
            else:
                print("Password is Not Correct.")
        else:
            print("UserID Not Found .")
    else:
        print("User Not Found .")

def first_login():
    f = open(file='data.json', mode='r')
    my_file = f.read()
    onj = json.loads(my_file)
    list1 = onj['Pass']
    ls = list1[0].get('User')
    l = list1[0].get('Password')
    # print(str(onj['Password']))
    if e1.get() == '' or e1.get() == '@':
        showerror("Error", "Please Enter Your User-Id.")
    elif e2.get() == '':
        showerror("Error", "Please Enter Your Password.")
    elif e1.get() in ls:
        if len(ls) == len(e1.get()):
            print('User Found')
            if e2.get() in l:
                if len(l) == len(e2.get()):
                # print("User found.")
                    print("Password Matched.")
                else:
                    print("Password Not Matched.")
            else:
                print("Password is Not Correct.")
        else:
            print("UserID Not Found .")
    else:
        print("User Not Found .")

def login_page():
    creator.destroy()
    global submit1, clsbtn, sbmt, ent2
    global my_frame2
    global ent1
    login_window = Tk()
    login_window.overrideredirect(True)
    login_window.title("STUDENT MANAGEMENT SOFTWARE")
    app_width = 500
    app_height = 500
    screen_width = login_window.winfo_screenwidth()
    screen_height = login_window.winfo_screenheight()
    x = (screen_width/2) - (app_width/2)
    y = (screen_height/2) - (app_height/2)

    login_window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    # window1.config(bg="#9b7ede")
    # window1.overrideredirect(True)
    my_font = Font(family="Comic Sans MS", size=20, weight='bold', slant='italic', underline=1)
    j = 0
    r = 0
    for i in range(100):
        c = str(222222+r)
        my_frame=Frame(login_window, width=10, height=500,bg='#'+c).place(x=j,y=0)
        j = j + 10
        r = r + 1
    Label(my_frame, text="Student Management",font=my_font,bg="#222222", fg="#03d5ff").pack(fill=X)
    my_frame2 = Frame(my_frame,width=300, height=350,bg='white')
    my_frame2.place(x=100,y=100)
    
    us_img = PhotoImage(file='user1.png')
    op_img = PhotoImage(file='open.png')
    Label(my_frame2, image=us_img, bg='white').place(x=90)
    l = ('console 13 bold')
    Label(my_frame2, text="Username", bg='white',font=l).place(x=10, y = 130)
    
    ent1 = Entry(my_frame2, width=23, border=0)
    ent1.config(font='courier 13')
    ent1.place(x=10, y=160)
    ent1.insert(0, "@")

    Label(my_frame2, text="Password", bg='white',font=l).place(x=10, y= 190)

    ent2 = Entry(my_frame2, width=23, border=0, show="•")
    ent2.config(font='courier 13')
    ent2.place(x=10, y=220)

    Frame(my_frame2, width=260, height=2,bg="#141414").place(x=10,y=180)
    Frame(my_frame2, width=260, height=2,bg="#141414").place(x=10,y=240)

    sbmt = Button(my_frame2, image=op_img,relief=FLAT,bg='white',activebackground='white',border=0,command=show_pass3,cursor='hand2')
    sbmt.place(x=252,y=220)
    my_font1 = Font(family="Courier", size=15, weight='normal')
    submit1 = Button(my_frame2, text="Login", relief=FLAT, bg='white',fg='#6c22f5',font=my_font1,activebackground='white',border=0,cursor='hand2')
    submit1.place(x=105,y=280)
    submit1.config(command=second_login)
    submit1.bind("<Enter>", onClickNewHover)
    submit1.bind("<Leave>", onLeaveNewHover)
    my_font2 = Font(family="Times New Roman", size=10, weight='normal')
    clsbtn = Button(my_frame2,text="Close",font=my_font2,bg='white',fg='red',relief=FLAT,border=0,activebackground='white',cursor='hand1',command=quit)
    clsbtn.place(x=260, y= 330)
    clsbtn.bind("<Enter>", closeOnClickHover)
    clsbtn.bind("<Leave>", closeOnLeaveHover)
    
    mainloop()

def dm_for_pass_save(nowas):
    try:
        with open('data.json', mode='r') as op:
            pd = json.load(op)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        with open('data.json', mode='w') as nwp:
            json.dump(nowas, nwp, indent=4)
    else:
        pd.update(nowas)
        with open('data.json', mode="w") as op:
            json.dump(pd, op, indent=4)
    showinfo("Success", "You can now login with this username and password.")
    login_page()

def before_login_page():
    if us.get() == '' or us.get() == '@':
        showerror("Error", "Enter Your Username .")
    elif ps.get() == '':
        showerror("Error", "Enter Your Password First.")
    elif re_ps.get() == '':
        showerror("Error", "Enter Your Password First.")
    elif asking.get() == '' or ans.get() == '' or ans.get() == 'answer here':
        showerror("Error", "Fill the question or answer box first.")
    elif ps.get() != re_ps.get():
        showerror("Error", "Password Not Matched !")
    elif us.get() or ps.get() or re_ps.get() or asking.get() or ans.get():
        pyperclip.copy(us.get())
        now = {
            "Pass":
            [{
                "User" : us.get(),
                "Password": ps.get()
            }]
        }
        dm_for_pass_save(now)
        # with open('data.json', 'r') as op:
        #     f = op.read()
        #     ob = json.loads(f)
        #     list1 = ob['Pass']
        #     ls = list1[0].get('User')
        #     if us.get() in ls:
        #         showerror("Found", "User Already Exist.")
        #     else:
        # login_page()
    else:
        showerror("Error", "Any other issue found.")
    # pass    

def main_win1():
    global creator
    global ps, re_ps, open_eye1, open_eye2,save_new_user
    global us, ps, re_ps, asking, ans

    window1.destroy()
    # print("It's working...")
    creator=Tk()
    creator.overrideredirect(True)
    app_width = 440
    app_height = 550
    screen_width = creator.winfo_screenwidth()
    screen_height = creator.winfo_screenheight()
    x = (screen_width/2) - (app_width/2)
    y = (screen_height/2) - (app_height/2)
    creator.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    

    my_font = Font(family="Comic Sans MS", size=20, weight='bold', slant='italic', underline=1)
    Label(creator, text="Create New Account", font=my_font, bg="#b06719", fg="white").pack(fill=X)
    Frame(creator, width=440, height=550,bg='#b06719').pack()
    Frame(creator, width=350, height=450,bg='white').place(x=45,y=50)
    add_User = PhotoImage(file='add_user1.png')
    Label(image=add_User, bg="white").place(x=160, y=50)
    l = ('console 13 bold')
    Label(text="Username", bg='white', fg='blue',font=l).place(x=70,y=170)
    us = Entry(creator, fg="brown",relief=FLAT,font="arial 13",width=29)
    us.place(x=70,y=195)
    us.insert(0, "@")
    Label(text="Password", bg='white', fg='blue',font=l).place(x=70,y=230)
    ps = Entry(creator, bg='white',font="arial 13",show='•',relief=FLAT,width=29)
    ps.place(x=70,y=260)
    Label(text="Re-Enter Password", bg='white', fg='blue',font=l).place(x=70,y=290)
    re_ps = Entry(creator, bg='white',font="arial 13",show='•',relief=FLAT,width=29)
    re_ps.place(x=70,y=325)
    Frame(creator, width=290, height=2,bg="#141414").place(x=70,y=217)
    Frame(creator, width=290, height=2,bg="#141414").place(x=70,y=283)
    Frame(creator, width=290, height=2,bg="#141414").place(x=70,y=348)

    eye_open = PhotoImage(file='open.png')
    open_eye1 = Button(creator, image=eye_open,relief=FLAT,bg='white',activebackground='white',border=0,cursor='hand2',command=show_pass1)
    open_eye1.place(x=342,y=263)
    open_eye2 = Button(creator, image=eye_open,relief=FLAT,bg='white',activebackground='white',border=0,cursor='hand2',command=show_pass2)
    open_eye2.place(x=342,y=328)

    
    Label(text="Select Any Question", bg='white', fg='blue',font=l).place(x=70,y=360)
    question_list = ["What is your favourite thing ?", "What is your DOB ?", "Which is your favourite place ?", "What is your favourite food ?"]
    asking = ttk.Combobox(creator, values=question_list,width=28,font='arial 10 bold')
    asking.place(x=100, y=390)
    asking.insert(0, question_list[0])
    ans = Entry(creator, bg='white', font='arial 13', relief=FLAT,width=24,justify=CENTER)
    ans.place(x=100, y=415)
    ans.insert(0, 'answer here')
    Frame(creator, width=220, height=2,bg="#141414").place(x=100,y=435)

    btn_font = Font(family="Times New Roman", size=13, weight='bold')
    save_new_user = Button(creator, text="Create", font=btn_font, relief=FLAT,borderwidth=0, bg='white',activebackground='white', fg='#6c22f5',cursor='hand2',command=before_login_page)
    save_new_user.place(x=180, y=460)
    save_new_user.bind("<Enter>", createOnHover)
    save_new_user.bind("<Leave>", createOffHover)

    my_font2 = Font(family="Times New Roman", size=10, weight='normal')
    closeBtn = Button(creator, text='Quit', font=my_font2,bg='white', fg='red',relief=FLAT,border=0,activebackground='white',cursor='hand1', command=quit)
    closeBtn.place(x=360,y=475)

    mainloop()
def jump():
    window1.after(10, main_win1)
    # main_win1()

def main_window():
    global e2,sb,window1,submit,cbtn,cr_new
    global e1, e2
    splash_root.destroy()
    window1 = Tk()
    window1.title("STUDENT MANAGEMENT SOFTWARE")
    app_width = 500
    app_height = 500
    screen_width = window1.winfo_screenwidth()
    screen_height = window1.winfo_screenheight()
    x = (screen_width/2) - (app_width/2)
    y = (screen_height/2) - (app_height/2)

    window1.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    # window1.config(bg="#9b7ede")
    window1.overrideredirect(True)
    my_font = Font(family="Comic Sans MS", size=20, weight='bold', slant='italic', underline=1)
    j = 0
    r = 0
    for i in range(100):
        c = str(222222+r)
        Frame(window1, width=10, height=500,bg='#'+c).place(x=j,y=0)
        j = j + 10
        r = r + 1
    main_label = Label(window1, text="Student Management", font=my_font,bg="#222222",fg="#03d5ff")
    main_label.pack(fill=X)
    Frame(window1, width=300, height=350, bg='white').place(x=100,y=80)
    us_img = PhotoImage(file='user1.png')
    op_img = PhotoImage(file='open.png')
    Label(window1, image=us_img, bg='white').place(x=190,y=90)
    l1 = Label(window1, text="Username", bg='white')
    l = ('console 13 bold')
    l1.config(font=l)
    l1.place(x=120, y = 220)
    
    e1 = Entry(window1, width=23, border=0)
    e1.config(font='courier 13')
    e1.place(x=120, y=250)
    e1.insert(0, "@")

    l2 = Label(window1, text="Password", bg='white')
    l2.config(font=l)
    l2.place(x=120, y= 280)

    e2 = Entry(window1, width=23, border=0, show="•")
    e2.config(font='courier 13')
    e2.place(x=120, y=310)

    Frame(window1, width=260, height=2,bg="#141414").place(x=120,y=270)
    Frame(window1, width=260, height=2,bg="#141414").place(x=120,y=330)

    sb = Button(window1, image=op_img,relief=FLAT,bg='white',activebackground='white',border=0,command=show_pass,cursor='hand2')
    sb.place(x=360,y=313)
    my_font1 = Font(family="Arial", size=10, weight='normal')
    submit = Button(window1, text="Login", relief=FLAT, bg='white',fg='#6c22f5',font=my_font1,activebackground='white',border=0,cursor='hand2')
    submit.place(x=225,y=350)
    submit.config(command=first_login)
    submit.bind("<Enter>", onClick)
    submit.bind("<Leave>", onLeave)
    my_font2 = Font(family="Times New Roman", size=10, weight='normal')
    cbtn = Button(text="Close",font=my_font2,bg='white',fg='red',relief=FLAT,border=0,activebackground='white',cursor='hand1',command=quit)
    cbtn.place(x=358, y= 405)
    cbtn.bind("<Enter>", closeClick)
    cbtn.bind("<Leave>", closeLeave)
    cr_new = Button(window1, text="Create New", relief=FLAT, bg='white',fg='#6c22f5',font=my_font1,activebackground='white',border=0,cursor='hand2',command=jump)
    cr_new.place(x=212,y=380)
    cr_new.bind("<Enter>",newOnClick)
    cr_new.bind("<Leave>",newOnClose)
    mainloop()

# Splah timer
splash_root.after(2000, main_window)


splash_root.mainloop()
