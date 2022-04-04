import tkinter as tk
import sys
import pygame
import math
import menu_button
from pygame.locals import *


# Main
root = tk.Tk()
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
waterBottom = screen_height / 2
waterBottom2 = screen_height / 3
water_start_x = 0
water_width = screen_width
water_box_start_y = screen_height
water_box_height = int(waterBottom2)
amplitude = 5
wave_offset_increment = 2.0
base_y = water_box_start_y - (75 * amplitude)
water_box_rect = Rect(water_start_x, water_box_start_y, water_width, water_box_height)
title_location_x = root.winfo_screenwidth() * .235
title_location_y = root.winfo_screenheight() * .08
grass_location1_x = root.winfo_screenwidth() * .1
grass_location1_y = root.winfo_screenheight() * .08
grass_location2_x = root.winfo_screenwidth() * .27
grass_location2_y = root.winfo_screenheight() * .46
grass_location3_x = root.winfo_screenwidth() * .78
grass_location3_y = root.winfo_screenheight() * .34
menu_button_image_location_x = root.winfo_screenwidth() * .4255
easy_button_image_location_y = root.winfo_screenheight() * .26
hard_button_image_location_y = root.winfo_screenheight() * .33
options_button_image_location_y = root.winfo_screenheight() * .4
instructions_button_image_location_y = root.winfo_screenheight() * .465
credits_button_image_location_y = root.winfo_screenheight() * .535



def close():
    root.withdraw()  # if you want to bring it back
    sys.exit()  # if you want to exit the entire thing


def handleEvents():
    for event2 in pygame.event.get():
        if event2.type == QUIT:
            return
        elif event2.type == KEYDOWN:
            if event2.key == K_ESCAPE:
                pygame.quit()
                return


# Images
title_image = pygame.image.load(r'Images/River_Crossing_Title.png').convert_alpha()
grass_image = pygame.image.load(r'Images/Grass.png').convert_alpha()
easy_image = pygame.image.load(r'Images/Easy_Button.png').convert_alpha()
hard_image = pygame.image.load(r'Images/Hard_Button.png').convert_alpha()
options_image = pygame.image.load(r'Images/Options_Button.png').convert_alpha()
instructions_image = pygame.image.load(r'Images/Instructions_Button.png').convert_alpha()
credits_image = pygame.image.load(r'Images/Credit_Button.png').convert_alpha()

# Buttons
easy_button = menu_button.Button(menu_button_image_location_x, easy_button_image_location_y, easy_image, 1)
hard_button = menu_button.Button(menu_button_image_location_x, hard_button_image_location_y, hard_image, 1)
options_button = menu_button.Button(menu_button_image_location_x, options_button_image_location_y, options_image, 1)
instructions_button = menu_button.Button(menu_button_image_location_x, instructions_button_image_location_y, instructions_image, 1)
credits_button = menu_button.Button(menu_button_image_location_x, credits_button_image_location_y, credits_image, 1)





run = True
while run:
    handleEvents()

    screen.fill(green)
    pygame.draw.rect(screen, blue, water_box_rect)
    # Title Location
    screen.blit(title_image, (title_location_x, title_location_y))
    screen.blit(grass_image, (grass_location1_x, grass_location1_y))
    screen.blit(grass_image, (grass_location2_x, grass_location2_y))
    screen.blit(grass_image, (grass_location3_x, grass_location3_y))
    # screen.blit(easy_image, (easy_button_image_location_x, easy_button_image_location_y))

    if easy_button.draw(screen):
        print('easy')
        run = False

    if hard_button.draw(screen):
        print('easy')
        run = False

    if options_button.draw(screen):
        print('easy')
        run = False

    if instructions_button.draw(screen):
        print('easy')
        run = False

    if credits_button.draw(screen):
        print('easy')
        run = False

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

    pygame.display.flip()
    pygame.time.wait(10)
    pygame.display.update()

pygame.quit()