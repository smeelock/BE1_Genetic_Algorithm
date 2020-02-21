from Ant import *
from Route import *
from City import *

from multiprocessing import Pool
import sys

class Civilization:
    def __init__(self, civ_name):
        self.__name = civ_name

        initial_nest = City("Initial Nest", 0, 0, is_nest=True, is_food=False) # initializing original nest
        self.__nestCities = [initial_nest]

        self.__foodCities = []

        self.__cities = [initial_nest]

        self.__routes = []
        # self.updateRoutes()

        self.__ants = []

        # ???
        # self.__natural_selection = 0 # les tours restants avant la prochaine sélection (pour l ’algorithme génétique)

    def go(self):
        pass

    # CAUTION: not working !!!!!!!!!!!!!!!!
    def stepForwardParallel(self):
        # Multi Threading : https://stackabuse.com/parallel-processing-in-python/
        def evaluateWalkFunctionOfAnt(ant):
            ant.walk()

        try :
            # Run this with a pool of 5 agents having a chunksize of 3 until finished
            agents = 3
            chunksize = len(self.__ants) / agents
            with Pool(processes=agents) as pool:
                result = pool.map(evaluateWalkFunctionOfAnt, self.__ants, chunksize)
        except :
            print("DEBUG: Error when trying to multithread. Running in single thread...\t")
            e = sys.exc_info()[0]
            self.stepForward()

    def stepForward(self):
        for ant in self.__ants :
            ant.walk()

    def addNest(self, nest_city):
        self.__nestCities.append(nest_city)
        self.__cities.append(nest_city)
        # self.updateRoutes()

    def addFoodCity(self, food_city):
        self.__foodCities.append(food_city)
        self.__cities.append(food_city)
        # self.updateRoutes()
    
    def addCity(self, city):
        self.__cities.append(city)
        # self.updateRoutes()       

    def addRoute(self, city1, city2):
        route = Route(city1, city2)
        self.__routes.append(route) 
        city1.addRouteFromCity(route)

    def addRoute(self, route):
        start_city = route.getStartCity()
        self.__routes.append(route)
        start_city.addRouteFromCity(route)

    def addAnt(self, ant):
        self.__ants.append(ant)

    def getInitialNest(self):
        return self.__nestCities[0]
    
    # def everyPossibleRoutes(self):
    #     """ Adds every possible routes between all cities """
    #     for city in self.__cities:
    #         for city2 in self.__cities:
    #             if city != city2:
    #                 r = Route(city, city2)
    #                 r_return = Route(city2, city) # the way back uses the same route, so must not be added in routes list 
    #                 if r not in self.__routes and r_return not in self.__routes:
    #                     self.__routes.append(r)
    #                     city.addRouteFromCity(r)
    
    def getCities(self):
        return self.__cities

    def getRoutes(self):
        return self.__routes
    
    def getAnts(self):
        return self.__ants
    
    
    # DEBUGGING 
    def printEnvironment(self):
        for route in self.__routes:
            print(route)

    def printAntsStatus(self):
        for ant in self.__ants:
            print(ant)

    def __str__(self):
        print(self.__name)
        self.printEnvironment()
        self.printAntsStatus()
        return ""
        
    