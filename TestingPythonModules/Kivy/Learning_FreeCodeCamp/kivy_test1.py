from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# the name used in this class for App has App at the end which is not shown on the app title
# the name in this calss must be same with the .kv file for the .kv file to work, ither than the App part of the name
class kivy_test1App(App):
    pass

class MainWidget(Widget):
    pass

class BoxLayoutExample(BoxLayout):
    pass
    '''
    # same this as done inside fucntion can be done from kv file
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="1")
        b2 = Button(text="2")
        b3 = Button(text="3")
        b4 = Button(text="4")
        self.add_widget((b1))
        self.add_widget((b2))
        self.add_widget((b3))
        self.add_widget((b4))
    '''

kivy_test1App().run()

# 6 Layouts - box, anchor, grid, stack, scrollview, page layout
# float, relative, scatter