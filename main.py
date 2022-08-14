import json
from tkinter import *  # predefined class
from difflib import get_close_matches
from tkinter import messagebox  # for message box
# difflib a predefined class and
# get_close_matches(a word,possibilities,n value,cutoff) is used to get the closest match
# it will return that a list of closest match here n is no. of values possibilities is list
# cutoff lies between 0-1.0 lower the value more will be matches

import pyttsx3  # text to speech convertor module works in offline

engine = pyttsx3.init()  # creating instance of engine class
voice = engine.getProperty('voices')  # storing the voices in variable voice
engine.setProperty('voice', voice[1].id)  # setting a female voice
engine.setProperty('rate', 128)

### FUNCTIONAL PART #########
def search():
    data = json.load(open('./data/data.json'))  # to load json file from data folder
    word = enterwordEntry.get()
    word.lower()
    if word in data:
        meaning = data[word]
        textarea.delete(1.0, END)
        for item in meaning:
            textarea.insert(END, u'\u2022' + item + '\n\n')  # insert is used to insert the items in textarea and END
            # from end u from bullets.
    elif len(get_close_matches(word, data.keys())) > 0:
        close_match = get_close_matches(word, data.keys())[0]
        res = messagebox.askyesno('Confirm', 'Did you mean ' + close_match + ' instead?')
        # message box return true on yes and false on no
        if res == True:
            enterwordEntry.delete(0, END)  # to delete the word in entry
            enterwordEntry.insert(END, close_match)
            textarea.delete(1.0, END)
            meaning = data[close_match]
            for item in meaning:
                textarea.insert(END, u'\u2022' + item + '\n\n')
        else:
            messagebox.showerror('Error', 'The Word does not exist please check it..')
            enterwordEntry.delete(0, END)
            textarea.delete(1.0, END)
    else:
        messagebox.showinfo('Information', 'The word does not exist')
        enterwordEntry.delete(0, END)
        textarea.delete(0, END)


def clear():
    enterwordEntry.delete(0, END)
    textarea.delete(1.0, END)


def iexit():
    res = messagebox.askyesno('Confirm', 'Sure You want to exit')
    if res:
        root.destroy()  # this will close the root window
    else:
        pass


def wordaudio():
    engine.say(enterwordEntry.get())  # for text to speech
    engine.runAndWait()  # to run our engine without this it will not run
def meaningaudio():
    engine.say(textarea.get(1.0, END))  # for text to speech
    engine.runAndWait()

# GUI PART##########################
root = Tk()  # an object of tkinter for gui
root.geometry('1000x626+100+30')  # defining the height and width and fixing its x,y position
root.title('Taking Dictionary by Mohd Riyan')  # Giving title to program
root.resizable(False, False)  # disable the resizability of wondows

bgimage = PhotoImage(file='./assets/bg.png')  # an object is made with imported  asset
bgLable = Label(root, image=bgimage)  # object of lable
bgLable.place(x=0, y=0)  # placing bg from 0,0

enterwordlable = Label(root, text='Enter Word', font=('castellar', 29, 'bold'), fg='red3', bg='whitesmoke')
# label with object with text
# font should be passed as tuple foreground or fg is for font color with tkinter color
# bg or backgroung for background
enterwordlable.place(x=530, y=20)  # place for positioning the label

enterwordEntry = Entry(root, font=('arial', 23, 'bold'), justify=CENTER, bd=8, relief=GROOVE)
# justify for centering the cusor
# relief for border style
# bd for border
enterwordEntry.place(x=510, y=80)

searchimage = PhotoImage(file='./assets/search.png')  # from flaticon.com
searchButton = Button(root, image=searchimage, bd=0, bg='whitesmoke', cursor='hand2', activebackground='whitesmoke',
                      command=search)
# Button class for button
searchButton.place(x=620, y=150)

micimage = PhotoImage(file='./assets/mic.png')
micButton = Button(root, image=micimage, bd=0, bg='whitesmoke', cursor='hand2', activebackground='whitesmoke',
                   command=wordaudio)
micButton.place(x=700, y=153)

meaninglable = Label(root, text='Meaning', font=('castellar', 29, 'bold'), fg='red3',
                     bg='whitesmoke')  # label objext with text
meaninglable.place(x=580, y=240)  # positioning the label

textarea = Text(root, width=34, height=8, font=('arial', 18, 'bold'), bd=8, relief=GROOVE)
textarea.place(x=460, y=300)

audioimage = PhotoImage(file='./assets/microphone.png')
audioButton = Button(root, image=micimage, bd=0, bg='whitesmoke', cursor='hand2', activebackground='whitesmoke',
                     command=meaningaudio)
audioButton.place(x=530, y=555)

clearimage = PhotoImage(file='./assets/clear.png')
clearButton = Button(root, image=clearimage, bd=0, bg='whitesmoke', cursor='hand2', activebackground='whitesmoke',
                     command=clear)
clearButton.place(x=660, y=555)

exitimage = PhotoImage(file='./assets/exit.png')
exitButton = Button(root, image=exitimage, bd=0, bg='whitesmoke', cursor='hand2', activebackground='whitesmoke',
                    command=iexit)
exitButton.place(x=790, y=555)


def enter_func(event):
    searchButton.invoke()  # this will cliked automatically


root.bind('<Return>', enter_func)  # here <Return> is for enter key

root.mainloop()  # to hold window everything before mainloop will be in loop and nothing will execute after it
# for bground pexels.com
# for voice commamd module in terminal type
# pip install pyttsx3
# hit enter
