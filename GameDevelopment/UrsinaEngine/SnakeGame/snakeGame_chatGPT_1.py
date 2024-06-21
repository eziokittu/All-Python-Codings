from ursina import *
import random

app = Ursina()

# Define the grid size and cell size
GRID_SIZE = 20
CELL_SIZE = 1
GAME_OVER = False
SCORE = 0

class Snake(Entity):
    def __init__(self):
        super().__init__()
        self.body = [self]
        self.direction = Vec3(1, 0, 0)

    def move(self):
        if not GAME_OVER:
            tail_position = self.position + self.direction * CELL_SIZE  # Save the new tail position
            self.position += self.direction * CELL_SIZE

            # Move the body
            for i in range(1, len(self.body)):
                temp = self.body[i].position + self.direction * CELL_SIZE
                self.body[i].position = self.body[i-1].position
                self.body[i-1].position = temp

    def add_tail(self):
        tail = Entity(model='quad', color=color.green, scale=CELL_SIZE)
        tail.position = self.body[-1].position - self.direction * CELL_SIZE
        self.body.append(tail)

    def update(self):
        self.move()

    def input(self, key):
        if not GAME_OVER:
            if key == 'a' or key == 'left arrow':
                self.direction = Vec3(-1, 0, 0)
            elif key == 'd' or key == 'right arrow':
                self.direction = Vec3(1, 0, 0)
            elif key == 'w' or key == 'up arrow':
                self.direction = Vec3(0, 1, 0)
            elif key == 's' or key == 'down arrow':
                self.direction = Vec3(0, -1, 0)

class Food(Entity):
    def __init__(self):
        super().__init__()
        self.model = 'quad'
        self.color = color.red
        self.scale = CELL_SIZE

    def generate_random_position(self):
        x = random.randint(-GRID_SIZE // 2, GRID_SIZE // 2) * CELL_SIZE
        y = random.randint(-GRID_SIZE // 2, GRID_SIZE // 2) * CELL_SIZE
        return Vec3(x, y, 0)

    def update(self):
        # Check if the food is eaten
        if snake.position == self.position:
            snake.add_tail()
            self.position = self.generate_random_position()
            global SCORE
            SCORE += 1

class GameOverWindow(Entity):
    def __init__(self):
        super().__init__()
        self.window = WindowPanel(title='Game Over', content='Score: ' + str(SCORE), z=-1, model='quad', scale=(2, 1))
        self.retry_button = Button(parent=self.window, text='Retry Game', scale=(0.25, 0.1), color=color.gray, on_click=self.retry_game)
        self.window.enabled = False

    def retry_game(self):
        global SCORE, GAME_OVER
        GAME_OVER = False
        SCORE = 0
        self.window.enabled = False
        snake.position = Vec3(0, 0, 0)
        for entity in snake.body[1:]:
            destroy(entity)
        snake.body = [snake]
        snake.direction = Vec3(1, 0, 0)
        food.position = food.generate_random_position()

snake = Snake()
food = Food()
game_over_window = GameOverWindow()

# Create walls around the game area
walls = Entity(model='quad', color=color.white, scale=(GRID_SIZE, CELL_SIZE), y=(GRID_SIZE // 2 + CELL_SIZE / 2))
walls = Entity(model='quad', color=color.white, scale=(GRID_SIZE, CELL_SIZE), y=-(GRID_SIZE // 2 + CELL_SIZE / 2))
walls = Entity(model='quad', color=color.white, scale=(CELL_SIZE, GRID_SIZE), x=(GRID_SIZE // 2 + CELL_SIZE / 2))
walls = Entity(model='quad', color=color.white, scale=(CELL_SIZE, GRID_SIZE), x=-(GRID_SIZE // 2 + CELL_SIZE / 2))

def check_collision():
    global GAME_OVER
    head_position = snake.position
    for segment in snake.body[1:]:
        if segment.position == head_position:
            GAME_OVER = True
    if abs(head_position.x) > (GRID_SIZE // 2) or abs(head_position.y) > (GRID_SIZE // 2):
        GAME_OVER = True

def update():
    if not GAME_OVER:
        snake.move()
        check_collision()
    else:
        game_over_window.window.enabled = True

camera.z -= 30  # Move the camera back
camera.rotation_x = -45  # Tilt the camera for better view

app.run()
