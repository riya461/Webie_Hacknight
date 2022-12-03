from tkinter import *
from tkinter import messagebox
import tkinter
import math 
from PIL import Image, ImageTk

tasks_list = []
counter = 1
PINK = "#e2979c"
RED = "#e7305b"
BROWN = "#964B00"
BLACK = "#002240"
FONT_NAME = "Courier"
WORK_MIN = 50
SHORT_BREAK_MIN = 10
reps = 0
timer = None

def inputError() :
    if enterTaskField.get() == "" :
        messagebox.showinfo("Enter","I dont think there can be an empty task!")
        return 0
    return 1

def insertTask(e = 0):
    global counter 
    value = inputError()
    if value == 0:
        return
    content = enterTaskField.get() + "\n"
    tasks_list.append(content)
    
    TextArea.insert('end -1 chars', "( " + str(counter) + " ) " + content)
    counter += 1

    enterTaskField.delete(0, END)

def delete(e = 0) :
    global counter
    if len(tasks_list) == 0 :
        messagebox.showinfo("No task","Hey... there is no unfinished business!")
        return
    number = taskNumberField.get(1.0, END)
    if number == "\n" :
        messagebox.showerror("input error")
        return
     
    else :
        task_no = int(number)

    taskNumberField.delete(0.0, END)

    tasks_list.pop(task_no - 1)
 
    counter -= 1
     
    TextArea.delete(1.0, END)
 
    for i in range(len(tasks_list)) :
        TextArea.insert('end -1 chars', "( " + str(i + 1) + " ) " + tasks_list[i])
def clear_screen():
    pass
def reset_timer():
    root.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text=" TIMER ")
    global reps
    reps = 0

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    
    
    if reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text=" BREAK ", fg=PINK)
    
    else:
        count_down(work_sec)
        title_label.config(text=" WORK. ", fg=BROWN)
    if reps == 3:
        clear_screen()


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = root.after(1000, count_down, count - 1)
    else:
        start_timer()
        


if __name__ == "__main__" :
    

    root = tkinter.Tk(className=' Webie: Your productivity sidechick ')

    root.geometry('600x430') 
    root.resizable(False,False)
    
    b = ImageTk.PhotoImage(file = "bg.jpeg")   
    limg= Label(root, i=b)
    limg.pack()
    
    
    
    enterTask = Label(text=" TASKS ", fg=BROWN, font=(FONT_NAME, 30))
    CenterTask = Label(root, text = "Press Enter key to submit")
 
    enterTaskField = Entry(root)
 
    Submit = Button(root, text = "Submit", command = insertTask)
 
    TextArea = Text(root, height = 10, width = 18, font = "lucida 13")
    taskNumber = Label(root, text = "Delete Task Number")
                        
    taskNumberField = Text(root, height = 1, width = 2, font = "lucida 13")
    
    deltask = Label(root, text = "Press Delete key to remove")
    done = Button(root, text = "Done",  command = delete)
    root.bind('<Return>', insertTask)
    root.bind('<Delete>',delete)

 
    enterTask.place(x = 15, y = 30)
    CenterTask.place(x = 25, y = 85)
               
               
    enterTaskField.place(x = 25, y = 110)
                        
    Submit.place(x = 155, y = 110)
         
    TextArea.place(x = 25, y = 140)
                        
    taskNumber.place(x = 25, y = 350)
                        
    taskNumberField.place(x = 150, y = 350)
    deltask.place(x=25,y=380)

    done.place(x = 175, y = 380)

    title_label = Label(text=" TIMER ", fg=BROWN, font=(FONT_NAME, 30))
    title_label.place(x = 370, y = 30)
    canvas = Canvas(root)
    canvas.pack()
    timer_text = canvas.create_text(100, 50, text="00:00", fill="black", font=(FONT_NAME, 35, "bold"))
    canvas.place(x=285, y=90)
    start_button = Button(text=" Start ", highlightthickness=0, command=start_timer)
    start_button.place(x=380, y=250)
    reset_button = Button(text=" Reset ", highlightthickness=0, command = reset_timer)
    reset_button.place(x = 440, y = 250)






    root.mainloop()