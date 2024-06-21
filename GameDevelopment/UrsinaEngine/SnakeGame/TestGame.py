from ursina import *
import random

app = Ursina()

def generate_secret_number():
    return random.randint(0, 100)

def check_guess():
    global secret_number, lives
    guess = int(input_field.text)

    if guess == secret_number:
        show_text("Congratulations, you win!")
        invoke(restart_game, delay=2)
    elif guess < secret_number:
        show_text("Try Higher!")
        lives -= 1
    else:
        show_text("Try Lower!")
        lives -= 1

    if lives <= 0:
        show_text(f"You Lose! The secret number was {secret_number}.")
        invoke(restart_game, delay=2)

def show_text(text):
    text_element = Text(text=text, origin=(0, 0), scale=2, background=True, lifetime=2)
    def remove_text():
        destroy(text_element)
    invoke(remove_text, delay=2)

def restart_game():
    global secret_number, lives
    secret_number = generate_secret_number()
    lives = 5
    input_field.enabled = True
    input_field.text = ""
    button_retry.enabled = False
    button_quit.enabled = False

def retry_game():
    button_retry.enabled = False
    button_quit.enabled = False
    input_field.enabled = True
    input_field.text = ""

def quit_game():
    application.quit()

secret_number = generate_secret_number()
lives = 5

window.title = "Find the Number Game"
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False

input_field = InputField(placeholder="Enter your guess", scale=(0.15, 0.05), position=(0, 0.1))
button_check = Button(text="Check", color=color.azure, scale=(0.1, 0.05), position=(0.3, 0), on_click=check_guess)
button_retry = Button(text="Retry", color=color.azure, scale=(0.1, 0.05), position=(0.3, -0.1), enabled=False, on_click=retry_game)
button_quit = Button(text="Quit", color=color.azure, scale=(0.1, 0.05), position=(0.3, -0.2), on_click=quit_game)

app.run()
