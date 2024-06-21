from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests
from selenium import webdriver
driver = webdriver.Chrome('D:\Coding Stuff, Editing\Visual Studio Python Codings\MyProjects\Jarvis AI\chromedriver');
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def talkToMe(audio):
    "speaks audio passed as argument"

    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)

    #  use the system's inbuilt say command instead of mpg123
    #  text_to_speech = gTTS(text=audio, lang='en')
    #  text_to_speech.save('audio.mp3')
    #  os.system('mpg123 audio.mp3')


def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
        #command=input()
        #the above command can be used to take input from the command line

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();

    return command

def assistant(command):
    "if statements for executing commands"

    if 'open reddit' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.reddit.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        driver.execute_script("window.open('https://www.reddit.com');")

        print('Done!')

    elif 'open youtube' in command:
        reg_ex = re.search('open youtube (.*)', command)
        url = 'https://www.youtube.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        driver.execute_script("window.open('https://www.youtube.com');")
        print('Done!')

    elif 'open website' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            driver.execute_script("window.open('"+url+"');")

            print('Done!')
        else:
            pass

    elif 'what\'s up' in command:
        talkToMe('Just doing my thing')

    elif 'joke' in command:
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
        if res.status_code == requests.codes.ok:
            talkToMe(str(res.json()['joke']))
        else:
            talkToMe('oops!I ran out of jokes')

    elif 'scroll down' in command:

        driver.switch_to.window(driver.window_handles[-1]);
        for x in range (3000):
            driver.execute_script("window.scrollBy(0, 1)")

    elif 'scroll up' in command:

        driver.switch_to.window(driver.window_handles[-1]);
        for x in range (3000):
            driver.execute_script("window.scrollBy(0, -1)")

    elif 'google' in command:
        reg_ex = re.search('google (.+)', command)
        if reg_ex:
            # This is done to structure the string  
            # into search url.(This can be ignored) 
            search_string = reg_ex.group(1).replace(' ', '+')  
              
            # Assigning the browser variable with chromedriver of Chrome. 
            # Any other browser and its respective webdriver  
            # like geckodriver for Mozilla Firefox can be used 
              
            for i in range(1): 
                query_string = "https://www.google.com/search?q=" + search_string + "&start=" + str(i)
                matched_elements = driver.execute_script("window.open('"+query_string+"');")

            print('Done!')
        else:
            pass

talkToMe('I am ready for your command')

#loop to continue executing multiple commands
while True:
    assistant(myCommand()) 