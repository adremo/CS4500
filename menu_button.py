import pygame
import tkinter as tk

# Main window repeated
root = tk.Tk()
root.withdraw()
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
offset = 0.0


class Button:
    def __init__(self, x, y, image):
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        self.image = pygame.transform.scale(image, (int(width * .11), int(height * .07)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()
# Hover and Clicked
        if self.rect.collidepoint(pos):
            width = root.winfo_screenwidth()
            height = root.winfo_screenheight()
            menu_boat_image = pygame.image.load(r'Images/Menu_Boat.png').convert_alpha()
            menu_boat_image = pygame.transform.scale(menu_boat_image, (width * .08, height * .072))
            surface.blit(menu_boat_image, (self.rect.x * .8, self.rect.y))

            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                print('clicked')
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
    
class Unit_Button:
    def __init__(self, name, x, y, image):
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        self.name = name
        self.image = pygame.transform.scale(image, (int(width * .04), int(height * .06)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        
    def draw_unit(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            width = root.winfo_screenwidth()
            height = root.winfo_screenheight()

            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                print('clicked on ' + str(self.name))
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
    

class Back_Button:
    # This class can be used to easily create a "back button." By default, the button will take the appearance of a
    # black arrow, and will appear on the lower-left corner of the screen. If you want to change the default behavior,
    # specify the necessary parameters when creating the button. Note that x and y must be specified together to change the position.
    def __init__(self, image=None, x=None, y=None, transform_width=.04, transform_height=.04):
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        self.clicked = False

        if image is not None:
            self.image = pygame.transform.scale(image, (int(width * transform_width), int(height * transform_height)))
        
        else:
            back_image = pygame.image.load(r'Images/back_arrow.png').convert_alpha()
            self.image = pygame.transform.scale(back_image, (int(width * transform_width), int(height * transform_height)))
        
        self.rect = self.image.get_rect()

        if x is not None and y is not None:
            self.rect.topleft = (x, y)
        
        else:
            x = width * 0.05
            y = height * 0.9
            self.rect.topleft = (x, y)
    
    def draw_back_button(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            width = root.winfo_screenwidth()
            height = root.winfo_screenheight()

            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action


class Custom_Button:
    # This class can be used to generate a button that *optionally* displays an image when hovered over it.
    # If the optional argument is left empty, no image will generate. Otherwise, it will use a provided image.
    # Images will display to the right of the button. The transform scaling values can also be specified.
    def __init__(self, x, y, image, optional_hover_image=None, transform_width=.04, transform_height=.04):
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        self.image = pygame.transform.scale(image, (int(width * transform_width), int(height * transform_height)))
        self.optional_hover_image = optional_hover_image
        self.confirmed_hover_image = None
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    def draw_custom_button(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            width = root.winfo_screenwidth()
            height = root.winfo_screenheight()

            if self.optional_hover_image is not None:
                self.confirmed_hover_image = pygame.transform.scale(self.optional_hover_image, (int(width * .04), int(height * .06)))
                surface.blit(self.confirmed_hover_image, (self.rect.x * 1.35, self.rect.y))

            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
