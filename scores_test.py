# Author: Tiana Madison
# Description: This program contains the unit tests for scores.py
# External Sources: Python 3.10.4 Documentation: https://docs.python.org/3/library/unittest.html 
# =========================================================================================================
import json
import os
import unittest
from scores import *

NAME_1 = "Foo"
NAME_2 = "Bar"
SCORE = 500
WORSE_SCORE = 600
SAME_SCORE = 500
BETTER_SCORE = 400
EASY_DIFFICULTY = "easy"
HARD_DIFFICULTY = "hard"

# What needs to be tested?
# load_scores function - not getting unit tests because it only uses json built in functions that are well-tested
# print_scores function - not tested because it will not be used in the game's code, it is only a developer tool to view data
# saves scores function - multiple scenarios will be tested to determine if scores are properly being saved.
# The following conditions must be met:
#   - if any empty .json file containing no data is present, data is saved to it
#   - if a .json file containing at least 1 entry of data is present, the following scenarios must be tested
#       > a 2nd entry with no overlapping name is saved
#       > a 3rd entry with an overlapping name is saved with a worse score (nothing should happen)
#       > a 3rd entry with an overlapping name is saved with the same score (nothing should happen)
#       > a 3rd entry with an overlapping name is saved with a better score (the score should be overwritten)

# If no .json file is present, one is created and data is saved to it
# To run this test, all .json files present must be deleted from the working directory beforehand.

class TestSaveScore(unittest.TestCase):
    """Multiple scenarios will be tested to determine if scores are properly being saved"""

    def setUp(self):
        """Delete any existing .json files from the working directory"""
        try: 
            os.remove("./easy.json")
        
        except FileNotFoundError:
            pass

        try:
            os.remove("./hard.json")
        
        except FileNotFoundError:
            pass

        try:
            os.remove("./easy_test.json")
        
        except FileNotFoundError:
            pass

        try:
            os.remove("./hard_test.json")
        
        except FileNotFoundError:
            pass
    
    # Tests for "easy" difficulty
    def testFileCreationEasy(self):
        """If no .json file is present, one is created and data is saved to it"""
        save_score(difficulty=EASY_DIFFICULTY, new_name=NAME_1, new_score=SCORE)
        test_data = load_scores(difficulty=EASY_DIFFICULTY)
        actual_name = test_data["scores"][0][0]["name"]
        actual_score = test_data["scores"][0][0]["score"]
        self.assertEqual(NAME_1, actual_name)
        self.assertEqual(SCORE, actual_score)
    
    def testEmptyFileEasy(self):
        """If an empty .json file containing no data is present, data is saved to it"""
        f = open("./easy_test.json", "w")
        save_score(difficulty=EASY_DIFFICULTY, new_name=NAME_1, new_score=SCORE)
        test_data = load_scores(difficulty=EASY_DIFFICULTY)
        actual_name = test_data["scores"][0][0]["name"]
        actual_score = test_data["scores"][0][0]["score"]
        self.assertEqual(NAME_1, actual_name)
        self.assertEqual(SCORE, actual_score)
        f.close()
    
    # Tests for "hard" difficulty
    def testFileCreationHard(self):
        """If no .json file is present, one is created and data is saved to it"""
        save_score(difficulty=HARD_DIFFICULTY, new_name=NAME_1, new_score=SCORE)
        test_data = load_scores(difficulty=HARD_DIFFICULTY)
        actual_name = test_data["scores"][0][0]["name"]
        actual_score = test_data["scores"][0][0]["score"]
        self.assertEqual(NAME_1, actual_name)
        self.assertEqual(SCORE, actual_score)
    
    def testEmptyFileHard(self):
        """If an empty .json file containing no data is present, data is saved to it"""
        f = open("./hard_test.json", "w")
        save_score(difficulty=HARD_DIFFICULTY, new_name=NAME_1, new_score=SCORE)
        test_data = load_scores(difficulty=HARD_DIFFICULTY)
        actual_name = test_data["scores"][0][0]["name"]
        actual_score = test_data["scores"][0][0]["score"]
        self.assertEqual(NAME_1, actual_name)
        self.assertEqual(SCORE, actual_score)
        f.close()

if __name__ == "__main__":
    unittest.main()
