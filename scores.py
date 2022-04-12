# Author: Tiana Madison
# Date: 12 April 2022
# Class: CS 4500
# ========================================================================================================
# Description: This program handles the saving and loading of scoring data using json.
# =========================================================================================================
# Central Data Structures used: Dictionaries
# =========================================================================================================
# External Files: json (There is no need to add anything, the program will create the necessary files)
# =========================================================================================================
# External Sources used: Python 3.10.4 Documentation: https://docs.python.org/3/library/json.html
# w3schools Json Information: https://www.w3schools.com/python/python_json.asp 
# =========================================================================================================
# Implementation: To use these functions, add this line to your import statements:
# from scores import *
#==========================================================================================================
import json

def load_scores(difficulty): # Return the raw scoring data as a dict, requires difficulty as a parameter
    if difficulty == "easy": # Loading the "easy mode" scores
        try:
            with open("./data/easy.json", "r", encoding="utf-8") as f:
                scores_easy = json.load(f)
            
        except FileNotFoundError: # Create temporary data storage if no local saved data is found
            scores_easy = []
    
        return scores_easy

    elif difficulty == "hard": # Loading the "hard mode" scores
        try:
            with open("./data/hard.json", "r", encoding="utf-8") as f:
                scores_hard = json.load(f)
            
        except FileNotFoundError: # Create temporary data storage if no local saved data is found
            scores_hard = []
        
        return scores_hard
    
    else:
        print("Error in loading scores. Was 'difficulty' correctly specified?")
        return None


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
    
    elif difficulty == "hard":
        try:
            with open("./data/hard.json", "r+", encoding="utf-8") as f:
                scores_hard = json.load(f)

                new_data = {
                        "name": new_name,
                        "score": new_score
                    },

                scores_hard["scores"].append(new_data) # Add the new data to the existing data
                f.seek(0)
                json.dump(scores_hard, f, indent=4) # Convert the saved data to json
            
        except FileNotFoundError: # Create temporary data storage if no local saved data is found
            scores_hard = {
                "scores": [
                    {
                        "name": new_name,
                        "score": new_score
                    },
                ]
            }

            f = open("./data/hard.json", "w") # Create the new local storage file
            json.dump(scores_hard, f, indent=4) # Save the data to the new json file
    
    else:
        print("Error in saving scores. Was 'difficulty' correctly specified?")

def print_scores(): # Pretty print all sets of scores in dictionary format (for developer use)
    print("===========================================================================")
    print("Loading Easy mode scores...\n")
    try:
        with open("./data/easy.json", "r", encoding="utf-8") as f:
            scores_easy = json.load(f)
            scores_formatted = json.dumps(scores_easy, indent=4) # Pretty formatting
            print(scores_formatted) # Print the "easy" mode scores if available
        
    except FileNotFoundError:
        scores_easy = []
        print("No saved easy mode scores.")

    print("\nLoading Hard mode scores...\n")
    try:
        with open("./data/hard.json", "r", encoding="utf-8") as f:
            scores_hard = json.load(f)
            scores_formatted = json.dumps(scores_hard, indent=4) # Pretty formatting
            print(scores_formatted) # Print the "hard" mode scores if available
        
    except FileNotFoundError:
        scores_hard = []
        print("No saved hard mode scores.")
    
    print("===========================================================================")