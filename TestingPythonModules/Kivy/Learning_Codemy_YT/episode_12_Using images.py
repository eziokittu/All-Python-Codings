from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.core.window import Window
#from kivy.uix.image import Image

#Builder.load_file("design_8.kv")
Builder.load_file("design_12.kv")

class MyLayout(Widget):
    pass

class episode_8_9(App):
    def build(self):
        # a way to colour the background outside the design file
        Window.clearcolor = (1,1,0,1)

        return MyLayout()

if __name__ == "__main__":
    episode_8_9().run()
