from _todo.views.TkinterView import TkinterView as View
import _todo.models.model_readtxt as tasks
from _todo.models.model_readtxt import ReadTXT


data = ReadTXT()
view = View(data.getData())