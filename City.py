from Route import *

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
    
    def addRouteFromCity(self, route_to_destination):
        self.__routeFromMe.append(route_to_destination)
    
    def isFoodCity(self):
        return self.__is_food
    
    def isNest(self):
        return self.__is_nest

    def getX(self):
        return self.__X
    
    def getY(self):
        return self.__Y

    def __str__(self):
        return self.__name
        