> Disclaimer: This project is intended to study the Scrapy Spider Framework and the MongoDB database, it cannot be used for commercial or other personal intentions. If used improperly, it will be the individuals bear.

* This is a python scrapy project for crawling [Physical Review Journal sites](https://journals.aps.org).
* This project can crawl up to 5 millon papers a day, depending on your bandwith.
* The crawler requests 18 threads at a time. You can request more threads and crawl a larger amount of paper per day. For the specific configuration see [pre-boot configuration](https://github.com/xiongzhp/paper_spider/blob/master/paperSpider/settings.py)


## Environment, Architecture

Language: Python2.7

Environment: MacOS, 8G RAM

Database: MongoDB

* Mainly uses python scrapy spider framework.
* Join to the Spider randomly by extracted from the Cookie pool and UA pool.
* Start_requests start five Request based on paperSpider classification, and crawl the five categories at the same time.
* Support paging crawl data, and join to the queue.

## Instructions for use

### Pre-boot configuration

* Install MongoDB and start without configuration
* Install Scrapy
* Install Python dependent modules：pymongo, json, requests
* Modify the configuration by needed, such as the interval time, the number of threads, etc.

### Start up

* cd paper_spider
* python quickstart.py

### More configurations
* The default configurations only crawl "highlights" papers from journals, Physical Review A B D, you can include more journals in [paperspdier_type.py](https://github.com/xiongzhp/paper_spider/blob/master/paperSpider/paperspider_type.py).
