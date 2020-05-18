import wikipedia
from tkinter import *
from tkinter.messagebox import showinfo


#search function
def search_content():
    search = entry.get()
    result = wikipedia.summary(search)
    showinfo("Wikipedia Search",result)
    
#creating window
win = Tk()
win.title("Wikipedia Search")
win.geometry("300x80")

#creating Label
label = Label(win, text="Wikipedia Search :")
label.grid(row=0,column=0)

#creating entry box
entry = Entry(win)
entry.grid(row=1,column=0)

#creating Button
button = Button(win,text="Search", command=search_content)
button.grid(row=1,column=1,padx=10)

win.mainloop()