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
#   - if a .json file containing at least 1 entry of data is present, the following scenarios must be tested
#       > a 2nd entry with no overlapping name is saved
#       > a 3rd entry with an overlapping name is saved with a worse score (nothing should happen)
#       > a 3rd entry with an overlapping name is saved with the same score (nothing should happen)
#       > a 3rd entry with an overlapping name is saved with a better score (the score should be overwritten)

# If no .json file is present, one is created and data is saved to it
# To run this test, all .json files present must be deleted from the working directory beforehand.

def delete_files():
    # Custom setup/teardown function for the test cases, as the built-in methods were deleting the files too early
    try: 
        os.remove("./easy.json")
    
    except FileNotFoundError:
        pass

    try:
        os.remove("./hard.json")
    
    except FileNotFoundError:
        pass

class TestSaveScore(unittest.TestCase):
    """Multiple scenarios will be tested to determine if scores are properly being saved"""

    # Tests for "easy" difficulty
    def testFileCreationEasy(self):
        """If no .json file is present, one is created and data is saved to it"""
        save_score(difficulty=EASY_DIFFICULTY, new_name=NAME_1, new_score=SCORE)
        test_data = load_scores(difficulty=EASY_DIFFICULTY)
        actual_name = test_data["scores"][0][0]["name"]
        actual_score = test_data["scores"][0][0]["score"]
        self.assertEqual(NAME_1, actual_name)
        self.assertEqual(SCORE, actual_score)
    
    def testSecondEntryEasy(self):
        """If a .json file containing at least 1 entry of data is present and a second entry with no overlapping name is saved"""
        save_score(difficulty=EASY_DIFFICULTY, new_name=NAME_2, new_score=SCORE)
        test_data = load_scores(difficulty=EASY_DIFFICULTY)
        actual_name = test_data["scores"][-1][0]["name"]
        actual_score = test_data["scores"][-1][0]["score"]
        self.assertEqual(NAME_2, actual_name)
        self.assertEqual(SCORE, actual_score)
    
    def duplicateNameSameScoreEasy(self):
        """
        If a .json file containing at least 1 entry of data is present and a third entry with an overlapping name 
        is saved with the same score (nothing should happen and no new data should be saved)
        """
        test_data = load_scores(difficulty=EASY_DIFFICULTY)
        expected_number_of_saves = len(test_data["scores"])
        
        save_score(difficulty=EASY_DIFFICULTY, new_name=NAME_1, new_score=SAME_SCORE)
        test_data = load_scores(difficulty=EASY_DIFFICULTY)
        actual_name = test_data["scores"][-1][0]["name"]
        actual_score = test_data["scores"][-1][0]["score"]
        actual_number_of_saves = len(test_data["scores"])
        
        self.assertEqual(NAME_1, actual_name)
        self.assertEqual(SCORE, actual_score)
        self.assertEqual(expected_number_of_saves, actual_number_of_saves)
    
    # Tests for "hard" difficulty
    def testFileCreationHard(self):
        """If no .json file is present, one is created and data is saved to it"""
        save_score(difficulty=HARD_DIFFICULTY, new_name=NAME_1, new_score=SCORE)
        test_data = load_scores(difficulty=HARD_DIFFICULTY)
        actual_name = test_data["scores"][0][0]["name"]
        actual_score = test_data["scores"][0][0]["score"]
        self.assertEqual(NAME_1, actual_name)
        self.assertEqual(SCORE, actual_score)
    
    def testSecondEntryHard(self):
        """If a .json file containing at least 1 entry of data is present and a second entry with no overlapping name is saved"""
        save_score(difficulty=HARD_DIFFICULTY, new_name=NAME_2, new_score=SCORE)
        test_data = load_scores(difficulty=HARD_DIFFICULTY)
        actual_name = test_data["scores"][-1][0]["name"]
        actual_score = test_data["scores"][-1][0]["score"]
        self.assertEqual(NAME_2, actual_name)
        self.assertEqual(SCORE, actual_score)
    
    def duplicateNameSameScoreHard(self):
        """
        If a .json file containing at least 1 entry of data is present and a third entry with an overlapping name 
        is saved with the same score (nothing should happen and no new data should be saved)
        """
        test_data = load_scores(difficulty=HARD_DIFFICULTY)
        expected_number_of_saves = len(test_data["scores"])
        
        save_score(difficulty=HARD_DIFFICULTY, new_name=NAME_1, new_score=SAME_SCORE)
        test_data = load_scores(difficulty=HARD_DIFFICULTY)
        actual_name = test_data["scores"][1][0]["name"]
        actual_score = test_data["scores"][-1][0]["score"]
        actual_number_of_saves = len(test_data["scores"])
        
        self.assertEqual(NAME_1, actual_name)
        self.assertEqual(SCORE, actual_score)
        self.assertEqual(expected_number_of_saves, actual_number_of_saves)

if __name__ == "__main__":
    unittest.main()
