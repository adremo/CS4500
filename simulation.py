# Andrew Morris
# Sound Sources: 
# game_music: https://freesound.org/people/FoolBoyMedia/sounds/257997/
# click_sound: https://freesound.org/people/brandondelehoy/sounds/333428/
# victory_sound: https://freesound.org/people/Eponn/sounds/619832/
# cancel_sound: https://freesound.org/people/plasterbrain/sounds/423167/
# water sound: https://freesound.org/people/thorvandahl/sounds/184200/

import sys
import pygame
import menu_button
import scores
import Graph
import options

#set up screen
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
offset = 0.0

# Colors
white = (255, 255, 255)
green = (82, 216, 50)
blue = (0, 0, 200)
red = (240, 0, 0)

# Fonts
font = pygame.font.Font('freesansbold.ttf', 36)
small_font = pygame.font.Font('freesansbold.ttf', 24)

# Sounds  
click_sound = pygame.mixer.Sound(r'Sounds/click_sound.wav')
victory_sound = pygame.mixer.Sound(r'Sounds/victory_sound.wav')
cancel_sound = pygame.mixer.Sound(r'Sounds/cancel_sound.wav')
water_sound = pygame.mixer.Sound(r'Sounds/water_sound.wav')

# Images
# Unit Images
fox_icon = pygame.image.load(r'Images/Units/Fox.png')
wolf_icon = pygame.image.load(r'Images/Units/Wolf.png')
snake_icon = pygame.image.load(r'Images/Units/Snake.png')
rabbit_icon = pygame.image.load(r'Images/Units/Rabbit.png')
goat_icon = pygame.image.load(r'Images/Units/Goat.png')
monkey_icon = pygame.image.load(r'Images/Units/Monkey.png')
owl_icon = pygame.image.load(r'Images/Units/Owl.png')
sheep_icon = pygame.image.load(r'Images/Units/Sheep.png')
cat_icon = pygame.image.load(r'Images/Units/Cat.png')
dog_icon = pygame.image.load(r'Images/Units/Dog.png')
mouse_icon = pygame.image.load(r'Images/Units/Mouse.png')
chicken_icon = pygame.image.load(r'Images/Units/Chicken.png')
goose_icon = pygame.image.load(r'Images/Units/Goose.png')
squirrel_icon = pygame.image.load(r'Images/Units/Squirrel.png')
frog_icon = pygame.image.load(r'Images/Units/Frog.png')
bug_icon = pygame.image.load(r'Images/Units/Bug.png')
grass_icon = pygame.image.load(r'Images/Units/Grass.png')
carrot_icon = pygame.image.load(r'Images/Units/Carrot.png')
cheese_icon = pygame.image.load(r'Images/Units/Cheese.png')
seeds_icon = pygame.image.load(r'Images/Units/Seeds.png')
broccoli_icon = pygame.image.load(r'Images/Units/Broccoli.png')
banana_icon = pygame.image.load(r'Images/Units/Banana.png')
fruit_icon = pygame.image.load(r'Images/Units/Fruit.png')
nuts_icon = pygame.image.load(r'Images/Units/Nuts.png')
# Other Images
arrow_right_image = pygame.image.load(r'Images/arrow_right_icon.png')
arrow_left_image = pygame.image.load(r'Images/arrow_left_icon.png')
left_side_boat_image = pygame.image.load(r'Images/left_side_boat.png')
right_side_boat_image = pygame.image.load(r'Images/right_side_boat.png')
river_image = pygame.image.load(r'Images/river_image.png')

# Unit string-to-image pairs dict
unit_images = {"Fox": fox_icon,
               "Wolf": wolf_icon,
               "Snake": snake_icon,
               "Rabbit": rabbit_icon,
               "Goat": goat_icon,
               "Monkey": monkey_icon,
               "Owl": owl_icon,
               "Sheep": sheep_icon,
               "Cat": cat_icon,
               "Dog": dog_icon,
               "Mouse": mouse_icon,
               "Chicken": chicken_icon,
               "Goose": goose_icon,
               "Squirrel": squirrel_icon,
               "Frog": frog_icon,
               "Bug": bug_icon,
               "Grass": grass_icon,
               "Carrot": carrot_icon,
               "Cheese": cheese_icon,
               "Seeds": seeds_icon,
               "Broccoli": broccoli_icon,
               "Banana" : banana_icon,
               "Fruit": fruit_icon,
               "Nuts": nuts_icon
}

# Screen coordinates
screen_width = screen.get_width()
screen_height = screen.get_height()
left_side_x = screen_width * 0.25
right_side_x = screen_width * 0.75
boat_left_x = screen_width * 0.34
boat_right_x = screen_width * 0.68
boat_y = screen_height * 0.55

# Generate buttons and UI images
travel_button_left = menu_button.Button(screen_width * 0.5, screen_height * 0.85, arrow_right_image)
travel_button_right = menu_button.Button(screen_width * 0.5, screen_height * 0.85, arrow_left_image)
travel_button_left.image = pygame.transform.scale(travel_button_left.image, (int(screen_width * .08), int(screen_height * .12)))
travel_button_right.image = pygame.transform.scale(travel_button_right.image, (int(screen_width * .08), int(screen_height * .12)))
river_image = pygame.transform.scale(river_image, (screen_width * 0.42, screen_height))
left_side_boat_image = pygame.transform.scale(left_side_boat_image, (screen_width * 0.18, screen_height * 0.13))
right_side_boat_image = pygame.transform.scale(right_side_boat_image, (screen_width * 0.18, screen_height * 0.13))

