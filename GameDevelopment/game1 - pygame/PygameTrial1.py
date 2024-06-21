import pygame
import random
import math

clock = pygame.time.Clock()
fps = 10

# the directory to to my assets folder
dir = "/GameDevelopment/game1 - pygame/assets/PygameTrial/"

# Initialize a pygame
pygame.init()

# Creating the screen
gameWindowWidth = 960
gameWindowHeight = 720
#screen = pygame.display.set_mode((gameWindowWidth,gameWindowHeight))

# Title and Icon
pygame.display.set_caption("Pygame Trial Game")
gameIcon = pygame.image.load(dir + "gamepad.png")
pygame.display.set_icon(gameIcon)





# Game Background
# gameBackground = pygame.image.load(dir + "background.png")

screen = pygame.display.set_mode((gameWindowWidth,gameWindowHeight), pygame.RESIZABLE)




class Button:
    """Create a button, then blit the surface in the while loop"""
 
    def __init__(self, text,  pos, font, bg="black", feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback
        self.change_text(text, bg)
 
    def change_text(self, text, bg="black"):
        """Change the text whe you click"""
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
 
    def show(self):
        screen.blit(self.surface, (self.x, self.y))
 
    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change_text(self.feedback, bg="red")




# some functions
def Draw_All():
    width = 60
    height = 60
    offsetX = width+10
    offsetY = height+10

    for i in range(8):
        for j in range(8):
            pygame.draw.rect(screen, pygame.Color(random.randrange(255),random.randrange(255),random.randrange(255)),
                pygame.Rect(offsetX*i, offsetY*j, width, height))
    pygame.display.flip()




button1 = Button(
    "Click here",
    (100, 100),
    font=30,
    bg="navy",
    feedback="Working")


# Game Loop
i_dont_want_to_quit_the_game = True
while i_dont_want_to_quit_the_game:
    clock.tick(fps)
    # the screen's colour will be changed - layer1
    #screen.fill((0,110,240)) # colours in RGB
    #screen.blit(gameBackground, (0,0))

    #Draw_All()
    button1.show()


    # Checking for events 
    for event in pygame.event.get():
        # Checking if we are quitting the Game
        if event.type == pygame.QUIT:
            i_dont_want_to_quit_the_game = False
        button1.click(event)

    # Updates each frame of the Pygame
    pygame.display.update() # this must be the last line