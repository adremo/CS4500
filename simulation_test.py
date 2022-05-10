# Andrew Morris
# 4/20/2022
# CS 4500 Spring 2022
# Unit tests for simulation.py
# Central Data Structures: Dictionaries used for testing simulation
# External Files: None

import unittest
from simulation import *
import Graph

class Test(unittest.TestCase):
    # Test for presence of images required for simulation.py
    def test_resource_loads(self):
        for unit in unit_images:
            try:
                print(type(unit_images[unit]))
            except:
                self.fail()

    # Tester can run the simulation and immediately exit, in which case the function tests for the correct 
    # return value from run_simulation() function. Otherwise, the tester can test the graphics/sounds/UI/logic 
    # of the running simulation (no music should play as music playback starts through main menu in main.py)
    def test_run_simulation(self):
        test_graph = Graph.Graph()
        
        min_boat_size = 0
        while min_boat_size < 1:
            test_graph.generateGraph(5)
            min_boat_size = test_graph.getMinimumBoatSize()
        
        print(test_graph.units)
        print(min_boat_size)
                
        turn_count = run_simulation(test_graph.units, min_boat_size)
        if turn_count < 3:
            print("Game exited early")
            self.assertEqual(turn_count, -1)
        else:
            print("Game won, turns used: " + str(turn_count))
        
    # Checks return value from check_unit_conflicts() from simulation
    def test_check_unit_conflicts(self):
        # Testing graph with 3 units containing no conflicts
        test_graph = Graph.Graph()
        conflict_count = 0
        min_boat_size = 0
        
        # conflict count is equal to 0 when minimum boat size is -1
        while min_boat_size != -1:
            test_graph.generateGraph(3)
            min_boat_size = test_graph.getMinimumBoatSize()
            
        test_conflicts = check_unit_conflicts(test_graph, test_graph, 0, test_graph.units)
        self.assertEqual(test_conflicts.__len__(), 0)
        
        # Testing graph with 5 units containing 4 conflicts
        test_graph = Graph.Graph()
        conflict_count = 0
        min_boat_size = 0
        
        while min_boat_size != 3:
            test_graph.generateGraph(5)
            min_boat_size = test_graph.getMinimumBoatSize()
            
        test_conflicts = check_unit_conflicts(test_graph, test_graph, 0, test_graph.units)
        self.assertEqual(test_conflicts.__len__(), 4)
        
        # Testing graph with no units
        test_graph = Graph.Graph()
        test_graph.generateGraph(0)
        test_conflicts = check_unit_conflicts(test_graph, test_graph, 0, test_graph.units)
        self.assertEqual(test_conflicts.__len__(), 0)

if __name__ == '__main__':
    unittest.main()