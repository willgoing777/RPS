import pygame

pygame.font.init()

# Text button class
class Button:
    # construct a text button, (x,y) indicates the button position
    def __init__(self, name, size,  x, y, color):
        self.color = color
        welcome_font = pygame.font.Font("font.ttf", size)
        self.text = welcome_font.render(name, True, self.color)
        w, h = self.text.get_size()
        self.width = w
        self.height = h
        self.x = x
        self.y = y

    # check if the button is clicked, return True if clikced, otherwise False
    def click(self, X, Y):
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    # draw the button on the given screen
    def draw(self, screen):

        screen.blit(self.text, (self.x, self.y))
