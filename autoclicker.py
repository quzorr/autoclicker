import time
import keyboard
import pyautogui

MAX_WORK_TIME = 10 * 3

work = False


def change_work():
    global work
    work = not work


keyboard.add_hotkey('shift', change_work)


def main():
    start_time = time.time()
    count_clicks = 0

    while True:
        difference = time.time() - start_time
        if work and difference < MAX_WORK_TIME:
            pyautogui.click()
            count_clicks += 1
            print(f'(CLICKING) click number: {count_clicks} {" "*2} time: {round(difference, 2)}')

        elif difference < MAX_WORK_TIME:
            print(f'(STOP) time: {round(difference, 2)}')
            time.sleep(0.1)

        else:
            quit()


if __name__ == '__main__':
    main()
