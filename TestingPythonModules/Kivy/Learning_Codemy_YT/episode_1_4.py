import kivy
from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        # call grid layout constructors
        super(MyGridLayout, self).__init__(**kwargs)

        # set the columns
        self.cols = 1
        

        # Creating a second GridLayout
        self.secondGrid = GridLayout(
            row_force_default=True,
            row_default_height = 50,
            col_force_default=True,
            col_default_width = 400
        )
        self.secondGrid.cols = 2

        # Add widgets
        self.secondGrid.add_widget(Label(text="Name: "))
        # Add input box
        self.name = TextInput()
        self.secondGrid.add_widget(self.name)

        # Add widgets
        self.secondGrid.add_widget(Label(text="Age: "))
        # Add input box
        self.age = TextInput()
        self.secondGrid.add_widget(self.age)

        # Add widgets
        self.secondGrid.add_widget(Label(text="Roll: "))
        # Add input box
        self.roll = TextInput()
        self.secondGrid.add_widget(self.roll)

        # Add the new secondGrid to our app
        self.add_widget(self.secondGrid)


        self.submit = Button(text = "Submit",
            font_size = 36,
            size_hint_y = None,
            height = 50,
            size_hint_x = None,
            width = 500)
        self.submit.bind(on_press = self.pressSubmit)
        self.add_widget(self.submit)

    def pressSubmit(self, instance):
        name = self.name.text
        age = self.age.text
        roll = self.roll.text

        print_text = f"Hello {name}, you are {age} years old, and your roll is {roll}"
        self.add_widget(Label(text = print_text))

        self.name.text = ""
        self.age.text = ""
        self.roll.text = ""

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    MyApp().run()