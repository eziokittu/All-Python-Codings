from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.core.window import Window

import re

#from kivy.uix.image import Image

# set the app size
Window.size = (300, 500)
# Window.borderless = True
Window.set_title("Mobile App 1")

# Designate the kv file
Builder.load_file("design1.kv")

class MyLayout(Widget):
    pass
    
class code1(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    code1().run()
