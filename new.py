


def submit():
    print('you love:')
    print(listbox.get(listbox.curselection()))
def add():
    listbox.insert(listbox.size(),entry.get())
    listbox.config(height=listbox.size())


from tkinter import*
window=Tk()
listbox=Listbox(window,bg="black",fg="white")

listbox.pack()
listbox.insert(0,'Dogs')
listbox.insert(1,'Cats')
listbox.insert(2,'Rabbit')
listbox.insert(3,'Birds')

listbox.config(font=('Impact',20),height= listbox.size())
entry= Entry(window)
entry.pack()

button=Button(window,text='submit',command=submit,bg='blue',fg='white',font=('Impact',10))
button.pack()

add1button =Button(window,text='Add',command=add,bg='blue',fg='white',font=('Impact',10))
add1button.pack()



window.mainloop()

