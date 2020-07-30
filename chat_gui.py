#Creating GUI with tkinter
import tkinter
import main
from tkinter import *
from tkmacosx import Button
def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    if msg != '':
            ChatLog.config(state=NORMAL)
            ChatLog.tag_configure("black", foreground="black")
            ChatLog.tag_configure("blue", foreground="blue")
            ChatLog.insert(END, "You: " + msg + '\n\n', "black")
            res = main.chatbot_response(msg)
            ChatLog.insert(END, "Cora: " + res + '\n\n', "blue")
            ChatLog.config(font=("Verdana", 12 ))
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)
base = Tk()
base.title("Your Personal Retirement Assistant")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)
#Create Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)
ChatLog.config(state=DISABLED)
#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview)
ChatLog['yscrollcommand'] = scrollbar.set
#Create Button to send message
SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width=120, height=5,
                    bd=0, bg='#add8E6', activebackground='#009acd',fg='#ffffff',
                    command= send )
#Create the box to enter message
EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")
#EntryBox.bind("<Return>", send)
#Place all components on the screen
scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)
# ChatLog.insert(END, "Cora: Hi, I'm Cora--Your Personal Retirement Assistant." + '\n\n')
base.mainloop()
