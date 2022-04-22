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
