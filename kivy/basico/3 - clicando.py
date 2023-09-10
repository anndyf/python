from kivy.app import App
from kivy.uix.button import Button

class MyButton(Button):
    def on_press(self):
        self.text = "Clicado!"

class MyApp(App):
    def build(self):
        return MyButton(text="Clique-me")

if __name__ == '__main__':
    MyApp().run()