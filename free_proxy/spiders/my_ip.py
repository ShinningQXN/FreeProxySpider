# import scrapy
# from scrapy.http.request import Request
# import re
# import logging
# import json

# logger = logging.basicConfig(filename="my_ip_log.txt",level=logging.INFO)





# # USE_PROXY = True

# class ProxySpider(scrapy.Spider):

#     name = "my_ip"
# #     # headers = {
# #     #         "Host": "https://octopart.com/",
# #     #         "Connection": "keep-alive",
# #     #         "Cache-Control": "max-age=0",
# #     #         "Upgrade-Insecure-Requests": "1",
# #     #         "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
# #     #         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
# #     #         "DNT": "1",
# #     #         "Accept-Encoding": "gzip, deflate, sdch",
# #     #         "Accept-Language":"en-US,en;q=0.8",
# #     #         "referer": "https://octopart.com/"
# #     #     }
#     headers = {
#         "Content-Type": "application/x-www-form-urlencoded",
#         "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
#     }


# #     #Read free proxy from free.json
#     path = '../proxy_pool/'
#     filename = path + 'free.json'

#     if filename:
#         with open(filename, 'r') as f:
#             datastore = json.load(f)
#     proxys = []
#     for data in datastore:
#         proxys.append(data['ip']+':'+data['port'])
#     print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#     print (proxys)

# #     def start_requests(self):
# #         # logging.info("Date: " + self.current_date)

# #         for proxy in self.proxys:
# #             print ("test1:")
# #             print(proxy)
# #             request = Request(url= "http://checkip.dyndns.org/", headers=self.headers, callback=self.parse)
        
# #             request.meta['proxy'] = proxy
# #             yield request 

# #     # def parse(self, response):
# #     def parse(self, response):
# #         pub_ip = response.xpath('//body/text()').re('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')[0]
# #         print ("My public IP is: " + pub_ip)





#     # def start_requests(self):
#     #     # print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#     #     request =  Request('http://quotes.toscrape.com/page/1/', callback=self.check_ip, headers = self.headers)
#     #     request.meta["proxy"] = self.proxys[0]
#     #     print ("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#     #     print(self.proxys[0])
#     #     yield request
#     #     # yield other requests from start_urls here if needed

#     # def check_ip(self, response):
#     #     print ("~qqqqqqqqqqqqqqqqqqqqqqq~")

#     #     pub_ip = response.xpath('//body/text()').re('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')[0]
#     #     # print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#     #     print ("My public IP is: " + pub_ip)

#     def start_requests(self):
#         urls = [
#             'http://quotes.toscrape.com/page/1/',
#             'http://quotes.toscrape.com/page/2/',
#         ]
#         for url in urls:
#             request =  Request('http://quotes.toscrape.com/page/1/', callback=self.parse, headers = self.headers)
#             request.meta["proxy"] = self.proxys[0]
#             yield request

#     def parse(self, response):
#         page = response.url.split("/")[-2]
#         filename = 'quotes-%s.html' % page
#         with open(filename, 'wb') as f:
#             f.write(response.body)
#         self.log('Saved file %s' % filename)
# # fetch('https://free-proxy-list.net/')
# # view(response)
# # response.css('table.table-striped.table-bordered.dataTable').extract()
# # response.css('table.table-striped.table-bordered').extract()
# # response.css('table.table-striped.table-bordered').css('tr').extract()[0]
# # response.css('table.table-striped.table-bordered').css('tr')[1].css('td')


# # http://icanhazip.com/

        





