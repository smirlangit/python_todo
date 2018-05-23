from configparser import ConfigParser
from os import path

from _todo.models.ObjTask import ObjTask as Task


# собирает все задачи из файла с задачами и оформляет в массив
class ReadTXT:

    TODOfile = "TODO.txt"
    conf = None

    def __init__(self):
        self.conf = ConfigParser()

    def getData(self):
        TODOFILE = self.TODOfile
        file_exist = path.exists(TODOFILE)
        if (file_exist):
            # загрузка данных из списка задач
            conf = self.conf
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

    def saveData(self, dataArray):
        TODOFILE = self.TODOfile
        file_exist = path.exists(TODOFILE)


        if (file_exist):
            conf = self.conf
            data = []
            data["zzz"]={"one":"1", "two":"2"}
            conf.write(TODOFILE, "w")
            return