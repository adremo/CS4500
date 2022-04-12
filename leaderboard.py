# Author: Tiana Madison
# Date: 12 April 2022
# Class: CS 4500
# ========================================================================================================
# Description: This program handles the saving and loading of scoring data using json.
# =========================================================================================================
# Central Data Structures used: Dicts
# =========================================================================================================
# External Files: json
# =========================================================================================================
# External Sources used: Python 3.10.4 Documentation: https://docs.python.org/3/library/json.html 
# =========================================================================================================
import json

test_score = 500

def load_scores():
    try:
        with open("./data/scores.json", "r", encoding="utf-8") as f:
            scores = json.load(f)
            print(scores)
        
    except FileNotFoundError: # Create temporary data storage if no local saved data is found
        scores = []

def save_scores():
    pass

load_scores()