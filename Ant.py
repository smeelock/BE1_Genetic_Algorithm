class Ant:
    def __init__(self):
        self.__alpha = 0 
        self.__beta = 0
        self.__gamma = 0
        self.__carry_food = False

        self.__x = 0
        self.__y = 0
        self.__stepCapacity = 1 # default step capacity : takes 1 step at a time
        self.__visitedCity = [] # queue: to remember where the ant went
 
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
        pass



        