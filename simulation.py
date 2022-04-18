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
red = (240, 0, 0)

font = pygame.font.Font('freesansbold.ttf', 36)
small_font = pygame.font.Font('freesansbold.ttf', 24)

# Screen coordinates
screen_width = screen.get_width()
screen_height = screen.get_height()
left_side_x = screen_width * 0.25
right_side_x = screen_width * 0.75
boat_left_x = screen_width * 0.34
boat_right_x = screen_width * 0.68
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
travel_button_left = menu_button.Button(screen_width * 0.5, screen_height * 0.85, arrow_right_image)
travel_button_right = menu_button.Button(screen_width * 0.5, screen_height * 0.85, arrow_left_image)


travel_button_left.image = pygame.transform.scale(travel_button_left.image, (int(screen_width * .08), int(screen_height * .12)))
travel_button_right.image = pygame.transform.scale(travel_button_right.image, (int(screen_width * .08), int(screen_height * .12)))
river_image = pygame.transform.scale(river_image, (screen_width * 0.42, screen_height))
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
    self.side = side # 0 = left side of river, 1 = right side
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
def display_UI(turn_count, boat_size, unit_graph, current_conflicts):
    # Display current number of turns/trips used
    turn_text = "Trips Taken: " + str(turn_count)
    turns_display = font.render(turn_text, True, blue, green)
    turns_rect = turns_display.get_rect()
    turns_rect.center = (screen_width * 0.1, screen_height * 0.1)
    screen.blit(turns_display, turns_rect)
    
    # Display max capacity of the boat
    capacity_text = "Boat Capacity: " + str(boat_size)
    capacity_display = font.render(capacity_text, True, white)
    capacity_rect = capacity_display.get_rect()
    capacity_rect.center = (screen_width * 0.5, screen_height * 0.1)
    screen.blit(capacity_display, capacity_rect)
    
    # Display label for travel button
    travel_text = "Send Boat Across"
    travel_display = font.render(travel_text, True, red)
    travel_rect = travel_display.get_rect()
    travel_rect.center = (screen_width * 0.54, screen_height * 0.97)
    screen.blit(travel_display, travel_rect)
    
    # Display conflicts on left side of screen    
    units = []
    for unit in unit_graph:
        units.append(unit)
        
    conflict_count = 0
    
    for unit in units:
        for food in unit_graph[unit]:
            if units.__contains__(food):
                conflict_count += 1
                conflict = (unit, food)
                conflict_text = str(unit) + " eats " + str(food)

                # If the conflict has been resolved by placing a unit into the boat, strikethrough and different color text
                if current_conflicts.__contains__(conflict) == False:
                    conflict_display = small_font.render(conflict_text, True, blue, green)
                    conflict_rect = conflict_display.get_rect()
                    conflict_rect.center = (screen_width * 0.09, screen_height * (0.18 + (conflict_count / 45)))
                else:
                    conflict_display = small_font.render(conflict_text, True, red, green)
                    conflict_rect = conflict_display.get_rect()
                    conflict_rect.center = (screen_width * 0.11, screen_height * (0.18 + (conflict_count / 45)))

                screen.blit(conflict_display, conflict_rect)
                
                if current_conflicts.__contains__(conflict) == False:
                    pygame.draw.lines(screen, blue, True, [(conflict_rect.left, conflict_rect.centery), (conflict_rect.right, conflict_rect.centery)], 3)
    
    conflict_title = "Conflicts: " + str(len(current_conflicts))
    conflict_title_display = font.render(conflict_title, True, blue)
    title_rect = conflict_title_display.get_rect()
    title_rect.center = (screen_width * 0.09, screen_height * 0.17)
    screen.blit(conflict_title_display, title_rect)
    
    # Display the boat on the screen based on turn
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
        
# Returns list of current conflicts found on the side that boat is on (which animals CAN eat something after boat leaves shore)
def check_unit_conflicts(left_side, right_side, boat, unit_graph):
    if boat.side == 0:
        unit_list = left_side.units
    else:
        unit_list = right_side.units
        
    current_conflicts = []
    for unit in unit_list:
        for food in unit_graph[unit]:
            if unit_list.__contains__(food):
                conflict = (unit, food)
                current_conflicts.append(conflict)

    return current_conflicts

# Game simulation function, contains main game simulation loop, returns turns used after game is won
def run_simulation(difficulty_setting, boat_size):
    # Initial setup, graphs can be changed later on when we get different graph stuff in
    if difficulty_setting == 0:
        unit_graph = easy_graph
    elif difficulty_setting == 1:  # this doesn't work yet, need to add more images/buttons/etc for units within the larger graph(s)
        unit_graph = medium_graph
    elif difficulty_setting == 2:
        #need hard graph, and later can use randomized graphs
        unit_graph = medium_graph
    
    left_side = left_side_class(len(unit_graph))
    right_side = right_side_class(len(unit_graph))
    boat = boat_class(boat_size, 0)
    win_condition = len(unit_graph)
    turn_count = 0

    for unit in unit_graph:
        left_side.units.append(unit)
    
    # Main Simulation loop: runs until win condition is met(# of units on right side of river is equal to # in units graph)
    run = True
    while run:
        screen.fill(green)
        screen.blit(river_image, (screen_width * 0.37, 0))

        handle_events()
        
        current_conflicts = check_unit_conflicts(left_side, right_side, boat, unit_graph)
        display_UI(turn_count, boat.size, unit_graph, current_conflicts)

        # Main logic for moving units around based on graphical user input, before attempting to cross river
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

        if travel_button_left.draw(screen):
            # if travel button on bottom is pressed, check to see if there are any animals on boat's current side which will eat each other when boat/farmer leaves
            current_conflicts = check_unit_conflicts(left_side, right_side, boat, unit_graph)
            if len(current_conflicts) == 0:
                if boat.side == 0:
                    print("Transferring units in boat(" + str(boat.units) + ") to right side of the river")
                    boat.side = 1
                    for u in boat.units:
                        right_side.units.append(u)
                        boat.units.remove(u)
                elif boat.side == 1:
                    print("Transferring units in boat(" + str(boat.units) + ") to left side of the river")
                    boat.side = 0
                    for u in boat.units:
                        left_side.units.append(u)
                        boat.units.remove(u)
                turn_count += 1
            else:
                print("Unit conflict present, cannot transfer boat")
                
        if len(right_side.units) == win_condition:
            print("All units have reached right side of river. You win!")
            run = False

        pygame.time.wait(15)
        pygame.display.update()
        
    return turn_count