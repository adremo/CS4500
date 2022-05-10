# Michael Schweighauser, Andrew Morris, Tiana Madison
# 4/3/2022
# CS 4500 Spring 2022
# Main menu screen displays graphics and plays sounds, various buttons allow user to 
# access the different parts of the game. Gets sound settings and begins music playback,
# sets up the game simulation and calls function to run it using game graph input, and 
# takes the user's score form simulation and input username recieved from high_score_input
# to update the high scores file.
# External Files: Sounds and images used in the 'Sounds' and 'Images' sections
# Central Data Structures: None

# Sound Sources: 
# game_music: https://freesound.org/people/FoolBoyMedia/sounds/257997/
# click_sound: https://freesound.org/people/brandondelehoy/sounds/333428/
# victory_sound: https://freesound.org/people/Eponn/sounds/619832/
# cancel_sound: https://freesound.org/people/plasterbrain/sounds/423167/
# water sound: https://freesound.org/people/thorvandahl/sounds/184200/

# Artwork by Michael Schweighauser (Main Menu) and Alex Chalmers (Game Unit images)
# Additional menu design by Tiana Madison

import tkinter as tk
import sys
import pygame
import math
import json
import menu_button
import scores
import Graph
from pygame.locals import *
from instructions import display_help_menu
from leaderboard import display_leaderboard
from options import display_options_menu, checkSounds, control_sound_volume
from simulation import run_simulation, check_unit_conflicts
from high_score_input import get_username

# Main window
root = tk.Tk()
root.withdraw()
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
offset = 0.0

# Color List
black = Color(0, 0, 0)
blue = Color(0, 0, 200)
light_blue = Color(30, 30, 230)
lighter_blue = Color(80, 80, 245)
brown = Color(100, 70, 50)
green = Color(82, 216, 50)

# variables
i = 0
two_pi = 2.0 * math.pi
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
waterBottom = screen_height / 3
waterBottom2 = screen_height / 4
water_start_x = 0
water_width = screen_width
water_box_start_y = screen_height
water_box_height = int(waterBottom2)
amplitude = 5
wave_offset_increment = 2.0
base_y = water_box_start_y - (75 * amplitude)
water_box_rect = Rect(water_start_x, water_box_start_y, water_width, water_box_height)
title_location_x = screen_width * .22
title_location_y = screen_height * .05
title_width = screen_width * .59
title_height = screen_height * .18
grass_location1_x = screen_width * .1
grass_location1_y = screen_height * .08
grass_location2_x = screen_width * .27
grass_location2_y = screen_height * .46
grass_location3_x = screen_width * .78
grass_location3_y = screen_height * .34
menu_button_image_location_x = screen_width * .44
easy_button_image_location_y = screen_height * .28
hard_button_image_location_y = screen_height * .36
options_button_image_location_y = screen_height * .44
instructions_button_image_location_y = screen_height * .52
leaderboard_button_image_location_y = screen_height * .60


def close():
    root.withdraw()
    sys.exit()


def handleEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
                running = False

# Sounds
# Game Music, loop by setting -1 as the .play() 'loops' param
pygame.mixer.music.load(r'Sounds/game_music.wav')
sound_options = checkSounds()
if sound_options["music"] == False:
    pygame.mixer.music.set_volume(0)
else:
    pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(-1)
# Menu Noises
click_sound = pygame.mixer.Sound(r'Sounds/click_sound.wav')

# Images
title_image = pygame.image.load(r'Images/River_Crossing_Title.png').convert_alpha()
title_image = pygame.transform.scale(title_image, (title_width, title_height))
grass_image = pygame.image.load(r'Images/Grass.png').convert_alpha()
easy_image = pygame.image.load(r'Images/Easy_Button.png').convert_alpha()
hard_image = pygame.image.load(r'Images/Hard_Button.png').convert_alpha()
options_image = pygame.image.load(r'Images/Options_Button.png').convert_alpha()
instructions_image = pygame.image.load(r'Images/Instructions_Button.png').convert_alpha()
leaderboard_image = pygame.image.load(r'Images/Leaderboard_Button.png').convert_alpha()

