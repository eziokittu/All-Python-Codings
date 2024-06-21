import datetime
from datetime import date
import pyttsx3

engine = pyttsx3.init('sapi5')

def wishme():
    hour = int(datetime.datetime.now().hour)

if __name__ == "__main__":
    wishme()