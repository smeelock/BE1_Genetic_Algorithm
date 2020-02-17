import Route

class City:
    def __init__(self, name, x, y, is_nest=False, is_food=False):
        self.__name = name
        self.__is_nest = is_nest
        self.__is_food = is_food
        self.__X = x
        self.__Y = y

        self.__routeFromMe = [] # list of routes with start=this city

    def getRoutesFromCity(self):
        return self.__routeFromMe
    
    def isFoodCity(self):
        return self.__is_food
    
    def isNest(self):
        return self.__is_nest

        