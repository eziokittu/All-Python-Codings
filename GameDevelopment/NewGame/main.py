import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)

# Create a sprite class
class Sprite:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))  # Fill the sprite with red color
        self.rect = self.image.get_rect()

    def update(self, delta_time):
        # Check if the left arrow key is pressed
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.x -= self.speed * delta_time
        # Check if the right arrow key is pressed
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.x += self.speed * delta_time
        # Check if the up arrow key is pressed
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.y -= self.speed * delta_time
        # Check if the down arrow key is pressed
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.y += self.speed * delta_time
        
        # Check player bounds
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0
        if self.x + self.rect.width > screen.get_width():
            self.x = screen.get_width() - self.rect.width
        if self.y + self.rect.height > screen.get_height():
            self.y = screen.get_height() - self.rect.height
        
        self.rect.x = self.x
        self.rect.y = self.y

# Create a sprite
sprite = Sprite(200, 150, 300)  # Change the speed to a larger value

# Run the game loop
running = True
current_time = pygame.time.get_ticks()
while running:
    # Calculate delta time
    elapsed_time = pygame.time.get_ticks() - current_time
    current_time = pygame.time.get_ticks()
    delta_time = elapsed_time / 1000.0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
    # Update the sprite
    sprite.update(delta_time)
    # Clear the screen
    screen.fill((255, 255, 255))
    # Draw the sprite
    screen.blit(sprite.image, (sprite.x, sprite.y))
    # Update the display
    pygame.display.update()