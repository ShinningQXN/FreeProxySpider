import scrapy
from scrapy.http.request import Request
import re
import logging
import urllib.request as urllib2

# OUTPUT_PATH = '../proxy_pool/free.json'


# logger = logging.basicConfig(filename="./logs/free_spider_log.txt",level=logging.INFO)

class ProxySpider(scrapy.Spider):
    name = "free"

    custom_settings = {
        # 'ITEM_PIPELINES': {
        #     'free_proxy.pipelines.JsonWriterPipeline': 300,
        # },

        'FEED_URI': 'ips.json',
    }

    #ITEM_PIPELINES = {
#    'free_proxy.pipelines.FreeProxyPipeline': 300,
#}

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    }
    headers_arrow = {
        "Host": "www.arrow.com",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "DNT": "1",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language":"en-US,en;q=0.8",
        "referer": "https://www.arrow.com"
    }
    headers_octo = {
        "Host": "https://octopart.com/electronic-parts/integrated-circuits-ics",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "DNT": "1",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language":"en-US,en;q=0.8",
        "referer": "https://octopart.com/electronic-parts/integrated-circuits-ics"
    }



    proxys = []

    # proxy = '185.93.3.123:8080'
    def start_requests(self):
        # logging.info("Date: " + self.current_date)
        open('./valid.txt', 'w').close()
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
                proxy = ip + ':' + port


                
                request = Request(url= "https://octopart.com/electronic-parts/integrated-circuits-ics", callback=self.parse_valid, headers=self.headers_arrow)
                request.meta['proxy'] = proxy
                request.meta['qxn'] = proxy
                # print ('f###########################################')
                # proxy = urllib2.ProxyHandler({'http': curr_ip})
                # opener = urllib2.build_opener(proxy)
                # opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
                # urllib2.install_opener(opener)
                
                try:
                    yield request                   
                except:
                    continue
                    
                yield {
                    'ip': ip,
                    'port': port
                }
                    # break

    def parse_valid(self, response):
        # print ('f###########################################')
        ip = response.meta['qxn']
        print ("###################################################3")
        print (ip)
        # with open('./valid.txt', 'a+') as f:
        #     f.write(proxy)
        #     f.write("\n")



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




    # def parse(self, response):
    #     response.css('table.table-striped.table-bordered').css('tr')[1].css('td::text').extract()
    #     rows = response.css('table.table-striped.table-bordered').css('tr')
    #     for i in range(1, len(rows) - 1):
    #         item = rows[i].css('td::text').extract()
    #         if item[6] == 'yes':
    #             ip = item[0]
    #             port = item[1]
    #             proxy = ip + ':' + port
                
    #             request = Request(url= "https://www.octopart.com/", callback=self.parse_valid(proxy), headers=self.headers)
    #             request.meta['proxy'] = proxy
    #             yield request
    #             # yield {
    #             #     'ip': ip,
    #             #     'port': port
    #             # }

    # def parse_valid(self, proxy):
        
    #     with open('./proxy_pool/valid.txt', 'a+') as f:
    #         f.write(proxy)
    #         f.write("\n")
    # def parse_2(self, response):
    #     print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    #     print(response.css(".serp-part-card")[0].css(".offerRow").css('.col-seller-inner::text').extract_first())






        






# fetch('https://free-proxy-list.net/')
# view(response)
# response.css('table.table-striped.table-bordered.dataTable').extract()
# response.css('table.table-striped.table-bordered').extract()
# response.css('table.table-striped.table-bordered').css('tr').extract()[0]
# response.css('table.table-striped.table-bordered').css('tr')[1].css('td')

# fetch('https://www.arrow.com/', headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
# fetch('https://octopart.com/', headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})

        





