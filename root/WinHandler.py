import pyautogui
from pyautogui import _window_win as WindowWin
import time
import logging

from .configs.properties import Properties

class WinHandler:
    def __init__(self):
        self._title = ''
        self._window = ''

    def _open_window(self):
        logging.info('Find the window title')
        self._window = WindowWin.getWindow(self._title)
        if not self._window:
            self._find_window_title_again()

        logging.info('Switch to window name %s' % self._title)
        self._window.set_foreground()
        logging.info('Set this window to maximize')
        self._window.maximize()
        time.sleep(Properties.waiting_time)

    def _find_window_title_again(self):
        error_msg = "There's no windows named '%s'" % self._title
        print(error_msg)
        print('You have 15 seconds to open the window')
        logging.warning("No windows named '%s'" % self._title)
        logging.warning('Wait %d second to find again'\
                        % Properties.waiting_time*7)
        time.sleep(Properties.waiting_time * 7)
        logging.info('Find the window tittle again')
        self._window = WindowWin.getWindow(self._title)
        if not self._window:
            raise Exception(error_msg)
        print('Found the window')

    def paste_into_doc(self, title):
        self._title = title
        self._open_window()

        logging.info("Paste clipboard's contents into active window")
        time.sleep(Properties.waiting_time)
        pyautogui.hotkey('ctrl', 'v')
        
        logging.info("Wait %d seconds" % Properties.waiting_time)
        time.sleep(Properties.waiting_time)

    def paste_into_word(self, title):
        self._title = title
        self._open_window()

        logging.info("Paste clipboard's contents into active window")
        time.sleep(Properties.waiting_time)
        for item in ['alt', 'h', 'v', 'm']:
            pyautogui.press(item)
        
        logging.info("Wait %d seconds" % Properties.waiting_time)
        time.sleep(Properties.waiting_time)

    def save_doc(self):
        logging.info("Save document")
        pyautogui.hotkey('ctrl', 's')
        logging.info('Wait %d seconds' % Properties.waiting_time)
        time.sleep(Properties.waiting_time)
