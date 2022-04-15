# As of right now the user feedback in terms of whether boat can/cannot cross, 
# when boat is crossing and with what, and when game is won, are all in console
#
# To do: Sounds, adding support for more than 1 game graph, create and include algorithm for fastest solution
#        Also a ton of UI/graphics stuff like swapping bottom arrow left/right, adding labels, arranging units
#        better, labeling things, highlighting which units are in conflict, and animations.

import sys
import pygame
import tkinter as tk
import menu_button
import scores

#set up screen again
root = tk.Tk()
root.withdraw()
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
offset = 0.0

#test graphs for now
easy_graph = { 
    "fox" : {"rabbit"},
    "rabbit" : {"cabbage"},
    "cabbage" : {}
    }

medium_graph = { 
    "fox" : {"rabbit"},
    "wolf" : {"goat", "rabbit"},
    "rabbit" : {"cabbage"},
    "goat" : {"cabbage, hay"},
    "cabbage" : {},
    "hay" : {}
    }

# Colors
white = (255, 255, 255)
green = (82, 216, 50)
blue = (0, 0, 200)

font = pygame.font.Font('freesansbold.ttf', 32)

# Screen coordinates
screen_width = screen.get_width()
screen_height = screen.get_height()
left_side_x = screen_width * 0.25
right_side_x = screen_width * 0.75
boat_left_x = screen_width * 0.3
boat_right_x = screen_width * 0.58
boat_y = screen_height * 0.55

# load images
fox_icon = pygame.image.load(r'Images/fox_icon.png')
rabbit_icon = pygame.image.load(r'Images/rabbit_icon.png')
cabbage_icon = pygame.image.load(r'Images/cabbage_icon.png')
arrow_right_image = pygame.image.load(r'Images/arrow_right_icon.png')
arrow_left_image = pygame.image.load(r'Images/arrow_left_icon.png')
left_side_boat_image = pygame.image.load(r'Images/left_side_boat.png')
right_side_boat_image = pygame.image.load(r'Images/right_side_boat.png')
river_image = pygame.image.load(r'Images/river_image.png')

# Generate buttons
fox_button_left = menu_button.Unit_Button(left_side_x, screen_height * 0.18, fox_icon)
rabbit_button_left = menu_button.Unit_Button(left_side_x, screen_height * 0.26, rabbit_icon)
cabbage_button_left = menu_button.Unit_Button(left_side_x, screen_height * 0.34, cabbage_icon)
fox_button_right = menu_button.Unit_Button(right_side_x, screen_height * 0.18, fox_icon)
rabbit_button_right = menu_button.Unit_Button(right_side_x, screen_height * 0.26, rabbit_icon)
cabbage_button_right = menu_button.Unit_Button(right_side_x, screen_height * 0.34, cabbage_icon)
fox_button_boat = menu_button.Unit_Button(screen_width * 0.5, screen_height * 0.28, fox_icon)
rabbit_button_boat = menu_button.Unit_Button(screen_width * 0.5, screen_height * 0.36, rabbit_icon)
cabbage_button_boat = menu_button.Unit_Button(screen_width * 0.5, screen_height * 0.44, cabbage_icon)
travel_button = menu_button.Button(screen_width * 0.5, screen_height * 0.9, arrow_right_image)

travel_button.image = pygame.transform.scale(travel_button.image, (int(screen_width * .04), int(screen_height * .06)))
river_image = pygame.transform.scale(river_image, (screen_width * 0.3, screen_height))
left_side_boat_image = pygame.transform.scale(left_side_boat_image, (screen_width * 0.18, screen_height * 0.13))
right_side_boat_image = pygame.transform.scale(right_side_boat_image, (screen_width * 0.18, screen_height * 0.13))

# lists to hold sets of buttons for easier access
unit_buttons_left = {
    "fox" : fox_button_left,
    "rabbit" : rabbit_button_left,
    "cabbage" : cabbage_button_left
}

unit_buttons_right = {
    "fox" : fox_button_right,
    "rabbit" : rabbit_button_right,
    "cabbage" : cabbage_button_right
}

unit_buttons_boat = {
    "fox" : fox_button_boat,
    "rabbit" : rabbit_button_boat,
    "cabbage" : cabbage_button_boat
}

# units is only for visual display, units are never actually "in the boat"
class boat_class:
  def __init__(self, size, side):
    self.size = size
    self.side = side
    self.units = []
    
