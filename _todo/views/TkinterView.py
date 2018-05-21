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
        el = Listbox(parent, name = "lb")
        el.bind('<<ListboxSelect>>', self.taskSelect)

        for item in data:
            task = self.asTask(item)
            el.insert(END, task.title)
        el.pack(side = LEFT, fill = BOTH)
        el.bind('<<ListboxSelect>>', self.showDescription("dfdf"))
        self.showDescription(self.asTask(data[0]).description)


    def taskSelect(self, event):
        self.showDescription("asd")


    # преобразовывает в тип данных TASK
    def asTask(self, task: Task) ->Task:
        return task

    def addDescription(self):
        parent = self.root
        el = Text(parent)
        el.pack(side=RIGHT, expand=YES, fill=BOTH)
        self.description = el

    def showDescription(self, text):
        el = self.description
        el.insert(1.0, text)





