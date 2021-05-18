from tkinter import *
from random import randint 

root = Tk()
root.title("Cистемы счисления")
root.geometry("700x500")
root.resizable(height= False,width= False)


def home():
    label_get.destroy()
    text_box_get.destroy()
    label1.destroy()
    label2.destroy()
    iscc_box.destroy()
    vcc_box.destroy()
    label_out.destroy()
    text_box_out.destroy()
    convert_button.destroy()
    back_button.destroy()
    label_resh.destroy()
    label_title.destroy()
    #frame.grid_forget()
    #canvas.delete("all")
    r_var.set(-1)
    global radio_test
    radio_test = Radiobutton(root, text='Тренировочный', command=test, value=0, variable = r_var)
    #radio_test.place(relx=0.53, rely=0.30, anchor="e")
    radio_test.grid(column=0, row=0, sticky=W)
    #//radio_test.pack(side=TOP)
    global radio_control    
    radio_control = Radiobutton(root, text='Контрольный', command=control, value=1, variable = r_var)
    #radio_control.place(relx=0.53, rely=0.38, anchor="e")
    radio_control.grid(column=0, row=1, sticky=W)
    #//radio_control.pack(side=TOP)

def home1():
    back_button.destroy()
    label_proverka.destroy()
    label_contr.destroy()
    label_contr1.destroy()
    label_contr2.destroy()
    text_box_out1.destroy()
    convert_button1.destroy()
    r_var.set(-1)
    global radio_test
    radio_test = Radiobutton(root, text='Тренировочный', command=test, value=0, variable = r_var)
    #radio_test.place(relx=0.53, rely=0.30, anchor="e")
    radio_test.grid(column=0, row=0, sticky=W)
    #//radio_test.pack(side=TOP)
    global radio_control    
    radio_control = Radiobutton(root, text='Контрольный', command=control, value=1, variable = r_var)
    #radio_control.place(relx=0.53, rely=0.38, anchor="e")
    radio_control.grid(column=0, row=1, sticky=W)
    #//radio_control.pack(side=TOP)

def test():
    radio_test.destroy()
    radio_control.destroy()
    #frame.pack(fill=BOTH, expand=1, side=TOP)
    #frame.place()
    global s_resh
    s_resh = ''
    global label_resh
    label_resh = Label(root,pady=5,text='')
    label_resh.place(relx=.6, rely=.1)    
    global label_title
    label_title = Label(root,pady=5,text='Решение')
    label_title.place(relx=.6, rely=.0)
    #label_resh = Label(root,pady=5,textvar=text_resh)
    def clear():
        text_box_out.delete(0, END)
 
     #Функция перевода в другие.
    def ConvertFromDec(value, num_sym_st, num_sym_end): 
        text_box_out.config(state="normal")
        clear()
        if  (num_sym_end <=10):
            text_box_out.insert(0, foo_all(value,num_sym_st,num_sym_end))
            global s_resh
            s_resh += 'Затем остатки в обратном порядке записать ' + '\n'
            label_resh.config(text=s_resh) 
            
        if (num_sym_end >10):
            text_box_out.insert(0, foo_all(value,num_sym_st,num_sym_end))
            s_resh += 'Затем остатки в обратном порядке записать ' + '\n'
            label_resh.config(text=s_resh) 
        text_box_out.config(state="readonly")
    
    #Если изначальная с.с или конечная с.с не 10-ая, то
        
    def foo(num, radix):
        return( int(num, radix))
    def foo_all(num, num_sym_st,num_sym_end):
        s = ''
        global s_resh
        s_resh = ''
        label_resh.config(text='') 
        b = int(foo(num,num_sym_st))
        while b > 0:
            s1=''
            if (b % num_sym_end) == 10:
                s1 = 'A'
                s_resh += 'Остаток от деления на  ' + str(num_sym_end) + ' = ' + s1 + '\n'
                label_resh.config(text=s_resh)
            elif (b % num_sym_end) == 11:
                s1 = 'B'
                s_resh += 'Остаток от деления на  ' + str(num_sym_end) + ' = ' + s1 + '\n'
                label_resh.config(text=s_resh)
            elif (b % num_sym_end) == 12:
                s1 = 'C'
                s_resh += 'Остаток от деления на  ' + str(num_sym_end) + ' = ' + s1 + '\n'
                label_resh.config(text=s_resh)
            elif (b % num_sym_end) == 13:
                s1 = 'D'
                s_resh += 'Остаток от деления на  ' + str(num_sym_end) + ' = ' + s1 + '\n'
                label_resh.config(text=s_resh)
            elif (b % num_sym_end) == 14:
                s1 = 'E'
                s_resh += 'Остаток от деления на  ' + str(num_sym_end) + ' = ' + s1 + '\n'
                label_resh.config(text=s_resh)
            elif (b % num_sym_end) == 15:
                s1 = 'F'
                s_resh += 'Остаток от деления на  ' + str(num_sym_end) + ' = ' + s1 + '\n'
                label_resh.config(text=s_resh)
            else:
                s1 = str(b % num_sym_end)
                s_resh += 'Остаток от деления на  ' + str(num_sym_end) + ' = ' + s1 + '\n'
                label_resh.config(text=s_resh)
            s = s1 + s
            b //=num_sym_end
        return s
        
    text = StringVar()
    text_out = StringVar()   
    
    global label_get
    label_get = Label(root,text="Введите число")
    label_get.place(relx=.15, rely=.1)
    global text_box_get
    text_box_get = Entry(root,font=48, justify=RIGHT, textvariable=text)
    text_box_get.place(relheight=0.1, relwidth=0.25, relx=.2, rely=.2, anchor="c")
 
    global label1 
    label1 = Label(root,text="Из")
    label1.place(relx=.14, rely=.35)
    global label2     
    label2 = Label(root,text="В")
    label2.place(relx=.24, rely=.35)    

    textis = StringVar()
    textv = StringVar()

    global iscc_box
    iscc_box = Entry(root,font=48, justify=RIGHT, textvariable=textis)
    iscc_box.place(relheight=0.1, relwidth=0.1, relx=.2, rely=.48, anchor="e")
    global vcc_box
    vcc_box = Entry(root,font=48, justify=RIGHT, textvariable=textv)
    vcc_box.place(relheight=0.1, relwidth=0.1, relx=.2, rely=.48, anchor="w")

    global label_out
    label_out = Label(root,text="Ответ")
    label_out.place(relx=.18, rely=.70)
    global text_box_out
    text_box_out = Entry(root,font=48, justify=RIGHT, textvariable=text_out, state="readonly")
    text_box_out.place(relheight=0.1, relwidth=0.25, relx=.2, rely=.8, anchor="c")
    global convert_button
    convert_button = Button(root,text="Перевести", command=lambda: ConvertFromDec(text.get(), int(textis.get()), int(textv.get())))
    convert_button.place(relx=.2, rely=.58, anchor="c")
    global back_button
    back_button = Button(root,text="Назад", command=home)
    back_button.place(relx=.055, rely=.04, anchor="c")

