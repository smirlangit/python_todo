from tkinter import *
from tkinter import messagebox
from _todo.models.ObjTask import ObjTask as Task

class TkinterView:
    root = None
    description = None

    def __init__(self, data):
        # создаем окно
        self.root = Tk()
        self.addDescription()
        self.show_tascs(data)

        self.root.mainloop()


    def show_tascs(self, data):
        parent = self.root


        for item in data:
            prop = StringVar()

            task = self.asTask(item)
            prop.set(str(task.title))

            el = Button(parent, text = task.title)

            data = {"title":task.title, "description":task.description}

            el.bind("<Button-1>", lambda event, arg = data: self.showDescription(arg) )
            el.pack(side = TOP, fill = BOTH)

    def showDescription(self, arg):
        el = self.description
        el.delete(1.0, END)
        el.insert(INSERT, arg["description"])

    # преобразовывает в тип данных TASK
    def asTask(self, task: Task) ->Task:
        return task

    def addDescription(self):
        parent = self.root
        el = Text(parent)
        el.pack(side=RIGHT, expand=YES, fill=BOTH)
        self.description = el







