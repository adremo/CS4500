# Author: Tiana Madison
# Date: 25 April 2022
# Class: CS 4500
# ========================================================================================================
# Description: This program handles the options menu.
# =========================================================================================================
# Central Data Structures used: Dictionaries
# =========================================================================================================
# External Files: json (There is no need to add anything, the program will create the necessary files)
# =========================================================================================================
# External Sources used: Python 3.10.4 Documentation: https://docs.python.org/3/library/json.html
# Pygame Documenation: https://www.pygame.org/docs/ref/mixer.html 
# =========================================================================================================
import re
import pygame
import json
import sys
import menu_button
from pygame.locals import *

# Setting up window
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
offset = 0.0

def checkSounds():
    try:
        with open("./options.json", "r+", encoding="utf-8") as f:
            sound_options = json.load(f)

    except FileNotFoundError:
        sound_options = {
                            "music": True,
                            "sounds": True       
                        }

        f = open("./options.json", "w") # Create the new local storage file
        json.dump(sound_options, f, indent=4) # Save the data to the new json file
    
    return sound_options

def control_sound_volume(default):
    sound_options = checkSounds()
    if sound_options["sounds"] == False:
        volume = 0
    else:
        volume = default
    return volume

def toggle_volume_sound():
    options = checkSounds()
    if options["sounds"] == False:
        options["sounds"] = True
    else:
        options["sounds"] = False
    
    f = open("./options.json", "w") # Create the new local storage file
    json.dump(options, f, indent=4) # Save the data to the new json file
    return options

def format_options(root, screen, options):
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
    SUBHEADER_COLOR_EASY = teal
    SUBHEADER_COLOR_HARD = teal
    MESSAGE_BACKGROUND_COLOR = teal
    ENTRY_BACKGROUND_1 = Color(54, 154, 181)
    ENTRY_BACKGROUND_2 = light_teal

    # Font
    header_font = pygame.font.SysFont(None, 120)
    subheader_font = pygame.font.SysFont(None, 50)
    entry_font = pygame.font.SysFont(None, 40)

    # Surface building and positioning
    x_offset = 900
    y_offset = 50
    starting_offset = 165 + (y_offset * 2.5)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight() 
    button_base_x = (screen_width/2) - 200
    button_base_y = (screen_width/2) - 150
    background_sub_rect = Rect(50, (screen_height/2) - 500, screen_width - 100, 1000)
    header_zone = Rect(100, 100, screen_width - 200, 150)
    content_zone = Rect(100, starting_offset, screen_width - 200, 700)
    subheader_zone_easy = Rect(100, 210, (screen_width/2) - 200, 70)
    subheader_zone_hard = Rect(1000, 210, (screen_width/2) - 150, 70)

    # Header text
    header_text = "Options"
    music_text = "Music:"
    sounds_text = "Sounds:"

    # Setting up the main surfaces
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, SUB_BACKGROUND_COLOR, background_sub_rect)
    pygame.draw.rect(screen, HEADER_COLOR, header_zone)
    pygame.draw.rect(screen, HEADER_COLOR, content_zone)
    #pygame.draw.rect(screen, SUBHEADER_COLOR_EASY, subheader_zone_easy)
    #pygame.draw.rect(screen, SUBHEADER_COLOR_HARD, subheader_zone_hard)

    # Fill in the header information
    header_object = header_font.render(header_text, True, TEXT_COLOR, HEADER_COLOR)
    header_rect = header_object.get_rect()
    header_rect.center = ((screen_width/2), 175)
    screen.blit(header_object, header_rect)

    # Fill in the options menu contents
    music_object = subheader_font.render(music_text, True, TEXT_COLOR, black)
    music_rect = music_object.get_rect()
    music_rect.center = ((screen_width/4), 600)
    screen.blit(music_object, music_rect)

    sounds_object = subheader_font.render(sounds_text, True, TEXT_COLOR, black)
    sounds_rect = sounds_object.get_rect()
    sounds_rect.center = ((screen_width/4), 800)
    screen.blit(sounds_object, sounds_rect)

    arrow_right = pygame.image.load(r'Images/arrow_right_icon.png')
    arrow_left = pygame.image.load(r'Images/arrow_left_icon.png')

    # Buttons for muting the music
    left_music_button = menu_button.Custom_Button(x=button_base_x, y=button_base_y, image=arrow_left)
    right_music_button = menu_button.Custom_Button(x=button_base_x + 100, y=button_base_y + 100, image=arrow_right)

    # Menu Noises
    click_sound = pygame.mixer.Sound(r'Sounds/click_sound.wav')
    volume = control_sound_volume(0.5)
    pygame.mixer.Sound.set_volume(click_sound, volume)

    if left_music_button.draw_custom_button(screen):
        options = toggle_volume_sound()
        volume = control_sound_volume(0.5)
        pygame.mixer.Sound.set_volume(click_sound, volume)
        pygame.mixer.Sound.play(click_sound)
        pygame.time.wait(200)
    
    if right_music_button.draw_custom_button(screen):
        pygame.mixer.Sound.play(click_sound)

def display_options_menu(root, screen, options):
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
        
        format_options(root, screen, options)

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