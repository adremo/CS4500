# Author: Tiana Madison
# Date: 13 April 2022
# Class: CS 4500
# ========================================================================================================
# Description: This program handles the leaderboard implementation.
# =========================================================================================================
# Central Data Structures used: Dictionaries
# =========================================================================================================
# External Files: json (There is no need to add anything, the program will create the necessary files)
# =========================================================================================================
# External Sources used: Python 3.10.4 Documentation: https://docs.python.org/3/library/json.html
# Pygame Documentation: https://www.pygame.org/docs/ 
# Geeks-for-Geeks Tutorial: https://www.geeksforgeeks.org/python-display-text-to-pygame-window/ 
# =========================================================================================================
import json
import pygame
import sys
import tkinter as tk
from pygame.locals import *
from scores import load_scores

# Setting up window
root = tk.Tk()
root.withdraw()
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
offset = 0.0

def format_leaderboard():
    # Setting up leaderboard appearance
    BACKGROUND_COLOR = Color(80, 80, 245)
    EASY_BACKGROUND_COLOR = Color(82, 216, 50)
    HARD_BACKGROUND_COLOR = Color(100, 70, 50)
    TEXT_COLOR = Color(255, 255, 255)

    # Font
    header_font = pygame.font.SysFont(None, 75)
    subheader_font = pygame.font.SysFont(None, 50)
    entry_font = pygame.font.SysFont(None, 40)

    # Surface building and positioning
    x_offset = 900
    y_offset = 50
    starting_offset = 165 + (y_offset * 2.5)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight() 
    entry_x_offset_easy = (screen_width/2) - 200
    entry_x_offset_hard = (screen_width/2) - 150
    easy_rect = Rect(50, (screen_height/2) - 500, (screen_width/2) - 100, 1000)
    hard_rect = Rect(950, (screen_height/2) - 500, (screen_width/2) - 50, 1000)
    header_zone_easy = Rect(100, 100, (screen_width/2) - 200, 100)
    header_zone_hard = Rect(1000, 100, (screen_width/2) - 150, 100)
    subheader_zone_easy = Rect(100, 210, (screen_width/2) - 200, 70)
    subheader_zone_hard = Rect(1000, 210, (screen_width/2) - 150, 70)

    # Header text
    header_text_easy = "Best Scores: Easy Difficulty"
    header_text_hard = "Best Scores: Hard Difficulty"
    subheader_text = "Rank                    Name                    Score"
    
    # Color List
    black = Color(0, 0, 0)
    blue = Color(0, 0, 200)
    light_blue = Color(30, 30, 230)
    lighter_blue = Color(80, 80, 245)
    brown = Color(100, 70, 50)
    green = Color(82, 216, 50)

    # Other variables
    MAX_ENTRIES = 15
    
    # Setting up the easy and hard surfaces
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, EASY_BACKGROUND_COLOR, easy_rect)
    pygame.draw.rect(screen, HARD_BACKGROUND_COLOR, hard_rect)
    pygame.draw.rect(screen, blue, header_zone_easy)
    pygame.draw.rect(screen, blue, header_zone_hard)
    pygame.draw.rect(screen, black, subheader_zone_easy)
    pygame.draw.rect(screen, black, subheader_zone_hard)

    # Fill in the header information
    header_object_easy = header_font.render(header_text_easy, True, TEXT_COLOR, blue)
    header_rect_easy = header_object_easy.get_rect()
    header_rect_easy.center = ((screen_width/4), 150)
    screen.blit(header_object_easy, header_rect_easy)

    header_object_hard = header_font.render(header_text_hard, True, TEXT_COLOR, blue)
    header_rect_hard = header_object_hard.get_rect()
    header_rect_hard.center = ((screen_width/4) + x_offset, 150)
    screen.blit(header_object_hard, header_rect_hard)

    # Fill in the subheader information
    subheader_object_easy = subheader_font.render(subheader_text, True, TEXT_COLOR, light_blue)
    subheader_rect_easy = subheader_object_easy.get_rect()
    subheader_rect_easy.center = ((screen_width/4), 245)
    screen.blit(subheader_object_easy, subheader_rect_easy)

    subheader_object_hard = subheader_font.render(subheader_text, True, TEXT_COLOR, light_blue)
    subheader_rect_hard = subheader_object_hard.get_rect()
    subheader_rect_hard.center = ((screen_width/4) + x_offset, 245)
    screen.blit(subheader_object_hard, subheader_rect_hard)

    # Load scores into local memory
    scores_easy = load_scores(difficulty="easy")
    scores_hard = load_scores(difficulty="hard")

    # Render leader data onto the screen
    if scores_easy == None:
        # Display that there are no saved high scores
        pass

    else:
        # Format and display the high scores
        for x in range (0, MAX_ENTRIES): # Alternating the zone colors
            if x % 2 == 0:
                zone_color_easy = black
            else:
                zone_color_easy = brown
            
            # Draw the entry zones
            entry_zone_easy = Rect(100, starting_offset + (x * y_offset), entry_x_offset_easy, 45)
            pygame.draw.rect(screen, zone_color_easy, entry_zone_easy)

            # Render rank data
            rank_text_easy = "#" + str(x + 1)
            rank_object_easy = entry_font.render(rank_text_easy, True, TEXT_COLOR, zone_color_easy)
            rank_rect_easy = rank_object_easy.get_rect()
            rank_rect_easy.center = ((screen_width/4) - 300, 310 + (x * y_offset))
            screen.blit(rank_object_easy, rank_rect_easy)

            # Determine name field data
            try:
                name_data_easy = scores_easy["scores"][x][0]["name"]
            
            except IndexError:
                # To handle out of range errors when there are not enough data entries to display
                name_data_easy = ""

            # Render name data
            name_object_easy = entry_font.render(name_data_easy, True, TEXT_COLOR, blue)
            name_rect_easy = name_object_easy.get_rect()
            name_rect_easy.center = ((screen_width/4), 310 + (x * y_offset))
            screen.blit(name_object_easy, name_rect_easy)

            # Determine score field data
            try:
                raw_score_data_easy = scores_easy["scores"][x][0]["score"]
                score_data_easy = str(raw_score_data_easy)
            
            except IndexError:
                # To handle out of range errors when there are not enough data entries to display
                score_data_easy = ""

            # Render score data
            score_object_easy = entry_font.render(score_data_easy, True, TEXT_COLOR, blue)
            score_rect_easy = score_object_easy.get_rect()
            score_rect_easy.center = ((screen_width/4) + 300, 310 + (x * y_offset))
            screen.blit(score_object_easy, score_rect_easy)

    if scores_hard == None:
        # Display that there are no saved high scores
        pass

    else:
        # Format and display the high scores
        for x in range (0, MAX_ENTRIES): # Alternating the zone colors
            if x % 2 == 0:
                zone_color_hard = black
            else:
                zone_color_hard = light_blue
        
            # Draw the entry zones
            entry_zone_hard = Rect(100 + x_offset, starting_offset + (x * y_offset), entry_x_offset_hard, 45)
            pygame.draw.rect(screen, zone_color_hard, entry_zone_hard)

            # Render rank data
            rank_text_hard = "#" + str(x + 1)
            rank_object_hard = entry_font.render(rank_text_hard, True, TEXT_COLOR, zone_color_hard)
            rank_rect_hard = rank_object_hard.get_rect()
            rank_rect_hard.center = ((screen_width/4) - 300 + x_offset, 310 + (x * y_offset))
            screen.blit(rank_object_hard, rank_rect_hard)

            # Determine name field data
            try:
                name_data_hard = scores_hard["scores"][x][0]["name"]
            
            except IndexError:
                # To handle out of range errors when there are not enough data entries to display
                name_data_hard = ""

            # Render name data
            name_object_hard = entry_font.render(name_data_hard, True, TEXT_COLOR, green)
            name_rect_hard = name_object_hard.get_rect()
            name_rect_hard.center = ((screen_width/4) + x_offset, 310 + (x * y_offset))
            screen.blit(name_object_hard, name_rect_hard)

            # Determine score field data
            try:
                raw_score_data_hard = scores_hard["scores"][x][0]["score"]
                score_data_hard = str(raw_score_data_hard)
            
            except IndexError:
                # To handle out of range errors when there are not enough data entries to display
                score_data_hard = ""

            # Render score data
            score_object_hard = entry_font.render(score_data_hard, True, TEXT_COLOR, green)
            score_rect_hard = score_object_hard.get_rect()
            score_rect_hard.center = ((screen_width/4) + 300 + x_offset, 310 + (x * y_offset))
            screen.blit(score_object_hard, score_rect_hard)


def display_leaderboard():
    # Main loop that controls the leaderboard page
    running = True
    FPS = 60 # Locks the FPS on the screen to this value
    clock = pygame.time.Clock()
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        format_leaderboard()
        pygame.display.update()
    
    return

display_leaderboard()
pygame.quit()

    