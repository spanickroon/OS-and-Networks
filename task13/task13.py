from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivymd.theming import ThemeManager


import psutil


Window.size = (700, 500)
Window.title = 'Task13'


class Container(FloatLayout):
    def update_info(self):
        self.spinner.values.extend([
            info.name() + ' ' + str(info.pid) for info in psutil.process_iter()
            ])
        self.spinner.text = self.spinner.values[0]

        self.spinner_info.values.extend([
            str(psutil.virtual_memory().free), str(psutil.cpu_percent())
            ])
        self.spinner_info.text = self.spinner_info.values[0]


class Task13App(App):
    theme_cls = ThemeManager()

    def build(self):
        self.theme_cls.theme_style = 'Light'
        return Container()


Task13App().run()
