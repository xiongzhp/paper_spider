#coding:utf-8
import requests
import logging
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from paperSpider.items import PaperItem
from paperSpider.paperspider_type import URL
from scrapy.http import Request
import re
import json
import random
import csv

class Spider(CrawlSpider):
    name = 'phyrevSpider'
    host = 'https://journals.aps.org'
    start_urls = list(set(URL))
    # logging.getLogger("requests").setLevel(logging.WARNING)  # 将requests的日志级别设成WARNING
    # logging.basicConfig(level=logging.DEBUG,
    #             format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    #             datefmt='%a, %d %b %Y %H:%M:%S',
    #             filename='logging.log',
    #             filemode='w')


    def requestsLog(name, log_file, level=logging.DEBUG):

        handler = logging.FileHandler(log_file)        
        # formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        # handler.setFormatter

        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)

        return logger

    def getResultFromLogger(name, log_file, level=logging.INFO):

        handler = logging.FileHandler(log_file)        
        # formatter = logging.Formatter('%(asctime)s,%(levelname)s,%(message)s')
        # handler.setFormatter(formatter)

        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)

        return logger

    # Requests logger
    requestsLog = requestsLog('requestslog', 'requests.log')

    # Results logger
    results = getResultFromLogger('results', 'PhyRev.txt')

    # with open('PhyRev.csv','wb') as f1:
    #     w= csv.writer(f1, dialect='excel') 
    #     w.writerow(['DOI', 'title', 'journal', 'link_url'])

        # test = True
    def start_requests(self):
        for start_url in self.start_urls:

            yield Request(url='https://journals.aps.org/%s' % start_url,callback = self.parse_pr_key)
    
    def parse_pr_key(self,response):
        selector = Selector(response)
        self.requestsLog.debug('request url:------>' + response.url)
        # logging.info(selector)
        divs = selector.xpath('//h5[@class="title"]') # 提取文章列表
        for div in divs:
            prItem = PaperItem()
            title = re.findall('<a.*?>(.*?)</a>',div.extract())[0]
            prItem['title'] = title
            short_url = re.findall('href="(.*?)"',div.extract())[0]
            journal = short_url.split('/')[1]
            prItem['journal'] = journal
            doi = re.findall('abstract/(.*)',short_url)[0]
            DOI = 'https://doi.org/' + doi
            # logging.debug(DOI)
            prItem['DOI'] = DOI
            link_url = self.host+short_url
            prItem['link_url'] = link_url
            self.results.info(DOI+'\t'+title+'\t'+link_url+'\t'+journal)
            # logging.info(' title:' + title + ' journal:' + journal + ' link_url:' + link_url + ' DOI:' + DOI)
            # w.writerow([DOI, title, journal, link_url])
            yield prItem

        url_next = selector.xpath(u'//a[text()="»"]/@href').extract()
        # logging.debug(url_next)
        if url_next:
        # if self.test:
            self.requestsLog.debug('next page:------>' + self.host+url_next[0])
            yield Request(url=self.host+url_next[0],callback=self.parse_pr_key)
            # self.test = False