# Buttons
easy_button = menu_button.Button(menu_button_image_location_x, easy_button_image_location_y, easy_image)
hard_button = menu_button.Button(menu_button_image_location_x, hard_button_image_location_y, hard_image)
options_button = menu_button.Button(menu_button_image_location_x, options_button_image_location_y, options_image)
instructions_button = menu_button.Button(menu_button_image_location_x, instructions_button_image_location_y,
                                         instructions_image)
leaderboard_button = menu_button.Button(menu_button_image_location_x, leaderboard_button_image_location_y, leaderboard_image)

# Main Menu Loop, dynamically displays graphics and plays feedback sounds, user buttons displayed below
# the game's title are as follows: Easy and Hard launch game simulations of the respective difficulty, 
# Options, Instructions, and Leaderboard display the respective page.
run = True
while run:
    sound_options = checkSounds() # Check the external sound option values
    volume = control_sound_volume(0.5)
    pygame.mixer.Sound.set_volume(click_sound, volume)
    handleEvents()

    screen.fill(green)
    pygame.draw.rect(screen, blue, water_box_rect)
    
    # Title Location
    screen.blit(title_image, (title_location_x, title_location_y))
    screen.blit(grass_image, (grass_location1_x, grass_location1_y))
    screen.blit(grass_image, (grass_location2_x, grass_location2_y))
    screen.blit(grass_image, (grass_location3_x, grass_location3_y))

    if easy_button.draw(screen):
        pygame.mixer.Sound.play(click_sound)
                
        graph = Graph.Graph()
        min_boat_size = 0
        conflicts = []
        while min_boat_size != 1 or conflicts.__len__() < 2:
            graph.generateGraph(3)
            conflicts = check_unit_conflicts(graph, graph, 0, graph.units)
            print(conflicts)
            min_boat_size = graph.getMinimumBoatSize()
            print(min_boat_size)
            
        turn_count = run_simulation(graph.units, min_boat_size)
                
        if turn_count > 0:
            print("Turns used: " + str(turn_count))
            username = get_username(turn_count)
            pygame.time.wait(400)
            scores.save_score("easy", username, turn_count)

    if hard_button.draw(screen):
        pygame.mixer.Sound.play(click_sound)
        
        graph = Graph.Graph()
        min_boat_size = 0
        conflicts = []
        while min_boat_size != 3 or conflicts.__len__() < 4:
            graph.generateGraph(7)
            conflicts = check_unit_conflicts(graph, graph, 0, graph.units)
            print(conflicts)
            min_boat_size = graph.getMinimumBoatSize()
            print(min_boat_size)
            
        turn_count = run_simulation(graph.units, min_boat_size)
        
        if turn_count > 0:
            print("Turns used: " + str(turn_count))
            username = get_username(turn_count)
            pygame.time.wait(400)
            scores.save_score("hard", username, turn_count)

    if options_button.draw(screen):
        pygame.mixer.Sound.play(click_sound)
        display_options_menu(root=root, screen=screen, options=sound_options)

    if instructions_button.draw(screen):
        pygame.mixer.Sound.play(click_sound)
        display_help_menu(root=root, screen=screen)

    if leaderboard_button.draw(screen):
        pygame.mixer.Sound.play(click_sound)
        display_leaderboard(root=root, screen=screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Running River
    for i in range(water_width):
        pixelX = i + water_start_x
        rad = ((float(i) + offset) / 90.0) * two_pi
        mod = math.sin(rad) * amplitude
        pixelY = round(base_y + mod)
        pygame.draw.line(screen, blue, (pixelX, pixelY + 7), (pixelX, water_box_start_y), 1)
        pygame.draw.line(screen, light_blue, (pixelX, pixelY + 3), (pixelX, pixelY + 6), 2)
        pygame.draw.line(screen, lighter_blue, (pixelX, pixelY), (pixelX, pixelY + 2), 2)

    offset += wave_offset_increment
    if offset > 90.0:
        offset -= 90.0

    pygame.time.wait(10)
    pygame.display.update()

pygame.quit()
