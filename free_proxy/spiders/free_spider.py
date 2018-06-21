import scrapy
from scrapy.http.request import Request
import re
import logging


# OUTPUT_PATH = '../proxy_pool/free.json'


logger = logging.basicConfig(filename="./logs/free_spider_log.txt",level=logging.INFO)

class ProxySpider(scrapy.Spider):
    name = "free"

    custom_settings = {
        'ITEM_PIPELINES': {
            # 'free_proxy.pipelines.JsonWriterPipeline': 300,
        }
    }

    #ITEM_PIPELINES = {
#    'free_proxy.pipelines.FreeProxyPipeline': 300,
#}

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    }





    # proxy = '185.93.3.123:8080'
    def start_requests(self):
        # logging.info("Date: " + self.current_date)
        request = Request(url= "https://free-proxy-list.net/", callback=self.parse, headers=self.headers)
        
        # request.meta['proxy'] = self.proxy
        yield request

    def parse(self, response):
        response.css('table.table-striped.table-bordered').css('tr')[1].css('td::text').extract()
        rows = response.css('table.table-striped.table-bordered').css('tr')
        for i in range(1, len(rows) - 1):
            item = rows[i].css('td::text').extract()
            if item[6] == 'yes':
                ip = item[0]
                port = item[1]
                yield {
                    'ip': ip,
                    'port': port
    }
        






# fetch('https://free-proxy-list.net/')
# view(response)
# response.css('table.table-striped.table-bordered.dataTable').extract()
# response.css('table.table-striped.table-bordered').extract()
# response.css('table.table-striped.table-bordered').css('tr').extract()[0]
# response.css('table.table-striped.table-bordered').css('tr')[1].css('td')




        





