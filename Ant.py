from Route import *
from City import *

import math
import random
import numpy as np
import itertools

class Ant:
    def __init__(self, initial_city, alpha=np.random.uniform(-5, 5), beta=np.random.uniform(-5, 5), gamma=np.random.uniform(-5, 5), daddy=None, mommy=None):
        if not(daddy is None or mommy is None) :
            new_chromosome = np.random.choice([0, 1], size=3)
            [alpha, beta, gamma] = new_chromosome*daddy.getDNA() + (1-new_chromosome)*mommy.getDNA()
            # NOTE : 0 = takes mother's characteristics ; 1 = takes father's
        self.__ID = next(itertools.count())

        # DNA of ant (default : random)
        self.__alpha = alpha
        self.__beta = beta
        self.__gamma = gamma

        self.__carry_food = False
        self.__num_success = 0 # to count each time ant brings food back home (to se which one is the best worker)
        self.__num_exploration = 0 # to count each time ant takes same route (to see which one is the best explorer)

        self.__current_city = initial_city

        self.__current_route = None
        self.__remaning_steps_on_current_route = None
        self.__on_the_way_back = False

        self.__X = initial_city.getX()
        self.__Y = initial_city.getY()

        self.__step_capacity = 1 # default step capacity : takes 1 step at a time
        self.__routes_taken = [] # queue: to remember where the ant went (lifo)
                                    # because when arriving to food, wants to go home so taking the last route (not the most ancient one)

        self.__coords_history = [(initial_city.getX(), initial_city.getY())] # lst of tuples containing the history of (x, y) where ant was during simulation
        self.__routes_history = []

        # Takes new random route from current (initial) city based on trend
        self.takeRoute(np.random.choice(self.__current_city.getRoutesFromCity()))
        
    def mutation(self, initial_city):
        # NOTE : let's say mutation affect only 1 gene but selected as random
        [self.__alpha, self.__beta, self.__gamma][np.random.randint(0, 3)] = np.random.uniform(-5, 5) 
        self.__init__(initial_city, self.__alpha, self.__beta, self.__gamma)        

    def getTrend(self):
        """ According to pheromon level (float), chooses the best route to move forward towards objective """
        available_routes = []
        for route in self.__current_city.getRoutesFromCity():
            if route not in self.__routes_taken: # to avoid cycling between 2 cities
                available_routes.append(route)
        
        if len(available_routes) > 0:
            # now chooses the routes with greatest phero level...
            route_with_max_pl = random.choice(available_routes)
            max_pl = route_with_max_pl.getPheromonLevel()
            for route in available_routes[1:]: # we skip the first one because is considered as the best choice in the first place
                pl = route.getPheromonLevel()
                if pl > max_pl:
                    route_with_max_pl = route
                    max_pl = pl

        else : # ant is in a dead end (cannot move) --> return home
            self.__on_the_way_back = True
            return self.__routes_taken.pop()
        
        return route_with_max_pl

    def walk(self):
        self.__remaning_steps_on_current_route -= self.__step_capacity
        destination = self.__current_route.getEndCity() if self.__current_city == self.__current_route.getStartCity() else self.__current_route.getStartCity() 
        
        # Move towards objective - update ant's coordinates
        self.__coords_history.append((self.__X, self.__Y))
        l = self.__current_route.computeManhattanDistance()
        nb_of_steps = l/self.__step_capacity # let's divide total distance to travel by ant's capacity to move
                    # +1 is to be sure there is at least 1 step...
        delta_X = destination.getX()-self.__current_city.getX()
        delta_Y = destination.getY()-self.__current_city.getY()
        self.__X += delta_X/nb_of_steps
        self.__Y += delta_Y/nb_of_steps
        
        if self.__remaning_steps_on_current_route <= 0: # ant has arrived at the end of the current route
            # update current city and ant status
            self.__current_city = destination

            # Checks if city is foodCity or Nest or nothing...
            if self.__current_city.isFoodCity(): 
                self.__carry_food = True # catch food
                self.__on_the_way_back = True # needs to return home
            # elif self.__current_city.isNest(): self.__init__(self.__current_city, self.__ID) # start over
            elif self.__current_city.isNest(): 
                self.__carry_food = False # leave food
                self.__on_the_way_back = False

            # Takes new route from new current city
            best_route = self.__routes_taken.pop() if self.__on_the_way_back else self.getTrend()
            self.takeRoute(best_route)  

            
    def spreadPheromon(self): # when walking on edges, ants leaves pheromon where they go
        pl = self.__current_route.getPheromonLevel()
        pl = self.__alpha*np.sin(self.__beta*pl + self.__gamma)
        self.__current_route.setPheromonLevel(pl)

    def takeRoute(self, route):
        self.__current_route = route
        self.__remaning_steps_on_current_route = route.computeManhattanDistance()
        if not(self.__on_the_way_back) : 
            self.__routes_taken.append(route)
            self.__routes_history.append(route)

        # spread pheromon (only once) on the new choosen route
        if not(self.__on_the_way_back and not(self.__carry_food)) : # spread phero unless ant is coming home without food
            self.spreadPheromon()
    
    def getX(self):
        return self.__X
    
    def getY(self):
        return self.__Y
    
    def getID(self):
        return self.__ID

    def getLastPosition(self):
        return self.__coords_history[-1]
    
    def getDNA(self):
        return [self.__alpha, self.__beta, self.__gamma]
    
    def getFitness(self):
        return self.__num_success, self.__num_exploration
    
    # DEBUG printing
    def __str__(self):
        return ("ID : {}\n\t \
               Current route : {}\n\t \
               Remaining steps : {}\n\t \
               Carrying food : {}\n\t \
               On the way back : {} \
                ".format(self.__ID, str(self.__current_route), self.__remaning_steps_on_current_route, self.__carry_food, self.__on_the_way_back))   