from .configs.properties import Properties
from .HTMLGetter import HTMLGetter

import logging
import os.path

class FileAnalyzer(object):
    def __init__(self, path):
        self.path = path
        self.content = ''
        
    def read_content(self):
        f = open(self.path, 'r', encoding="utf8")
        self.content = f.read()
        f.close()

class Info(FileAnalyzer):
    def __init__(self):
        self._info_list = []
        super(Info, self).__init__(\
            os.path.dirname(__file__) + '/../info.txt')
        self._analyze()

    def _analyze(self):
        logging.info('Read all contents in info.txt file')
        self.read_content()
        self._info_list = self.content.split('\n\n')

    def get_title_window(self):
        logging.info('Get title window from file')
        return self._info_list[1]

    def get_tag_to_get(self):
        lst = self._info_list[2].split(',')
        logging.info('Get the main tag from file')
        return {
            Properties.tag_to_get['tag_name']: lst[0].strip(),
            Properties.tag_to_get['att_name']: lst[1].strip(),
            Properties.tag_to_get['att_value']: lst[2].strip()
            }

    def get_tags_to_delete(self):
        tags_list = self._info_list[3].splitlines()
        tags_to_delete = []
        logging.info('Get the tags that will need removing')
        for tag in tags_list:
            item = tag.split(',')
            dic = {
                Properties.tag_to_get['tag_name']: item[0].strip(),
                Properties.tag_to_get['att_name']: item[1].strip(),
                Properties.tag_to_get['att_value']: item[2].strip()
                }
            tags_to_delete.append(dic)

        return tags_to_delete

    def get_urls(self):
        html = self._info_list[4]
        logging.info('Get list of urls')
        return HTMLGetter.get_all_hrefs(html)
