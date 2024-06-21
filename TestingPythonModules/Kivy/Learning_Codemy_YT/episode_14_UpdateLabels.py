from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.core.window import Window
#from kivy.uix.floatlayout import FloatLayout

Builder.load_file("design_14.kv")

class MyLayout(Widget):
    def ButtonPress(self):
        name = self.ids.name_input.text

        # updating the label text
        self.ids.name_label.text = name
        self.ids.name_input.text = ""

class episode_14(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    episode_14().run()
