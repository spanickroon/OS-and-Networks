from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivymd.theming import ThemeManager
from kivy.animation import Animation


Window.size = (700, 500)
Window.title = 'Task8'


class Container(FloatLayout):

    def on_touch_down(self, touch):
        x, y = touch.pos
        if x > 140 or y < 450:
            self.moving_image(touch.pos)
        super().on_touch_down(touch)

    def moving_image(self, pos_mouse):
        anim = Animation(pos=pos_mouse)

        if self.spinner.text == 'Image1':
            moving_obj = self.image_1
        elif self.spinner.text == 'Image2':
            moving_obj = self.image_2
        elif self.spinner.text == 'Image3':
            moving_obj = self.image_3
        else:
            moving_obj = self.image_4

        anim.start(moving_obj)


class Task9App(App):
    theme_cls = ThemeManager()

    def build(self):
        self.theme_cls.theme_style = 'Light'
        return Container()


Task9App().run()
