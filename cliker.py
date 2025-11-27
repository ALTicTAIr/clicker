from tkinter import *
win2 = Tk()
win2.geometry("600x600")
win2.resizable(True,True)
win2.title("test window")
win2.config(bg='lightblue')
tex = 0
tex = int(tex)
label = Label(win2,
text=tex, 
font=("Arial", 20))
label.place(x=50, y=50)

def greet(w):
    global tex
    tex += w
    label.config(text=tex)

btn = Button(win2,
text= 'нажми меня',
command = lambda: greet(1),      
font = ('Comic Sans MS', 20, 'italic'),
bg = 'lime',
activebackground = 'red',
activeforeground = 'white'
)
btn.place(x=150, y=150)

win2.mainloop()