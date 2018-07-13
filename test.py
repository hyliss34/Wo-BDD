
import MyBDD,WoWApi
import inspect
import re

functions = inspect.getmembers(WoWApi, inspect.isfunction)

for func in functions:
    doc = func[1].__doc__
    l = re.sub(r"\(([^\)]+)\)", r"(:obj:`\1`)", doc.rstrip())
    print(l)




