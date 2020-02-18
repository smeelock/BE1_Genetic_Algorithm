from Route import *
from City import *

import math
import random

class Ant:
    def __init__(self, initial_city, ID):
        self.__ID = ID

        self.__alpha = random.uniform(-5, 5)
        self.__beta = random.uniform(-5, 5)
        self.__gamma = random.uniform(-5, 5)
        self.__carry_food = False

        self.__current_city = initial_city

        self.__current_route = None
        self.__remaning_steps_on_current_route = None
        self.__currently_on_the_road = (self.__current_route != None)

        self.__step_capacity = 1 # default step capacity : takes 1 step at a time
        self.__routes_taken = [] # queue: to remember where the ant went (lifo)
                                    # because when arriving to food, wants to go home so taking the last route (not the most ancient one)

        # Takes new random route from current (initial) city based on trend
        self.takeRoute(random.choice(self.__current_city.getRoutesFromCity()))

    def getTrend(self, pheroLevel):
        """ According to pheromon level (float), chooses the best route to move forward towards objective """
        if not(self.__carry_food): # if not on the way back
            available_routes = []
            for route in self.__current_city.getRoutesFromCity():
                if route not in self.__routes_taken: # to avoid cycling between 2 cities
                    available_routes.append(route)

            # now chooses the routes with greatest phero level...
            route_with_max_pl = available_routes[0]
            max_pl = route_with_max_pl.getPheromonLevel()
            for route in available_routes[1:]: # we skip the first one because is considered as the best choice in the first place
                pl = route.getPheromonLevel()
                if pl > max_pl:
                    route_with_max_pl = route
                    max_pl = pl
            
            return route_with_max_pl

        else : # on the way back, simply pop out every routes in the routes_taken list
            return self.__routes_taken.pop()

    def catchFood(self):
        self.__carry_food = True

    def leaveFood(self):
        self.__carry_food = False

    def walk(self):
        self.__remaning_steps_on_current_route -= self.__step_capacity
        self.spreadPheromon()
        
        if self.__remaning_steps_on_current_route <= 0: # ant is arrived at the end of the current route
            # update current city and ant status
            self.__current_city = self.__current_route.getEndCity() if self.__current_city == self.__current_route.getStartCity() else self.__current_route.getStartCity()
            self.__currently_on_the_road = False # useless ???

            # Checks if city is foodCity or Nest or nothing...
            if self.__current_city.isFoodCity(): self.catchFood()
            # elif self.__current_city.isNest(): self.__init__(self.__current_city, self.__ID) # start over
            elif self.__current_city.isNest(): self.leaveFood()

            # Takes new route from new current city based on trend
            best_route = self.getTrend()
            self.takeRoute(best_route)
            
    def spreadPheromon(self): # when walking on edges, ants leaves pheromon where they go
        pl = self.__current_route.getPheromonLevel()
        pl = self.__alpha*math.sin(self.__beta*pl + self.__gamma)
        self.__current_route.setPheromonLevel(pl)

    def takeRoute(self, route):
        self.__current_route = route
        self.__remaning_steps_on_current_route = route.getLength()
        self.__routes_taken.append(route)
        self.__currently_on_the_road = True
    

    def __str__(self):
        return ("ID : {}\n\t \
               Current route : {}\n\t \
               Remaining steps : {}\n\t \
               Carrying food : {} \
                ".format(self.__ID, str(self.__current_route), self.__remaning_steps_on_current_route, self.__carry_food))   