from tkinter import *
from tkinter import messagebox
import tkinter


tasks_list = []
counter = 1

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
    
    TextArea.insert('end -1 chars', "[ " + str(counter) + " ] " + content)
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
        TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i])

if __name__ == "__main__" :
    

    root = tkinter.Tk(className=' Webie: Your productivity sidechick ')

    root.geometry('600x430') 
    
    enterTask = Label(root, text = "... Add your Tasks ...")
    CenterTask = Label(root, text = "Press Enter to submit")
 
    enterTaskField = Entry(root)
 
    Submit = Button(root, text = "Submit", command = insertTask)
 
    TextArea = Text(root, height = 10, width = 18, font = "lucida 13")
    taskNumber = Label(root, text = "Delete Task Number")
                        
    taskNumberField = Text(root, height = 1, width = 2, font = "lucida 13")
    
    deltask = Label(root, text = "Press Delete to remove")
    done = Button(root, text = "Done",  command = delete)
    root.bind('<Return>', insertTask)
    root.bind('<Delete>',delete)

 
    enterTask.place(x = 40, y = 70)
    CenterTask.place(x = 25, y = 90)
               
               
    enterTaskField.place(x = 25, y = 110)
                        
    Submit.place(x = 155, y = 110)
         
    TextArea.place(x = 25, y = 140)
                        
    taskNumber.place(x = 25, y = 350)
                        
    taskNumberField.place(x = 150, y = 350)
    deltask.place(x=25,y=380)

    done.place(x = 155, y = 380)
    
    root.mainloop()