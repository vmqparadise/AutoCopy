import urllib.request
import logging
import requests
from .configs.properties import Properties
from bs4 import BeautifulSoup

class HTMLGetter:
    def __init__(self, url):
        self._url = url
        self._html = ''
        self._parser = 'html.parser'
        self._soup = ''

    def open_url(self):
        logging.info('Go to %s' % self._url)
        self._html = urllib.request.urlopen(self._url).read()
        self._soup = BeautifulSoup(self._html, self._parser)
                
    def delete_tags(self, tags):
        for tag in tags:
            tag_name = tag[Properties.tag_to_get['tag_name']]
            att_name = tag[Properties.tag_to_get['att_name']]
            att_value = tag[Properties.tag_to_get['att_value']]

            tag_print = '<%s %s="%s">' % (tag_name, att_name, att_value)
            logging.info('Find tag %s' % tag_print)
            results = self._soup.find_all(tag_name, {att_name: att_value})
            if results is None:
                logging.warning('Cannot find tag %s' % tag_print)
            else:
                for res in results:
                    logging.info('Delete tag %s' % tag_print)
                    res.decompose()
            
    def find(self, tags):
        tag_name = tags[Properties.tag_to_get['tag_name']]
        att_name = tags[Properties.tag_to_get['att_name']]
        att_value = tags[Properties.tag_to_get['att_value']]

        logging.info('Find <%s %s="%s">' % (tag_name, att_name, att_value))
        return self._soup.find_all(tag_name, {att_name: att_value})

    def get_html(self, tag_to_get, tags_to_delete = []):
        self.delete_tags(tags_to_delete)
        result = self.find(tag_to_get)
        
        self._html = str.join(u'\n', map(str, result))
        self._soup = BeautifulSoup(self._html, self._parser)
        logging.info('Get html from the found tag')
        return self._soup.prettify()

    @staticmethod
    def get_all_hrefs(html):
        lst = []
        soup = BeautifulSoup(html, 'html.parser')
        for a in soup.find_all('a', href=True):
            lst.append(a['href'])

        return lst
