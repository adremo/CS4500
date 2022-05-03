# Author: Tiana Madison
# Date: 2 May 2022
# Class: CS 4500
# ========================================================================================================
# Description: This program handles the help menu.
# =========================================================================================================
# Central Data Structures used: None
# =========================================================================================================
# External Files: None
# =========================================================================================================
# External Sources used: Python 3.10.4 Documentation: https://docs.python.org/3/library/json.html
# Pygame Documenation: https://www.pygame.org/docs/ 
# =========================================================================================================
import pygame
import sys
import menu_button
from pygame.locals import *
from options import checkSounds, control_sound_volume


# Setting up window
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
offset = 0.0


def format_help(root, screen):
    # Setting up options menu appearance

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
    SUB_BACKGROUND_COLOR = black
    TEXT_COLOR = Color(255, 255, 255)
    HEADER_COLOR = teal
    HEADER_COLOR_HARD = teal
    SUBHEADER_COLOR_LEFT = teal
    SUBHEADER_COLOR_RIGHT = teal
    MESSAGE_BACKGROUND_COLOR = teal
    ENTRY_BACKGROUND_1 = Color(54, 154, 181)
    ENTRY_BACKGROUND_2 = light_teal

    # Font
    header_font = pygame.font.SysFont(None, 120)
    subheader_font = pygame.font.SysFont(None, 50)
    entry_font = pygame.font.SysFont(None, 40)

    # Surface building and positioning
    button_offset = 100
    y_offset = 50
    starting_offset = 165 + (y_offset * 2.5)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight() 
    button_base_x = (screen_width/3) + 200
    button_base_y = 475
    background_sub_rect = Rect(50, (screen_height/2) - 500, screen_width - 100, 1000)
    header_zone = Rect(100, 100, screen_width - 200, 150)
    #content_zone = Rect(100, starting_offset, screen_width - 200, 700)
    content_zone_left = Rect(100, starting_offset, (screen_width/2) - 140, 700)
    content_zone_right = Rect(960, starting_offset, (screen_width/2) - 100, 700)

    # Header text
    header_text = "Instructions:"
    subheader_text_left = "How to Play:"
    subheader_text_right = "Graphs and Vertex Covers:"

    # Setting up the main surfaces
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, SUB_BACKGROUND_COLOR, background_sub_rect)
    pygame.draw.rect(screen, HEADER_COLOR, header_zone)
    #pygame.draw.rect(screen, HEADER_COLOR, content_zone)
    pygame.draw.rect(screen, SUBHEADER_COLOR_LEFT, content_zone_left)
    pygame.draw.rect(screen, SUBHEADER_COLOR_RIGHT, content_zone_right)

    # Fill in the header information
    header_object = header_font.render(header_text, True, TEXT_COLOR, HEADER_COLOR)
    header_rect = header_object.get_rect()
    header_rect.center = ((screen_width/2), 175)
    screen.blit(header_object, header_rect)

def display_help_menu(root, screen):
    # Main loop that controls the options page
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
        
        format_help(root, screen)

        # Menu Noises
        click_sound = pygame.mixer.Sound(r'Sounds/click_sound.wav')
        volume = control_sound_volume(0.5)
        pygame.mixer.Sound.set_volume(click_sound, volume)
        
        # Back to main menu button
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        main_menu_button = menu_button.Back_Button(x=width * 0.07, y=height * 0.85)
        
        if main_menu_button.draw_back_button(screen):
            pygame.mixer.Sound.play(click_sound)
            running = False

        pygame.display.update()
    
    return

pygame.quit()