import City

RHO = 0.5 # evaporation ratio

class Route:
    def __init__(self, start_city, end_city):
        self.__start_city = start_city
        self.__end_city = end_city
        self.__pheromon_level = 0
        self.__length = 0
    
    def evaporationOfPheromon(self):
        self.__pheromon_level *= (1 - RHO)
    
    def updatePheromonLevel(self, new_phero_level):
        self.__pheromon_level = new_phero_level
    
    def getPheromonLevel(self):
        return self.__pheromon_level

    def getLength(self):
        return self.__length
    
    def getStartCity(self):
        return self.__start_city
    
    def getEndCity(self):
        return self.__end_city

        