import Route

class City:
    def __init__(self, name, x, y, is_nest=False, is_food=False):
        self.__name = name
        self.__is_nest = is_nest
        self.__is_food = is_food
        self.__X = x
        self.__Y = y

        self.__pathFromMe = [] # list of routes with start=this city

    def getPathFromCity(self):
        return self.__pathFromMe

        