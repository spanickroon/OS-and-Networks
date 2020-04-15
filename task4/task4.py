import pyxhook


class DoublingNumbers:

    def __init__(self):
        self.hook = pyxhook.HookManager()
        self.hook.KeyDown = self.on_press_key
        self.hook.HookKeyboard()

    def on_press_key(self, event):
        if chr(event.Ascii).isdigit():
            print(chr(event.Ascii))
        return True


def main():
    hk = DoublingNumbers()
    hk.hook.start()


if __name__ == '__main__':
    main()
