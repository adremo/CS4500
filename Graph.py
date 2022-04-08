# River Crossing Graph
# Author: Alex Chalmers
# External:
#   https://stackoverflow.com/questions/1535327/how-to-print-instances-of-a-class-using-print - overwriting default print
#   https://www.geeksforgeeks.org/convert-object-to-string-in-python/ - Converting object to string
#   https://www.tutorialspoint.com/python_data_structure/python_graphs.htm - Graph Data Structure

class Graph:
    def __init__(self, units={}):
        self.units = units

    def __str__(self):
        return str(self.units)

    def addUnit(self, name, enemies):
        self.units[name] = enemies

    def addUnit(self, unit):
        self.units[unit.name] = unit.diet

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
    
class Unit:
    def __init__(self, name, diet=[]):
        self.name = name
        self.diet = diet

#Testing
wolf = Unit("Wolf", ["Cow", "Sheep", "Rabbit"])
cow = Unit("Cow", ["Grass"])
sheep = Unit("Sheep", ["Grass"])
grass = Unit("Grass")
rabbit = Unit("Rabbit", ["Carrot"])
carrot = Unit("Carrot")
cat = Unit("Cat", ["Mouse"])
dog = Unit("Dog", ["Cat"])
mouse = Unit("Mouse", ["Cheese"])
cheese = Unit("Cheese")
chicken = Unit("Chicken", ["Seeds"])
seeds = Unit("Seeds")


graph = Graph()

graph.addUnit(cheese)
graph.addUnit(sheep)
graph.addUnit(seeds)

print(graph)
