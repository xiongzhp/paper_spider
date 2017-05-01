# -*- coding: utf-8 -*-

# Scrapy settings for paperspider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'phyrevSpider'

SPIDER_MODULES = ['paperSpider.spiders']
NEWSPIDER_MODULE = 'paperSpider.spiders'

DOWNLOAD_DELAY = 1  # 间隔时间
# LOG_LEVEL = 'INFO'  # 日志级别
CONCURRENT_REQUESTS = 18  # 默认为18
# CONCURRENT_ITEMS = 1
# CONCURRENT_REQUESTS_PER_IP = 1
REDIRECT_ENABLED = False
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'paperspider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

DOWNLOADER_MIDDLEWARES = {
    "paperSpider.middlewares.UserAgentMiddleware": 401,
    "paperSpider.middlewares.CookiesMiddleware": 402,
}
ITEM_PIPELINES = {
    "paperSpider.pipelines.PaperhubMongoDBPipeline": 403,
}
