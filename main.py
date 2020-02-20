from Civilization import *
from Ant import *
from Route import *
from City import *

from AppResults import *

import random
import time

if __name__ == "__main__":
    # 1 nest, 1 food, 2 random other cities
    # cities coordinates are in [-100 100]
    civ = Civilization("first try")
    rdm_cities = [City("city 1", -30, -20), City("city 2", -10, 10), City("city 3", 42, -66)]
    food_city = City("Food City 1", 100, 100, is_nest=False, is_food=True)
    for i in range(len(rdm_cities)): 
        civ.addCity(rdm_cities[i])
        civ.addRoute(Route(rdm_cities[i-1], rdm_cities[i]))
    civ.addFoodCity(food_city)
    civ.addRoute(Route(rdm_cities[-1], food_city)) # route to objective city (food)
    civ.addRoute(Route(civ.getInitialNest(), rdm_cities[1])) # route to original nest
    civ.addRoute(Route(civ.getInitialNest(), rdm_cities[2])) # route to original nest


    # 10 ants
    for i in range(10):
        civ.addAnt(Ant(civ.getInitialNest(), ID=i))

    win = MainWindow(civ, civ.getCities(), civ.getRoutes())
    win.mainloop()

    
    # start_time = time.time()
    # while (time.time()-start_time < 1.): # 1 seconds simulation
    #     print("===== Time {}s =====".format(time.time()-start_time))
    #     civ.stepForward()
    #     print(civ)
    