class left_side_class:
  def __init__(self, size):
    self.size = size
    self.units = []
    
class right_side_class:
  def __init__(self, size):
    self.size = size
    self.units = []

# need to add more UI elements, and also text messages for when game events occur, also sound
def display_UI(turn_count, boat_size):
    turn_text = "Trips Taken: " + str(turn_count)
    turns_display = font.render(turn_text, True, blue, green)
    turns_rect = turns_display.get_rect()
    turns_rect.center = (screen_width * 0.1, screen_height * 0.1)
    screen.blit(turns_display, turns_rect)
    
    capacity_text = "Boat Capacity: " + str(boat_size)
    capacity_display = font.render(capacity_text, True, white)
    capacity_rect = turns_display.get_rect()
    capacity_rect.center = (screen_width * 0.5, screen_height * 0.1)
    screen.blit(capacity_display, capacity_rect)
    
    if turn_count % 2 == 0:
        screen.blit(left_side_boat_image, (boat_left_x, boat_y))
    else:
        screen.blit(right_side_boat_image, (boat_right_x, boat_y))

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
                running = False
        
# Returns true if there are NO unit conflicts on boat's current side of the river (not in boat)        
def check_unit_conflicts(left_side, right_side, boat, unit_graph):
    if boat.side == 0:
        unit_list = left_side.units
    else:
        unit_list = right_side.units
        
    conflicts = []
    for unit in unit_list:
        for food in unit_graph[unit]:
            if unit_list.__contains__(food):
                conflict = (unit, food)
                conflicts.append(conflict)

    if len(conflicts) == 0:
        return False
    else:
        print("Conflicts present on shore: " + str(conflicts))
        return True

# Game simulation function, contains main game simulation loop, returns turns used after game is won
def run_simulation(difficulty_settings):
    # Initial setup, graphs and boat sizes can be changed later on
    if difficulty_settings == 0:
        # these should be changed later to be equal to whatever input boat size is
        boat_size = 1
        unit_graph = easy_graph
    elif difficulty_settings == 1:  # this doesn't work yet, need to add more images/buttons/etc for units within the larger graph(s)
        boat_size = 3
        unit_graph = medium_graph
    elif difficulty_settings == 2:
        boat_size = 3
        #need hard graph, and later can use randomized graphs
        unit_graph = medium_graph
        
    left_side = left_side_class(len(unit_graph))
    right_side = right_side_class(len(unit_graph))
    boat = boat_class(boat_size, 0)
    win_condition = len(unit_graph)
    turn_count = 0

    for unit in unit_graph:
        left_side.units.append(unit)
    
    # simulation loop
    run = True
    while run:
        screen.fill(green)
        screen.blit(river_image, (screen_width * 0.37, 0))

        handle_events()
        display_UI(turn_count, boat.size)

        for unit in unit_graph.keys():
            if left_side.units.__contains__(unit):
                if unit_buttons_left[unit].draw_unit(screen):
                    if len(boat.units) < boat.size and boat.side == 0:
                        left_side.units.remove(unit)
                        boat.units.append(unit)
            elif right_side.units.__contains__(unit):
                if unit_buttons_right[unit].draw_unit(screen):
                    if len(boat.units) < boat.size and boat.side == 1:
                        right_side.units.remove(unit)
                        boat.units.append(unit)
            elif boat.units.__contains__(unit):
                if unit_buttons_boat[unit].draw_unit(screen):
                    boat.units.remove(unit)
                    if boat.side == 0:
                        left_side.units.append(unit)
                    else:
                        right_side.units.append(unit) 
                
        if travel_button.draw(screen):
            if check_unit_conflicts(left_side, right_side, boat, unit_graph):
                print("Unit conflict present, cannot transfer boat")
            else:
                if boat.side == 0:
                    print("Transferring units in boat(" + str(boat.units) + ") to right side of the river")
                    boat.side = 1
                    for u in boat.units:
                        right_side.units.append(u)
                        boat.units.remove(u)
                else:
                    print("Transferring units in boat(" + str(boat.units) + ") to left side of the river")
                    boat.side = 0
                    for u in boat.units:
                        left_side.units.append(u)
                        boat.units.remove(u)
                    
                turn_count += 1
        
        if len(right_side.units) == win_condition:
            print("All units have reached right side of river. You win!")
            run = False

        pygame.time.wait(10)
        pygame.display.update()
        
    return turn_count
