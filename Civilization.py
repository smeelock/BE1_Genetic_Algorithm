import City
import Ant
import Route

class Civilization:
    def __init__(self, civ_name):
        self.__name = civ_name

        initial_nest = City("Initial Nest", 0, 0, is_nest=True, is_food=False) # initializing original nest
        self.__nestCities = [initial_nest]

        self.__foodCities = []

        self.__cities = []
        self.updateCities()

        self.__ants = []

        # ???
        # self.__natural_selection = 0 # les tours restants avant la prochaine sélection (pour l ’algorithme génétique)

    def go(self):
        pass

    def stepForward(self):
        pass

    def addNestCity(self, nest_city):
        self.__nestCities.append(nest_city)
        self.updateCities()

    def addFood(self, food_city):
        self.__foodCities.append(food_city)
        self.updateCities()
    
    def updateCities(self): 
        """ Updates city list when adding/removing a city (either nest, food, or not) """
        self.__cities = self.__nestCities + self.__foodCities
    