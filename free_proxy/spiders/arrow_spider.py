import scrapy
from scrapy.http.request import Request
import re
import logging
import json

logger = logging.basicConfig(filename="./logs/arrow_log.txt",level=logging.INFO)







class ProxySpider(scrapy.Spider):
    name = "arrow"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    }


    #Read free proxy from free.json
    filename =  './proxy_pool/original.json'

    if filename:
        with open(filename, 'r') as f:
            datastore = json.load(f)
    proxys = []
    for data in datastore:
        proxys.append(data['ip']+':'+data['port'])

    def start_requests(self):
        # logging.info("Date: " + self.current_date)
        for proxy in self.proxys:
            request = Request(url= "https://www.arrow.com/", headers=self.headers, errback=self.remove_invalid(proxy), dont_filter=True)
        
            # request.meta['proxy'] = proxy
            yield request
        output = open('./proxy_pool/valid_proxy.txt', 'w')
        tmp = []
        for item in self.proxys:
            output.write("%s\n" % item)


    # def parse(self, response):
    def remove_invalid(self, proxy):
        self.proxys.remove(proxy)
       

        






# fetch('https://free-proxy-list.net/')
# view(response)
# response.css('table.table-striped.table-bordered.dataTable').extract()
# response.css('table.table-striped.table-bordered').extract()
# response.css('table.table-striped.table-bordered').css('tr').extract()[0]
# response.css('table.table-striped.table-bordered').css('tr')[1].css('td')




        





