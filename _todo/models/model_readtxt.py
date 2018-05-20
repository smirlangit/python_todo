from configparser import ConfigParser
from os import path

from _todo.models.ObjTask import ObjTask as Task


# собирает все задачи из файла с задачами и оформляет в нужный массив
def getData():
    TODOFILE = "TODO.txt"
    file_exist = path.exists(TODOFILE)
    if (file_exist):
            # загрузка данных из списка задач
            conf = ConfigParser()
            conf.read(TODOFILE, encoding="utf-8")
            sections = conf.sections()

            # собираем данные для всех секций
            data = []
            for section in sections:
                task = Task()

                task.title = conf.get(section, "title")
                task.description = conf.get(section, "desc")
                task.status = conf.get(section, "status")
                task.date_start = conf.get(section, "date_start")
                task.date_end = conf.get(section, "date_end")

                data.append(task)

            return data