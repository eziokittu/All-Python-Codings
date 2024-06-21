from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file("design_5_7.kv")

class MyGridLayout(Widget):
    
    name = ObjectProperty(None)
    age = ObjectProperty(None)
    roll = ObjectProperty(None)

    def pressSubmit(self):
        name = self.name.text
        age = self.age.text
        roll = self.roll.text

        print_text = f"Hello {name}, you are {age} years old, and your roll is {roll}"
        print(print_text)

        # clearing the input boxes
        self.name.text = ""
        self.age.text = ""
        self.roll.text = ""



# class MyApp --> my.kv
# class MyApp1 --> myapp1.kv
# class hello --> hello.kv
class episode_5(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    episode_5().run()
