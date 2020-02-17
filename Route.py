import City

class Route:
    def __init__(self, start_city, end_city):
        self.__start_city = start_city
        self.__end_city = end_city
        self.__pheromon_quantity = 0
        self.__length = 0
    
    def evaporationOfPheromon(self):
        pass

        