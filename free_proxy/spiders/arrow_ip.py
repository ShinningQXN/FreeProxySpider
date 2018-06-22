import scrapy
from scrapy.http.request import Request
import re
import logging
import urllib.request as urllib2
from scrapy.utils.project import get_project_settings
from pymongo import MongoClient

# logger = logging.basicConfig(filename="./logs/free_spider_log.txt",level=logging.INFO)
class ProxySpider(scrapy.Spider):
    name = "arrow"

    settings=get_project_settings()
    free_list_header = settings.get('FREE_LIST_HEADER')
    arrow_header = settings.get('ARROW_HEADER')
    connection = MongoClient(settings['MONGODB_SERVER'],settings['MONGODB_PORT'])       
    db = connection[settings['MONGODB_DB']]
    ip_collection = db[settings['MONGODB_ARROW_IP_COLLECTION']]
    ip_collection.delete_many({})

    custom_settings = {
        'ITEM_PIPELINES': {
            'free_proxy.pipelines.MongoDB_ARROW_Pipeline': 300,
        },

        # 'FEED_URI': 'ipsarrow.json',
    }
    # headers_proxy = {
    #     'content-type':'application/x-www-form-urlencoded',
    #     'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    # }
    
    # headers_octo = {
    #     'authority': 'octopart.com',
    #     'method': 'GET',
    #     'accept': 'application/json, text/javascript, */*; q=0.01',
    #     'accept-encoding': 'gzip, deflate, br',
    #     'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,la;q=0.6',
    #     'referer': 'https://octopart.com/electronic-parts/integrated-circuits-ics',
    #     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    #     'accept': '*/*',
    #     'dnt': 1
    # }
    

    def start_requests(self):
        open('./ips.json', 'w').close()
        request = Request(url= "https://free-proxy-list.net/", callback=self.parse, headers=self.free_list_header)
        yield request


    def parse(self, response):
        # parse free proxy list's response
        response.css('table.table-striped.table-bordered').css('tr')[1].css('td::text').extract()
        rows = response.css('table.table-striped.table-bordered').css('tr')
        count = 0
        # for each ip in the table
        for i in range(1, len(rows) - 1):
            item = rows[i].css('td::text').extract()
            
            if item[6] == 'yes':
                
                ip = item[0]
                port = item[1]
                proxy = ip + ':' + port

                # filter the proxy, customize the url and header               
                request = Request(url= "https://arrow.com", callback=self.parse_valid, headers=self.arrow_header, dont_filter=True)
                request.meta['proxy'] = proxy
                request.meta['qxn'] = proxy
                try:
                    yield request                   
                except:
                    continue


    def parse_valid(self, response):   
        ip = response.meta['qxn']
        yield {'ip': ip}
        print (ip)




    def errback_httpbin(self, failure):
        # log all failures
        self.logger.error(repr(failure))

        # in case you want to do something special for some errors,
        # you may need the failure's type:
        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.logger.error('HttpError on %s', response.url)

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error('DNSLookupError on %s', request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)








# fetch('https://free-proxy-list.net/')
# view(response)
# response.css('table.table-striped.table-bordered.dataTable').extract()
# response.css('table.table-striped.table-bordered').extract()
# response.css('table.table-striped.table-bordered').css('tr').extract()[0]
# response.css('table.table-striped.table-bordered').css('tr')[1].css('td')

# fetch('https://www.arrow.com/', headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
# fetch('https://octopart.com/', headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})

        





