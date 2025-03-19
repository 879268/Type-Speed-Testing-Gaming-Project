from tkinter import *
import random
from tkinter import messagebox

# List of words
words = ['Mango', 'apple', 'question', 'purpose','Eastpoint college of engineering','Program Outcomes', 'Class', 'Students', 'huManity', 'danger', 'no', 'Python', 'Stranger', 'name']

def labelSlider():
    global count, sliderWords
    text = 'Welcome to Typing Speed Game'
    if count >= len(text):
        count = 0
        sliderWords = ''
    sliderWords += text[count]
    count += 1
    fontLabel.configure(text=sliderWords)
    fontLabel.after(100, labelSlider)

def time():
    global timeleft, score, miss
    if timeleft >= 10:
        pass
    else:
        timeLabelCount.configure(fg='red')
    if timeleft > 0:
        timeleft -= 1
        timeLabelCount.configure(text=timeleft)
        timeLabelCount.after(1000, time)
    else:
        gamePlayDetailLabel.configure(text='Hit={} | Miss={} | Total Score={}'.format(score, miss, score-miss))
        rr = messagebox.askretrycancel('Notification', 'For Play Again Hit Retry Button')
        if rr == True:
            score = 0
            timeleft = 60
            miss = 0
            timeLabelCount.configure(text=timeleft)
            wordLabel.configure(text=words[0])
            scoreLabelCount.configure(text=score)

def startGame(event):
    global score, miss
    if timeleft == 60:
        time()
    gamePlayDetailLabel.configure(text='')
    if wordEntry.get().lower() == wordLabel['text'].lower():
        score += 1
        scoreLabelCount.configure(text=score)
    else:
        miss += 1
        print("miss:", miss)
    random.shuffle(words)
    wordLabel.configure(text=words[0])
    wordEntry.delete(0, END)

##### ROOT METHOD
root = Tk()
root.geometry('800x600+400+100')  # Screen size
root.configure(bg='powder blue')  # Background color
root.title('Typing Speed Test')

#### Variables
score = 0
timer = 60
count = 0
sliderWords = ''
miss = 0
timeleft = 60

#### LABEL METHODS
fontLabel = Label(root, text='', font=('arial', 25, 'italic bold'), bg='powder blue', fg='red', width=40)
fontLabel.place(x=70, y=10)  # fg=foreground
labelSlider()

random.shuffle(words)
wordLabel = Label(root, text=words[0], font=('arial', 40, 'italic bold'), bg='powder blue')
wordLabel.place(x=350, y=240)

scoreLabel = Label(root, text='Your Score:', font=('arial', 25, 'italic bold'), bg='powder blue')
scoreLabel.place(x=10, y=100)

scoreLabelCount = Label(root, text=score, font=('arial', 25, 'italic bold'), bg='powder blue', fg='blue')
scoreLabelCount.place(x=220, y=100)

timeLabel = Label(root, text='Time Left:', font=('arial', 25, 'italic bold'), bg='powder blue')
timeLabel.place(x=500, y=100)

timeLabelCount = Label(root, text=timer, font=('arial', 25, 'italic bold'), bg='powder blue', fg='blue')
timeLabelCount.place(x=680, y=100)

gamePlayDetailLabel = Label(root, text='Type Word And Hit Enter Button', font=('arial', 25, 'italic bold'), bg='powder blue', fg='dark gray')
gamePlayDetailLabel.place(x=170, y=450)

#### WORD ENTRY
wordEntry = Entry(root, font=('arial', 25, 'italic bold'), bd=10, justify='center')
wordEntry.place(x=225, y=320)
wordEntry.focus_set()

#### Bind Enter key to startGame
root.bind('<Return>', startGame)

root.mainloop()