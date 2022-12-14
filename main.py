# Disappearing text writing app.
from tkinter import *

# Create Tkinter UI for the app.
root = Tk()
root.title("The Most Dangerous Writing")
root.geometry('740x800')
root.config(bg="#181D31")
root.option_add('*Label.Font', "consolas 15")
root.option_add('*Text.Font', "consolas 15")


# Create text box
label = Label(text="Dangerous writing",fg="red",bg="#181D31")
label.grid(row=0,column=0,padx=75,pady=40)
label2 = Label(text="Don’t stop writing, or all progress will be lost.",fg="#678983",bg="#181D31")
label2.grid(row=1,column=0,padx=75,pady=20)
text_box = Text(root, width=50,fg="#F0E9D2",bg="#181D31",wrap=WORD)
text_box.grid(row=2,column=0,padx=75,pady=20)

# Track user input every second.
stop_writing_id = None


def wait(event):
    global stop_writing_id
    if stop_writing_id is not None:
        root.after_cancel(stop_writing_id)
    # If user stop writing for 5 seconds then clear all textbox.
    stop_writing_id = root.after(5000, done)


# Clearing function

def done():
    text_box.delete('1.0', 'end')


# Track and start function by user start typing
text_box.bind('<Key>', wait)


root.mainloop()
