import Civilization
import Ant
import Route
import City

import random

if __name__ == "__main__":
    # 1 nest, 1 food, 2 random other cities
    civ = Civilization("first try")
    rdm_cities = [City("city 1", 3, -2), City("city 2", 1, 1)]
    for city in rdm_cities: civ.addCity(city)
    civ.addFoodCity(City("Food City 1", 5, 5, is_nest=False, is_food=True))

    # 10 ants
    for i in range(10):
        name = "Ant {}".format(i)
        civ.addAnt(Ant(name, civ.getInitialNest(), ID=i))
    
    
