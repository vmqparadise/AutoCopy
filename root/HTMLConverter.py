from .HTMLGetter import HTMLGetter
from .configs.properties import Properties

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import logging
import time
import pyperclip
import os

class HTMLConverter:
    def __init__(self, driver):
        self.driver = driver
        self._tags_to_delete = []
        self._tag_to_get = dict()

    def set_tags_to_delete(self, tags):
        self._tags_to_delete = tags

    def set_tag_to_get(self, tags):
        self._tag_to_get = tags

    def get_html(self, url):
        getter = HTMLGetter(url)
        getter.open_url()
        html = getter.get_html(\
            self._tag_to_get, self._tags_to_delete)
        return html

    def get_html_into_web_converter(self, contents):
        logging.info('Copy contents to clipboard')
        pyperclip.copy(contents)

        url = Properties.html_cleaner['url']
        logging.info('Browse to %s' % url)
        self.driver.get(url)
        actions = ActionChains(self.driver)
        
        self.paste_html(actions)
        self.copy_word()

    def paste_html(self, actions):
        time.sleep(2)
        html_agree = self.driver.find_element_by_xpath(\
            "//button[text()='AGREE']")      
        html_textbox = self.driver.find_element_by_class_name(\
            Properties.html_cleaner['html_txtbox_class_name'])
        logging.info(html_textbox)
        clear_button = self.driver.find_element_by_class_name(\
            Properties.html_cleaner['clear_button_class_name'])
        logging.info(clear_button)

        self.driver.implicitly_wait(5)
        
        #logging.info('Click on agree button')
        actions.click(html_agree)
        self.driver.implicitly_wait(2)

        logging.info('Click Fresh Page button')
        actions.click(clear_button)

        logging.info('Click on html textbox')
        actions.click(html_textbox)
        self.driver.implicitly_wait(3)

        logging.info('Select all temporary text by sending Ctrl + A')
        #html_textbox.send_keys(Keys.CONTROL, 'a')
        #actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        #time.sleep(1)

        logging.info("Paste clipboard's contents into html textbox")
        #html_textbox.send_keys(Keys.CONTROL, 'v')
        actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

        logging.info('Wait %d seconds' % Properties.waiting_time)
        time.sleep(Properties.waiting_time)

    def copy_word(self):
        edit_menu = self.driver.find_element_by_id(\
            Properties.html_cleaner['edit_id'])
        logging.info('Click edit menu')
        edit_menu.click()
        
        select_all = self.driver.find_element_by_id(\
            Properties.html_cleaner['edit_select_all_id'])
        logging.info('Click Select all')
        select_all.click()

        logging.info('Click edit menu again')
        edit_menu.click()
        copy = self.driver.find_element_by_id(\
            Properties.html_cleaner['edit_copy_id'])
        logging.info('Click Copy')
        copy.click()

        logging.info('Wait %d seconds' % Properties.waiting_time)
        time.sleep(Properties.waiting_time)