def control():
    radio_test.destroy()
    radio_control.destroy()
    global label_contr
    label_contr = Label(root,text="")
    label_contr.place(relx=.18, rely=.10)
    global label_contr1
    label_contr1 = Label(root,text="")
    label_contr1.place(relx=.20, rely=.70)
    global back_button
    back_button = Button(root,text="Назад", command=home1)
    back_button.place(relx=.055, rely=.04, anchor="c")
    global label_proverka
    label_proverka = Label(root,text="")
    label_proverka.place(relx=.32, rely=.18)
    a=randint(2,16)
    p=randint(2,16)
    c=randint(1,3)
    print(a,p,c)
    s2=""
    #Перевод в контрольном режиме
    for i in range(1,c+1):
        s2+=str(randint(1,a-1))
    label_contr.config(text=s2)
    print(s2,"-")
    s6="Переведите из " + str(a)+"-чной C.C." + " в " + str(p)+"-чную С.С" + " число " + str(s2)
    global label_contr2
    label_contr2 = Label(root,text=s6)
    label_contr2.place(relx=.05, rely=.10)
    
    def ConvertFromDec(s2,a,p):
        global s4
        if  (p <=10):
            s4= foo_all(s2,a,p)
            label_contr1.config(text=s4)
            
        if (p >10):
            s4= foo_all(s2,a,p)
            label_contr1.config(text=s4)
    
    #Если изначальная с.с или конечная с.с не 10-ая, то
        
    def foo(num, radix):
        return( int(num, radix))
    def proverka(mi):
        if mi!='':
            if mi==s4:
                label_proverka.config(text="Верно")
            if mi!=s4:
                label_proverka.config(text="Не верно")
        else:
            label_proverka.config(text="Введите ответ")
    def foo_all(schislo, a,p):
        s = ''
        b = int(foo(schislo,a))
        while b > 0:
            s1=''
            if (b % p) == 10:
                s1 = 'A'
                
            elif (b % p) == 11:
                s1 = 'B'
                
            elif (b % p) == 12:
                s1 = 'C'
               
            elif (b % p) == 13:
                s1 = 'D'
               
            elif (b % p) == 14:
                 s1 = 'E'
                
            elif (b % p) == 15:
                s1 = 'F'
                
            else:
                s1 = str(b % p)
                
            s = s1 + s
            b //=p
        return s
    ConvertFromDec(s2,a,p)
    text_contl = StringVar()   
    global text_box_out1
    text_box_out1 = Entry(root,font=48, justify=RIGHT, textvariable=text_contl)
    text_box_out1.place(relheight=0.1, relwidth=0.25, relx=.05, rely=.15)
    
    global convert_button1
    convert_button1 = Button(root,text="Проверить", command=lambda: proverka(text_box_out1.get()))
    convert_button1.place(relx=.17, rely=.30, anchor="c")
    

r_var = IntVar()
r_var.set(-1) 
radio_test = Radiobutton(root, text='Тренировочный', command=test, value=0, variable = r_var)
#radio_test.place(relx=0.56, rely=0.30, anchor="e")
#radio_test.pack(side=TOP)
radio_test.grid(column=0, row=0, sticky=W)
radio_control = Radiobutton(root, text='Контрольный', command=control, value=1, variable = r_var)
#radio_control.place(relx=0.53, rely=0.38, anchor="e")
#radio_control.pack(side=TOP)
radio_control.grid(column=0, row=1, sticky=W)

root.mainloop()
