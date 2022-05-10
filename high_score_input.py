# Andrew Morris
# 5/2/2022
# CS 4500 Spring 2022
# Expected to follow a game win, takes in the final turn count from the game and displays it.
# Gets the user's name from keyboard input and returns it, default name is "???" in case of no name entered.
# External Files: None
# Central Data Structures: None

import sys
import pygame
import options
import menu_button
from pygame.locals import *

#set up screen
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
offset = 0.0

# Screen coordinates
screen_width = screen.get_width()
screen_height = screen.get_height()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
background_color = (34, 26, 92)
header_color = (41, 106, 131)

# Fonts
font = pygame.font.Font('freesansbold.ttf', 36)
small_font = pygame.font.Font('freesansbold.ttf', 24)

# Sounds  
click_sound = pygame.mixer.Sound(r'Sounds/click_sound.wav')

# Textbox Rect
text_box = pygame.Rect(screen_width * .3, screen_height * .4, screen_width * .4, screen_height * .1)

# Takes in turn count from completed game, records user input for username, returns username.
# User can exit with Escape, Enter, or by clicking the Main Menu (back arrow) button.
def get_username(turn_count):
    volume_6 = options.control_sound_volume(0.6)
    
    # Default username for leaderboard in case user does not want to enter their name
    username = "???"
    text_entered = False

    run = True
    while(run):
        # Set up screen
        screen.fill(background_color)
        content_zone = Rect(screen_width/11, screen_height * .18, screen_width - (screen_width/5.5), screen_height * .6)
        pygame.draw.rect(screen, header_color, content_zone)

        # Display UI text
        victory_text = "You won in " + str(turn_count) + " turns!"
        victory_display = font.render(victory_text, True, white)
        victory_rect = victory_display.get_rect()
        victory_rect.center = (screen_width * .5, screen_height * 0.3)
        screen.blit(victory_display, victory_rect)

        victory_subtext = "Please type your name for the leaderboard and press Enter to submit it:"
        victory_subdisplay = small_font.render(victory_subtext, True, white)
        victory_subrect = victory_subdisplay.get_rect()
        victory_subrect.center = (screen_width * .5, screen_height * 0.36)
        screen.blit(victory_subdisplay, victory_subrect)

        # Event Loop, record user's unicode inputs, using backspace to delete characters and ignoring tabs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                elif event.key == pygame.K_RETURN:
                    run = False
                elif event.key == pygame.K_TAB:
                    continue
                elif event.key == pygame.K_BACKSPACE:
                    username = username[0:-1]
                else:
                    if text_entered == False:
                        username = ""
                        text_entered = True
                    if len(username) <= 20:
                        username += event.unicode

        main_menu_button = menu_button.Back_Button(x=screen_width * 0.07, y=screen_height * 0.9)

        if main_menu_button.draw_back_button(screen):
            run = False

        # Display username text to screen
        pygame.draw.rect(screen, black, text_box)
        
        if (text_entered):
            text_surface = font.render(username, True, (255, 255, 255))
            screen.blit(text_surface, ((screen_width * .4), (screen_height * .44)))

        pygame.display.flip()
    
    pygame.mixer.Sound.play(click_sound)
    return username