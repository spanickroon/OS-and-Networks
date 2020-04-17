from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivymd.theming import ThemeManager
from kivy.animation import Animation
from kivy.config import Config

Config.set('kivy', 'window_icon', 'сovid.ico')

Window.size = (700, 500)
Window.title = 'Task6'
Window.set_system_cursor('hand')
Window.set_icon('covid.ico')


class Container(FloatLayout):
    anim =\
        Animation(
            pos_hint={'center_x': 0, 'y': 0.2}, duration=2) +\
        Animation(
            pos_hint={'center_x': 1, 'y': 0.2}, duration=3)

    def start_moving(self):
        self.start_button.disabled = True
        self.stop_button.disabled = False
        self.anim.repeat = True
        self.anim.start(self.text_label)

    def stop_moving(self):
        self.start_button.disabled = False
        self.stop_button.disabled = True
        self.anim.repeat = False
        self.anim.cancel(self.text_label)


class Task6App(App):
    theme_cls = ThemeManager()

    def build(self):
        self.theme_cls.theme_style = 'Light'
        return Container()


Task6App().run()
