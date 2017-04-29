#coding:utf-8
import requests
import logging
from scrapy.spider import CrawlSpider
from scrapy.selector import Selector
from PaperSpider.items import PaperVideoItem
from PaperSpider.paperspider_type import PH_TYPES
from scrapy.http import Request
import re
import json
import random
class Spider(CrawlSpider):
    name = 'paperSpider'
    host = 'https://journals.aps.org/pra/highlights/'
    start_urls = list(set(PH_TYPES))
    logging.getLogger("requests").setLevel(logging.WARNING)  # 将requests的日志级别设成WARNING
    logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='logging.log',
                filemode='w')
    # test = True
    def start_requests(self):
        for ph_type in self.start_urls:
            yield Request(url='https://journals.aps.org/pra/highlights/%s' % ph_type,callback = self.parse_ph_key)
    def parse_ph_key(self,response):
        selector = Selector(response)
        logging.debug('request url:------>' + response.url)
        # logging.info(selector)
        divs = selector.xpath('//div[@class="phimage"]')
        for div in divs:
            viewkey = re.findall('viewkey=(.*?)"',div.extract())
            # logging.debug(viewkey)
            yield Request(url='https://journals.aps.org/pra/highlights/embed/%s' % viewkey[0],callback = self.parse_ph_info)
        url_next = selector.xpath('//a[@class="orangeButton" and text()="Next"]/@href').extract()
        # logging.debug(url_next)
        if url_next:
        # if self.test:
            logging.debug(' next page:---------->' + self.host+url_next[0])
            yield Request(url=self.host+url_next[0],callback=self.parse_ph_key)
            # self.test = False
    def parse_ph_info(self,response):
        phItem = PaperVideoItem()
        selector = Selector(response)
        _ph_info = re.findall('flashvars_.*?=(.*?);\n',selector.extract())
        logging.debug('PH信息的JSON:')
        logging.debug(_ph_info)
        _ph_info_json = json.loads(_ph_info[0])
        title = _ph_info_json.get('title')
        phItem['title'] = title
        journal = _ph_info_json.get('journal')
        phItem['journal'] = journal
        link_url = _ph_info_json.get('link_url')
        phItem['link_url'] = link_url
        DOI = _ph_info_json.get('DOI')
        phItem['DOI'] = DOI
        logging.info(' title:' + title + ' journal:' + journal + ' link_url:' + link_url + ' DOI:' + DOI)
        yield phItem

