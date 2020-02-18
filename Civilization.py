from Ant import *
from Route import *
from City import *

class Civilization:
    def __init__(self, civ_name):
        self.__name = civ_name

        initial_nest = City("Initial Nest", 0, 0, is_nest=True, is_food=False) # initializing original nest
        self.__nestCities = [initial_nest]

        self.__foodCities = []

        self.__cities = [initial_nest]

        self.__routes = []
        self.updateRoutes()

        self.__ants = []

        # ???
        # self.__natural_selection = 0 # les tours restants avant la prochaine sélection (pour l ’algorithme génétique)

    def go(self):
        pass

    def stepForward(self):
        for ant in self.__ants :
            ant.walk

    def addNest(self, nest_city):
        self.__nestCities.append(nest_city)
        self.__cities.append(nest_city)
        self.updateRoutes()

    def addFoodCity(self, food_city):
        self.__foodCities.append(food_city)
        self.__cities.append(food_city)
        self.updateRoutes()
    
    def addCity(self, city):
        self.__cities.append(city)
        self.updateRoutes()        

    def addAnt(self, ant):
        self.__ants.append(ant)

    def getInitialNest(self):
        return self.__nestCities[0]
    
    def updateRoutes(self):
        for city in self.__cities:
            for city2 in self.__cities:
                if city != city2:
                    r = Route(city, city2)
                    if r not in self.__routes:
                        self.__routes.append(r)
                        city.addRouteFromCity(r)
    
    
