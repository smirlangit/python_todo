from tkinter import *
from tkinter import messagebox
from _todo.models.ObjTask import ObjTask as Task

class TkinterView:
    root = None

    def __init__(self, data):
        # создаем окно
        self.root = Tk()
        self.show_tascs(data)
        self.root.mainloop()


    def show_tascs(self, data):
        parent = self.root
        el = Listbox(parent)

        for item in data:
            task = self.asTask(item)
            el.insert(END, task.title)
        el.pack(side = LEFT, fill = BOTH)
        return "all"

    # преобразовывает в тип данных TASK
    def asTask(self, task: Task) ->Task:
        return task

