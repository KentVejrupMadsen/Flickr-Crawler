import BrowserFrame
import time

frame = None


def main():
    global frame

    frame = BrowserFrame.BrowserFrame()

    Continue = True
    frame.load('')

    while Continue:
        time.sleep(3.5)

        frame.get_image()

        frame.next()

    frame.is_done()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
