import pygame


class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()
        # print(pos)

        if self.rect.collidepoint(pos):
            menu_boat_image = pygame.image.load(r'Images/Menu_Boat.png').convert_alpha()
            menu_boat_image = pygame.transform.scale(menu_boat_image, (150, 75))
            surface.blit(menu_boat_image, (self.rect.x * .8, self.rect.y))
            # print("hover")
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                print('clicked')
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
