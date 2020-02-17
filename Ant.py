import Route
import math
import random

class Ant:
    def __init__(self, initial_city):
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
    
    def getTrend(self, pheroLevel):
        """ According to pheromon level (float), chooses the best route to move forward towards objective """
        pass

    def catchFood(self):
        pass

    def leaveFood(self):
        pass

    def walk(self):
        pass

    def spreadPheronom(self): # when walking on edges, ants leaves pheromon where they go
        pl = self.__current_route.getPheromonLevel()
        pl = self.__alpha*math.sin(self.__beta*pl + self.__gamma)
        self.__current_route.updatePheromonLevel(pl)

    def takeRoute(self, route):
        self.__current_route = route
        self.__remaning_steps_on_current_route = route.getLength()
        self.__routes_taken.append(route)



        