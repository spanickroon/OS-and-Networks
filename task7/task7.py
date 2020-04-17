from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivymd.theming import ThemeManager
from kivy.animation import Animation

Window.size = (700, 500)
Window.title = 'Task7'


class Container(FloatLayout):
    def add_item(self):
        if self.text_input.text.strip() != '':
            text = self.text_input.text.strip()
            self.left_spinner.values.append(text)
            self.left_spinner.text = text
            self.text_input.text = ''

    def move_to_right(self):
        text = self.left_spinner.text
        if text != '':
            try:
                self.right_spinner.values.index(text)
            except ValueError:
                self.right_spinner.values.append(text)
                self.right_spinner.text = text

    def delete_selected(self):
        text = self.left_spinner.text
        list_values = self.left_spinner.values
        try:
            list_values.remove(text)
            self.left_spinner.text = list_values[0]
        except (ValueError, IndexError):
            self.left_spinner.text = ''

    def clear_all(self):
        self.left_spinner.values.clear()
        self.right_spinner.values.clear()
        self.left_spinner.text = ''
        self.right_spinner.text = ''


class Task7App(App):
    theme_cls = ThemeManager()

    def build(self):
        self.theme_cls.theme_style = 'Light'

        return Container()


Task7App().run()
