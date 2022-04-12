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
# w3schools Json Information: https://www.w3schools.com/python/python_json.asp 
# =========================================================================================================
import json

def load_scores():
    # Loading the "easy mode" scores
    try:
        with open("./data/easy.json", "r", encoding="utf-8") as f:
            scores_easy = json.load(f)
            print(scores_easy)
        
    except FileNotFoundError: # Create temporary data storage if no local saved data is found
        scores_easy = []
    
    print("=================Divider Line=======================================")

    # Loading the "hard mode" scores
    try:
        with open("./data/hard.json", "r", encoding="utf-8") as f:
            scores_hard = json.load(f)
            print(scores_hard)
        
    except FileNotFoundError: # Create temporary data storage if no local saved data is found
        scores_hard = []

def save_score(difficulty, new_name, new_score): # Updates the list of high-scores
    if difficulty == "easy":
        try:
            with open("./data/easy.json", "r+", encoding="utf-8") as f:
                scores_easy = json.load(f)

                new_data = {
                        "name": new_name,
                        "score": new_score
                    },

                scores_easy["scores"].append(new_data) # Add the new data to the existing data
                f.seek(0)
                json.dump(scores_easy, f, indent=4) # Convert the saved data to json
            
        except FileNotFoundError: # Create temporary data storage if no local saved data is found
            scores_easy = {
                "scores": [
                    {
                        "name": new_name,
                        "score": new_score
                    },
                ]
            }

            f = open("./data/easy.json", "w") # Create the new local storage file
            json.dump(scores_easy, f, indent=4) # Save the data to the new json file

test_name = "Mirin"
test_score = 77

print("Program start:\n")
load_scores()
save_score(difficulty="easy", new_name=test_name, new_score=test_score)
print("Scores successfully saved.\n")
load_scores()