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
Window.set_title("Calculator")

# Designate the kv file
Builder.load_file("design_15.kv")

class MyLayout(Widget):
    def button_function_clear(self):
        ''' function to clear all characters from the textbox and show "0" by default'''
        self.ids.id_textinput.text = "0"

    def button_function_remove(self):
        ''' function to remove the last character from the textbox'''
        value_textinput = self.ids.id_textinput.text
        value_textinput = value_textinput[:-1]
        self.ids.id_textinput.text = value_textinput

    def button_function_posneg(self):
        ''' makes the text box positive or negative'''
        value_textinput = self.ids.id_textinput.text
        if "-" in value_textinput:
            self.ids.id_textinput.text = value_textinput.replace("-", "+")
        elif "+" in value_textinput:
            self.ids.id_textinput.text = value_textinput.replace("+", "-")

    def button_function_math(self, sign):
        ''' on button press functions for addition, subtraction, multiplication, division'''
        value_textinput = self.ids.id_textinput.text
        self.ids.id_textinput.text = f"{value_textinput}{sign}"

    def button_function_equals(self):
        '''on "equals to" button press'''
        value_textinput = self.ids.id_textinput.text

        # Addition
        if "+" in value_textinput:
            num_list = value_textinput.split("+")
            ans = 0.0
            for num in num_list:
                ans += float(num)
            self.ids.id_textinput.text = str(ans)

    def button_press_dot(self):
        '''adds a decimal point to the textbox'''
        value_textinput = self.ids.id_textinput.text 
        numbers = re.split(r"", value_textvalue)
        if "." not in value_textinput:
            self.ids.id_textinput.text = f"{value_textinput}."

    def button_press_numbers(self, digit):
        '''adds the digit from 0 to 9 passed as parameter to the function when pressed the buttons'''
        value_textinput = self.ids.id_textinput.text 
        if value_textinput == "0":
            self.ids.id_textinput.text = ""
            self.ids.id_textinput.text = f"{digit}"
        else:
            self.ids.id_textinput.text = f"{value_textinput}{digit}"
class episode_8_9(App):
    def build(self):
        # a way to colour the background outside the design file
        # Window.clearcolor = (1,1,0,1)

        return MyLayout()

if __name__ == "__main__":
    episode_8_9().run()