# Classes to hold units, track game state 
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

# Display info to the screen, including labels and and game state info, and some non-interactive graphics
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

                # If the conflict has been resolved by placing a unit into the boat, generate strikethrough and different color text
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
        
# Returns list of current conflicts found on the side that boat is on (which animals CAN eat something after boat leaves shore)
def check_unit_conflicts(left_side, right_side, side, unit_graph):
    if side == 0:
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
def run_simulation(game_graph, boat_size):
    volume = options.control_sound_volume(0.6)
    pygame.mixer.Sound.set_volume(click_sound, volume)
    pygame.mixer.Sound.set_volume(victory_sound, volume)
    pygame.mixer.Sound.set_volume(cancel_sound, volume)
    pygame.mixer.Sound.set_volume(water_sound, volume)
    
    unit_graph = game_graph
    
    # Hold buttons for the possible units 
    unit_buttons_left = {}
    unit_buttons_right = {}
    unit_buttons_boat = {}

    # Play water sound until game is complete
    pygame.mixer.Sound.play(water_sound, -1)
    
    # Initialize variables and objects
    left_side = left_side_class(len(unit_graph))
    right_side = right_side_class(len(unit_graph))
    boat = boat_class(boat_size, 0)
    win_condition = len(unit_graph)
    turn_count = 0

    for unit in unit_graph:
        left_side.units.append(unit)
    print(unit_graph)    
    # Main Simulation loop: runs until win condition is met(# of units on right side of river is equal to # in units graph)
    run = True
    while run:
        screen.fill(green)
        screen.blit(river_image, (screen_width * 0.37, 0))

        current_conflicts = check_unit_conflicts(left_side, right_side, boat.side, unit_graph)
        display_UI(turn_count, boat.size, unit_graph, current_conflicts)
                
        # Generate buttons for every possible unit and available positions for each unit
        left_count = 0
        for unit in left_side.units:
            left_button = menu_button.Unit_Button(unit, left_side_x, screen_height * (0.15 + (left_count / 11)), unit_images[unit])
            unit_buttons_left[unit] = (left_button)
            left_count += 1

        right_count = 0
        for unit in right_side.units:
            right_button = menu_button.Unit_Button(unit, right_side_x, screen_height * (0.15 + (right_count / 11)), unit_images[unit])
            unit_buttons_right[unit] = (right_button)
            right_count += 1
            
        boat_count = 0
        for unit in boat.units:
            if boat.side == 0:
                boat_button = menu_button.Unit_Button(unit, screen_width * 0.34, screen_height * (0.45 + (boat_count / 11)), unit_images[unit])
            else:
                boat_button = menu_button.Unit_Button(unit, screen_width * 0.68, screen_height * (0.45 + (boat_count / 11)), unit_images[unit])
            unit_buttons_boat[unit] = (boat_button)
            boat_count += 1

        # Handle pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    turn_count = -1
                    run = False
        
        pygame.time.wait(40)
        clicked = False
        # Main logic for moving units around based on graphical user input, before attempting to cross river            
        for unit in unit_graph:
            if left_side.units.__contains__(unit):
                if unit_buttons_left[unit].draw_unit(screen) and clicked == False:
                    pygame.time.wait(80)
                    clicked = True
                    
                    if len(boat.units) < boat.size and boat.side == 0:
                        pygame.mixer.Sound.play(click_sound)
                        left_side.units.remove(unit)
                        boat.units.append(unit)
            elif right_side.units.__contains__(unit):
                if unit_buttons_right[unit].draw_unit(screen) and clicked == False:
                    pygame.time.wait(80)
                    clicked = True
                    
                    if len(boat.units) < boat.size and boat.side == 1:
                        pygame.mixer.Sound.play(click_sound)
                        right_side.units.remove(unit)
                        boat.units.append(unit)
            elif boat.units.__contains__(unit):
                if unit_buttons_boat[unit].draw_unit(screen) and clicked == False:
                    pygame.time.wait(80)
                    clicked = True
                    
                    pygame.mixer.Sound.play(click_sound)
                    boat.units.remove(unit)
                    if boat.side == 0:
                        left_side.units.append(unit)
                    else:
                        right_side.units.append(unit) 

        if travel_button_left.draw(screen) and clicked == False:
            clicked = True
            # if travel button on bottom is pressed, check to see if there are any animals on boat's current side which will eat each other when boat/farmer leaves
            current_conflicts = check_unit_conflicts(left_side, right_side, boat.side, unit_graph)
            if len(current_conflicts) == 0:
                pygame.mixer.Sound.play(click_sound)
                
                if boat.side == 0:
                    print("Transferring units in boat(" + str(boat.units) + ") to right side of the river")
                    boat.side = 1
                    for u in boat.units:
                        right_side.units.append(u)
                    boat.units.clear()
                elif boat.side == 1:
                    print("Transferring units in boat(" + str(boat.units) + ") to left side of the river")
                    boat.side = 0
                    for u in boat.units:
                        left_side.units.append(u)
                    boat.units.clear()
                turn_count += 1
            else:
                pygame.mixer.Sound.play(cancel_sound)
                print("Unit conflict present, cannot transfer boat")
                
        if len(right_side.units) == win_condition:
            print("Game won, all units have reached right side of river.")
            pygame.mixer.Sound.stop(water_sound)
            pygame.mixer.Sound.play(victory_sound)

            run = False

        pygame.display.update()
    
    pygame.mixer.Sound.stop(water_sound)
    return turn_count
