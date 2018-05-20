from _todo.views.TkinterView import TkinterView as View
import _todo.models.model_readtxt as tasks


data = tasks.getData()
view = View(data)