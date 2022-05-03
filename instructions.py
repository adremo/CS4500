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
    MESSAGE_BACKGROUND_COLOR = black
    ENTRY_BACKGROUND_1 = Color(54, 154, 181)
    ENTRY_BACKGROUND_2 = light_teal

    # Font
    header_font = pygame.font.SysFont(None, 120)
    subheader_font = pygame.font.SysFont(None, 50)
    content_font = pygame.font.SysFont(None, 40)

    # Surface building and positioning
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_offset = (screen_width * .45)
    y_offset = (screen_height * .047)
    starting_offset = (screen_height * .1125) + (y_offset * 2.5) 
    background_sub_rect = Rect(screen_width/25, screen_height/20, screen_width - (screen_width/12), screen_height - (screen_height/10))
    header_zone = Rect(screen_width/16, screen_height/11, (screen_width * .875), screen_height - (screen_height/1.15))
    content_zone_left = Rect(screen_width/16, starting_offset, (screen_width * .425), (screen_height * .7))
    content_zone_right = Rect((screen_width * .5), starting_offset, (screen_width * .4375), (screen_height * .7))

    # Header text
    header_text = "Instructions:"
    subheader_text_left = "How to Play:"
    subheader_text_right = "Graphs and Vertex Covers:"

    # Content text
    content_text_left = """The goal of the game is to get all of the animals and plants
                        from one side of the river to the other.\n\n
                        Keyboard Controls:\n
                        Esc - Go back to the Main Menu\n\n
                        Mouse Controls:\n
                        Left click on an animal or plant icon to add it to your boat.\n\n
                        Left click on the arrow at the bottom of the screen to send the boat
                        across the river and deposit its contents on the other side.\n\n
                        Try to get all of the cargo across the river in as few turns as possible!"""
    
    content_text_right = "TBD"

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
    header_rect.center = ((screen_width/2), (screen_height * .15))
    screen.blit(header_object, header_rect)

    # Fill in the subheader information
    subheader_object_left = subheader_font.render(subheader_text_left, True, TEXT_COLOR, SUBHEADER_COLOR_LEFT)
    subheader_rect_left = subheader_object_left.get_rect()
    subheader_rect_left.center = ((screen_width/4), (screen_height * .26))
    screen.blit(subheader_object_left, subheader_rect_left)

    subheader_object_right = subheader_font.render(subheader_text_right, True, TEXT_COLOR, SUBHEADER_COLOR_RIGHT)
    subheader_rect_right = subheader_object_right.get_rect()
    subheader_rect_right.center = ((screen_width/4) + x_offset, (screen_height * .26))
    screen.blit(subheader_object_right, subheader_rect_right)

    # Fill in the text contents
    content_object_left = subheader_font.render(content_text_left, True, TEXT_COLOR, MESSAGE_BACKGROUND_COLOR)
    content_rect_left = content_object_left.get_rect()
    content_rect_left.center = ((screen_width/4), (screen_height * .55))
    #screen.blit(content_object_left, content_rect_left)

    content_object_right = subheader_font.render(content_text_right, True, TEXT_COLOR, MESSAGE_BACKGROUND_COLOR)
    content_rect_right = content_object_right.get_rect()
    content_rect_right.center = ((screen_width/4) + x_offset, (screen_height * .55))
    screen.blit(content_object_right, content_rect_right)

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
        main_menu_button = menu_button.Back_Button(x=width * 0.07, y=height * 0.9)
        
        if main_menu_button.draw_back_button(screen):
            pygame.mixer.Sound.play(click_sound)
            running = False

        pygame.display.update()
    
    return

pygame.quit()