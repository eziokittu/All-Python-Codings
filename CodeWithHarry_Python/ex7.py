# I failed to do it so I copied it.

#Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log - Every 40 min
# Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
# Physical activity - physical.mp3 every - 45 min - ExDone - log
# Rules
# Pygame module to play audio

from pygame import mixer
from datetime import datetime
from time import time

dir = "D:/Coding Stuff, Editing/Visual Studio Python Codings/CodeWithHarry_Python/assets/"

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if stopper in input_of_user:
            mixer.music.stop()
            break

def log_now(msg):
    with open(dir + "mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

def Description(watersecs, exsecs, eyessecs):
    print("This is a time schedule.".center(string_adjust_length,"-"))
    print("Every 'x' seconds a music plays to complete the task.")
    print("The tasks and time schedules are as follows :")
    print(f"Drink water - {watersecs} seconds , give rest to your eyes - {eyessecs} seconds , do some exercise - {exsecs} seconds")
    print("Stop the music by writing '' as INPUT respectively as per task.")
    print("Time Starts Now".center(string_adjust_length,"-"))

if __name__ == '__main__':
    # musiconloop("water.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 6#40*60
    exsecs = 10#30*60
    eyessecs = 15#45*60
    stopper_water = "water"
    stopper_exercise = "exer"
    stopper_eyes = "eyes"

    string_adjust_length = 100

    Description(watersecs, exsecs, eyessecs)

    while True:
        if time() - init_water > watersecs:
            print(f"Water Drinking time. Enter '{stopper_water}' to stop the alarm.".rjust(string_adjust_length," "))
            musiconloop(dir + 'ex7_water.mp3', stopper_water)
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes > eyessecs:
            print(f"Eye exercise time. Enter '{stopper_eyes}' to stop the alarm.".rjust(string_adjust_length," "))
            musiconloop(dir + "ex7_eyes.mp3", stopper_eyes)
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() - init_exercise > exsecs:
            print(f"Physical Activity Time. Enter '{stopper_exercise}' to stop the alarm.".rjust(string_adjust_length," "))
            musiconloop(dir + 'ex7_physical.mp3', stopper_exercise)
            init_exercise = time()
            log_now("Physical Activity done at")