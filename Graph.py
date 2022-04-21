# River Crossing Graph
# Author: Alex Chalmers
# External:
#   https://stackoverflow.com/questions/1535327/how-to-print-instances-of-a-class-using-print - overwriting default print
#   https://www.geeksforgeeks.org/convert-object-to-string-in-python/ - Converting object to string
#   https://www.tutorialspoint.com/python_data_structure/python_graphs.htm - Graph Data Structure
#   https://stackoverflow.com/questions/4859292/how-to-get-a-random-value-from-dictionary - Getting a random element of a dictionary (Garrat and Seaux's Comments)

import random

class Graph:
    def __init__(self, units={}):
        self.units = units
        self.presets = {
            #Eats Many
            "Fox":["Cat", "Chicken", "Cow", "Sheep", "Mouse"],
            "Wolf": ["Cow", "Sheep", "Rabbit", "Goose"],
            "Snake": ["Rabbit", "Mouse", "Squirrel", "Frogs"],


            #Eats a Few
            "Rabbit":["Carrot", "Grass"],
            "Goat": ["Broccoli", "Grass"],
            "Monkey":["Banana", "Fruit"],
            "Owl": ["Mouse", "Squirrel"],

            #Eats One
            "Cow": ["Grass"],
            "Sheep": ["Grass"],
            "Cat": ["Mouse"],
            "Dog": ["Cat"],
            "Mouse": ["Cheese"],
            "Chicken": ["Seeds"],
            "Goose": ["Grass"],
            "Squirrel": ["Nuts"],
            "Frog": ["Bug"],
            "Bug": ["Grass"],

            #Eats None
            "Grass": [],
            "Carrot": [],
            "Cheese": [],
            "Seeds":[],
            "Broccoli": [],
            "Banana": [],
            "Fruit":[],
            "Nuts": []

        }

    def __str__(self):
        return str(self.units)

    def addUnit(self, name, diet):
        self.units[name] = diet

    def getRandomUnit(self):
        return random.choice(list(self.presets.items()))


    def generateGraph(self, unitCount):
        self.units.clear() # Necessary if generateGraph() is called multiple times(to get graph with min boat size of 1)
        for number in range(0, unitCount):
            buffer = self.getRandomUnit()

            while(self.contains(buffer)):
                buffer = self.getRandomUnit()
            self.addUnit(buffer[0], buffer[1])

    def contains(self, unitName):
        for unit in self.units:
            if(unit == unitName):
                return True
        return False

    def checkValid(self):
        for unit in self.units:
            for enemy in self.units.get(unit):
                if(self.contains(enemy)):
                    return False
        return True
    
    def getMinimumBoatSize(self):
        minBoatSize = -1

        for unit in self.units:
            for prey in self.units[unit]:
                print(prey)
                if(self.contains(prey)):
                    minBoatSize += 1
        return minBoatSize

    def loadImage(self, unitName):
        print("NYI")

    def getOptimalPath(self):
        optimalTurn = {}

        #get initial predators
        for unit in self.units:
            for prey in self.units[unit]:
                if(self.contains(prey)):
                    optimalTurn.dd(unit)

        #Check for overlapping

        return optimalTurn



graph = Graph()

graph.generateGraph(3)
