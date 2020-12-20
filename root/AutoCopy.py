from .HTMLConverter import HTMLConverter
from .WinHandler import WinHandler
from .FileAnalyzer import Info
from .configs.properties import Properties

import logging
import os.path
import time
from selenium import webdriver

class AutoCopy:
    def __init__(self):
        self.driver = ''
        
        info = Info()        
        self._title_window = info.get_title_window()
        self._tag_to_get = info.get_tag_to_get()
        self._tags_to_delete = info.get_tags_to_delete()
        self._urls = info.get_urls()

    def _start(self, converter, contents):
        converter.get_html_into_web_converter(contents)
        
        win = WinHandler()
        win.paste_into_word(self._title_window)
        win.save_doc()
        #win.paste_into_doc(self._title_window)

    def _get_content_from_url(self, converter, url):
        converter.set_tags_to_delete(self._tags_to_delete)
        converter.set_tag_to_get(self._tag_to_get)
        return converter.get_html(url)
    
    def run(self):
        length = len(self._urls)
        number_for_one_loop = 20
        i = 0

        while i < length:
            try:
                logging.info('Open Chrome browser')
                self.driver = webdriver.Chrome()
                self.driver.maximize_window()

                converter = HTMLConverter(self.driver)
                str_for_one_loop = ''
                
                for index in range(0, number_for_one_loop):
                    logging.info('---------------------------------------------')
                    logging.info('BEFORE length = %s' % length)
                    logging.info('BEFORE i = %s' % i)
                    logging.info('BEFORE index = %s' % index)
                    if i >= length:
                        break
                    logging.info('GET %s' % self._urls[i])
                    str_for_one_loop += self._get_content_from_url(\
                        converter, self._urls[i])
                    i += 1
                    
                    logging.info('AFTER i = %s' % i)
                    logging.info('AFTER index = %s' % index)
                        
                self._start(converter, str_for_one_loop)
                logging.info('Wait %d seconds' % Properties.waiting_time)
                time.sleep(Properties.waiting_time)
            except Exception as ex:
                logging.error(ex)
                close = input("We have errors. Do you want to quit? (y/n): ")
                if close.lower() == 'y':
                    break
            finally:
                logging.info('Quit the browser')      
                self.driver.quit()
                logging.info('---------------------------------------------')

