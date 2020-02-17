class Ant:
    def __init__(self):
        self.__alpha = 0 
        self.__beta = 0
        self.__gamma = 0
        self.__carry_food = False
        self.__stepCapacity = 1 # default step capacity : takes 1 step at a time
 
    def getTrend(self, pheroLevel):
        """ According to pheromon level (float), chooses the best route to move forward towards objective """
        pass

    def catchFood(self):
        pass

    def leaveFood(self):
        pass

    def walk(self):
        pass



        