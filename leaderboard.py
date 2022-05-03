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
# Geeks-for-Geeks Tutorials: https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
# https://www.geeksforgeeks.org/python-add-new-keys-to-a-dictionary/ 
# Dictionary Sorting with Lambda: https://www.youtube.com/watch?v=6uih8-Cc7Cg&ab_channel=JieJenn
# RGB Calculator: https://www.w3schools.com/colors/colors_rgb.asp   
# =========================================================================================================
import pygame
import sys
import menu_button
from pygame.locals import *
from scores import scores_setup, load_scores
from options import control_sound_volume

# Setting up window
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
offset = 0.0

def format_leaderboard(root, screen):
    # Setting up leaderboard appearance

    # Color List
    black = Color(0, 0, 0)
    blue = Color(58, 121, 227)
    light_blue = Color(30, 30, 230)
    lighter_blue = Color(80, 80, 245)
    brown = Color(100, 70, 50)
    green = Color(82, 216, 50)
    purple = Color(112, 65, 192)
    light_purple = Color(186, 156, 199)
    pink = Color(203, 165, 188)
    magenta = Color(172, 89, 188)
    teal = Color(41, 106, 131)
    light_teal = Color(98, 184, 208)

    BACKGROUND_COLOR = Color(34, 26, 92)
    EASY_BACKGROUND_COLOR = black
    HARD_BACKGROUND_COLOR = black
    TEXT_COLOR = Color(255, 255, 255)
    HEADER_COLOR_EASY = teal
    HEADER_COLOR_HARD = teal
    SUBHEADER_COLOR_EASY = teal
    SUBHEADER_COLOR_HARD = teal
    MESSAGE_BACKGROUND_COLOR = teal
    ENTRY_BACKGROUND_1 = Color(54, 154, 181)
    ENTRY_BACKGROUND_2 = light_teal

    # Font
    header_font = pygame.font.SysFont(None, 75)
    subheader_font = pygame.font.SysFont(None, 50)
    entry_font = pygame.font.SysFont(None, 40)

    # Surface building and positioning
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_offset = (screen_width * .45)
    y_offset = (screen_height * .047)
    starting_offset = (screen_height * .1125) + (y_offset * 2.5) 
    entry_x_offset_easy = (screen_width/2) - (screen_width * .1)
    entry_x_offset_hard = (screen_width/2) - (screen_width * .0725)
    easy_rect = Rect((screen_width * .025), (screen_height/2) - (screen_height * .47), (screen_width/2) - (screen_width * .05), (screen_height * .935))
    hard_rect = Rect((screen_width * .5) - (screen_width * .005), (screen_height/2) - (screen_height * .47), (screen_width/2) - (screen_width * .025), (screen_height * .935))
    header_zone_easy = Rect((screen_width * .05), (screen_height * .075), (screen_width/2) - (screen_width * .1), (screen_height * .075))
    header_zone_hard = Rect((screen_width * .52), (screen_height * .075), (screen_width/2) - (screen_width * .075), (screen_height * .075))
    subheader_zone_easy = Rect((screen_width * .05), (screen_height * .165), (screen_width/2) - (screen_width * .1), (screen_height * .0525))
    subheader_zone_hard = Rect((screen_width * .52), (screen_height * .165), (screen_width/2) - (screen_width * .075), (screen_height * .0525))

    # Header text
    header_text_easy = "Best Scores: Easy Difficulty"
    header_text_hard = "Best Scores: Hard Difficulty"
    subheader_text = "Rank                    Name                    Score"

    # Other variables
    MAX_ENTRIES = 15
    
    # Setting up the easy and hard surfaces
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, EASY_BACKGROUND_COLOR, easy_rect)
    pygame.draw.rect(screen, HARD_BACKGROUND_COLOR, hard_rect)
    pygame.draw.rect(screen, HEADER_COLOR_EASY, header_zone_easy)
    pygame.draw.rect(screen, HEADER_COLOR_HARD, header_zone_hard)
    pygame.draw.rect(screen, SUBHEADER_COLOR_EASY, subheader_zone_easy)
    pygame.draw.rect(screen, SUBHEADER_COLOR_HARD, subheader_zone_hard)

    # Fill in the header information
    header_object_easy = header_font.render(header_text_easy, True, TEXT_COLOR, HEADER_COLOR_EASY)
    header_rect_easy = header_object_easy.get_rect()
    header_rect_easy.center = ((screen_width/4), (screen_height * .12))
    screen.blit(header_object_easy, header_rect_easy)

    header_object_hard = header_font.render(header_text_hard, True, TEXT_COLOR, HEADER_COLOR_HARD)
    header_rect_hard = header_object_hard.get_rect()
    header_rect_hard.center = ((screen_width/4) + (screen_width * .475), (screen_height * .12))
    screen.blit(header_object_hard, header_rect_hard)

    # Fill in the subheader information
    subheader_object_easy = subheader_font.render(subheader_text, True, TEXT_COLOR, SUBHEADER_COLOR_EASY)
    subheader_rect_easy = subheader_object_easy.get_rect()
    subheader_rect_easy.center = ((screen_width/4), (screen_height * .19))
    screen.blit(subheader_object_easy, subheader_rect_easy)

    subheader_object_hard = subheader_font.render(subheader_text, True, TEXT_COLOR, SUBHEADER_COLOR_HARD)
    subheader_rect_hard = subheader_object_hard.get_rect()
    subheader_rect_hard.center = ((screen_width/4) + (screen_width * .475), (screen_height * .19))
    screen.blit(subheader_object_hard, subheader_rect_hard)

    # Load scores into local memory
    scores_easy = load_scores(difficulty="easy")
    scores_hard = load_scores(difficulty="hard")

    # Render leaderboard data onto the screen
    if len(scores_easy) == 0:
        # Display that there are no saved high scores
        message_text_easy = "No data"
        
        # Draw surface
        easy_message_zone = Rect((screen_width * .05), starting_offset, entry_x_offset_easy, (screen_height * .7))
        pygame.draw.rect(screen, MESSAGE_BACKGROUND_COLOR, easy_message_zone)

        # Display message
        message_object_easy = subheader_font.render(message_text_easy, True, TEXT_COLOR, MESSAGE_BACKGROUND_COLOR)
        message_rect_easy = message_object_easy.get_rect()
        message_rect_easy.center = ((screen_width/4), (screen_height * .55))
        screen.blit(message_object_easy, message_rect_easy)

    else:
        # Create new unsorted dictionaries from the data
        scores_easy_unsorted = scores_setup()

        for x in range(0, len(scores_easy["scores"])):
            scores_easy_unsorted.add(scores_easy["scores"][x][0]["name"], scores_easy["scores"][x][0]["score"])
        
        # Sort the new dictionaries
        scores_easy_sorted = {k: v for k, v in sorted(scores_easy_unsorted.items(), key=lambda v: v[1])}

        name_data_easy_list = []
        score_data_easy_list = []

        for k, v in scores_easy_sorted.items():
            name_data_easy_list.append(k)
            score_data_easy_list.append(v)

        # Format and display the high scores
        for x in range (0, MAX_ENTRIES): # Alternating the zone colors
            if x % 2 == 0:
                zone_color_easy = ENTRY_BACKGROUND_1
            else:
                zone_color_easy = ENTRY_BACKGROUND_2
            
            # Draw the entry zones
            entry_zone_easy = Rect((screen_width * .05), starting_offset + (x * y_offset), entry_x_offset_easy, (screen_height * .0425))
            pygame.draw.rect(screen, zone_color_easy, entry_zone_easy)

            # Render rank data
            rank_text_easy = "#" + str(x + 1)
            rank_object_easy = entry_font.render(rank_text_easy, True, TEXT_COLOR, zone_color_easy)
            rank_rect_easy = rank_object_easy.get_rect()
            rank_rect_easy.center = ((screen_width/4) - (screen_width * .15), (screen_height * .25) + (x * y_offset))
            screen.blit(rank_object_easy, rank_rect_easy)

            # Determine name field data
            try:
                name_data_easy = name_data_easy_list[x]
            
            except IndexError:
                # To handle out of range errors when there are not enough data entries to display
                name_data_easy = ""

            # Render name data
            name_object_easy = entry_font.render(name_data_easy, True, TEXT_COLOR, zone_color_easy)
            name_rect_easy = name_object_easy.get_rect()
            name_rect_easy.center = ((screen_width/4), (screen_height * .25) + (x * y_offset))
            screen.blit(name_object_easy, name_rect_easy)

            # Determine score field data
            try:
                raw_score_data_easy = score_data_easy_list[x]
                score_data_easy = str(raw_score_data_easy)
            
            except IndexError:
                # To handle out of range errors when there are not enough data entries to display
                score_data_easy = ""

            # Render score data
            score_object_easy = entry_font.render(score_data_easy, True, TEXT_COLOR, zone_color_easy)
            score_rect_easy = score_object_easy.get_rect()
            score_rect_easy.center = ((screen_width/4) + (screen_width * .15), (screen_height * .25) + (x * y_offset))
            screen.blit(score_object_easy, score_rect_easy)

    if len(scores_hard) == 0:
        # Display that there are no saved high scores
        message_text_hard = "No data"
        
        # Draw surface
        hard_message_zone = Rect((screen_width * .0715) + x_offset, starting_offset, entry_x_offset_hard, (screen_height * .7))
        pygame.draw.rect(screen, MESSAGE_BACKGROUND_COLOR, hard_message_zone)

        # Display message
        message_object_hard = subheader_font.render(message_text_hard, True, TEXT_COLOR, MESSAGE_BACKGROUND_COLOR)
        message_rect_hard = message_object_hard.get_rect()
        message_rect_hard.center = ((screen_width * .725), (screen_height * .55))
        screen.blit(message_object_hard, message_rect_hard)

    else:
        # Create new unsorted dictionaries from the data
        scores_hard_unsorted = scores_setup()

        for x in range(0, len(scores_hard["scores"])):
            scores_hard_unsorted.add(scores_hard["scores"][x][0]["name"], scores_hard["scores"][x][0]["score"])
        
        # Sort the new dictionaries
        scores_hard_sorted = {k: v for k, v in sorted(scores_hard_unsorted.items(), key=lambda v: v[1])}

        name_data_hard_list = []
        score_data_hard_list = []

        for k, v in scores_hard_sorted.items():
            name_data_hard_list.append(k)
            score_data_hard_list.append(v)

        # Format and display the high scores
        for x in range (0, MAX_ENTRIES): # Alternating the zone colors
            if x % 2 == 0:
                zone_color_hard = ENTRY_BACKGROUND_1
            else:
                zone_color_hard = ENTRY_BACKGROUND_2
        
            # Draw the entry zones
            entry_zone_hard = Rect((screen_width * .07) + x_offset, starting_offset + (x * y_offset), entry_x_offset_hard, (screen_height * .0425))
            pygame.draw.rect(screen, zone_color_hard, entry_zone_hard)

            # Render rank data
            rank_text_hard = "#" + str(x + 1)
            rank_object_hard = entry_font.render(rank_text_hard, True, TEXT_COLOR, zone_color_hard)
            rank_rect_hard = rank_object_hard.get_rect()
            rank_rect_hard.center = ((screen_width/4) - (screen_width * .125) + x_offset, (screen_height * .25) + (x * y_offset))
            screen.blit(rank_object_hard, rank_rect_hard)

            # Determine name field data
            try:
                name_data_hard = name_data_hard_list[x]
            
            except IndexError:
                # To handle out of range errors when there are not enough data entries to display
                name_data_hard = ""

            # Render name data
            name_object_hard = entry_font.render(name_data_hard, True, TEXT_COLOR, zone_color_hard)
            name_rect_hard = name_object_hard.get_rect()
            name_rect_hard.center = ((screen_width/4) + (screen_width * .475), (screen_height * .25) + (x * y_offset))
            screen.blit(name_object_hard, name_rect_hard)

            # Determine score field data
            try:
                raw_score_data_hard = score_data_hard_list[x]
                score_data_hard = str(raw_score_data_hard)
            
            except IndexError:
                # To handle out of range errors when there are not enough data entries to display
                score_data_hard = ""

            # Render score data
            score_object_hard = entry_font.render(score_data_hard, True, TEXT_COLOR, zone_color_hard)
            score_rect_hard = score_object_hard.get_rect()
            score_rect_hard.center = ((screen_width/4) + (screen_width * .175) + x_offset, (screen_height * .25) + (x * y_offset))
            screen.blit(score_object_hard, score_rect_hard)


def display_leaderboard(root, screen):
    # Main loop that controls the leaderboard page
    # Takes the root and screen from the main file as parameters
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
        
        format_leaderboard(root, screen)

        # Menu Noises
        click_sound = pygame.mixer.Sound(r'Sounds/click_sound.wav')
        volume = control_sound_volume(0.5)
        pygame.mixer.Sound.set_volume(click_sound, volume)
        
        # Back to main menu button
        #menu_boat_image = pygame.image.load(r'Images/Menu_Boat.png').convert_alpha()
        #back_button_image = pygame.image.load(r'Images/back_arrow.png').convert_alpha()
        #main_menu_button = menu_button.Custom_Button(200, 800, back_button_image, optional_hover_image=menu_boat_image)
        main_menu_button = menu_button.Back_Button()

        if main_menu_button.draw_back_button(screen):
            pygame.mixer.Sound.play(click_sound)
            running = False

        pygame.display.update()
    
    return

pygame.quit()

    