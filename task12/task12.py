from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color

from threading import Thread, Lock
import time


Window.size = (700, 500)
Window.title = 'Task12'


class Container(FloatLayout):
    def fill_red(self):
        Color(1, 0, 0)
        Rectangle(pos=self.pos, size=self.size)

    def fill_green(self):
        Color(0, 1, 0)
        Rectangle(pos=self.pos, size=self.size)

    def fill_blue(self):
        Color(0, 0, 1)
        Rectangle(pos=self.pos, size=self.size)

    def on_touch_down(self, touch):
        with self.canvas:
            th_1 = Thread(target=self.fill_red)
            th_2 = Thread(target=self.fill_green)
            th_3 = Thread(target=self.fill_blue)

            th_1.start()
            th_2.start()
            th_3.start()

        super().on_touch_down(touch)


class Task11App(App):
    def build(self):
        return Container()


Task11App().run()
