import scrapy
import requests
from bs4 import BeautifulSoup as soup
import json
from scrapy_splash import SplashRequest

class Bbspidyv8Spider(scrapy.Spider):
    name = 'bbspidyv8'
    # allowed_domains = ['bigbasket.com']

    def start_requests(self):
        fn = open('N:/Python projects saved/Shopolite/bigbasketv3/Bigbasket_product_page.json')
        start_urls = json.load(fn)

        meta={
        'splash': {
                'args': {
                    'html': 1,
                    'wait': 5,
                    'headers': {
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
                    },
                },
            }
        }
        # headers = {
        # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
        # }

        for url in start_urls:
        
            yield SplashRequest(url, callback=self.parse, meta=meta)

        fn.close()
    # start_urls = ['https://www.bigbasket.com/custompage/sysgenpd/?type=pc&slug=foodgrains-oil-masala']

    # header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}



    def parse(self, response):
        try:
            yield {
                'product_name' : response.xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/span/text()').get(),
                'product_title' : response.xpath('//*[@id="title"]/h1/text()').extract_first().strip(),
                'product_brand' : response.xpath('//*[@id="title"]/a/text()').extract_first(),
                'image_link_front' : response.xpath('//*[@id="carousel"]/div[1]/img/@src').get(),
                'image_link_back' : response.xpath('//*[@id="carousel"]/div[2]/img/@src').get(),
                'image_link_nutritional_info' : response.xpath('//*[@id="carousel"]/div[4]/img/@src').get(),
                'image_link_ingredient' : response.xpath('//*[@id="carousel"]/div[3]/img/@src').get(),
                'image_link_fssai' : response.xpath('//*[@id="carousel"]/div[5]/img/@src').get(),
                'product_category_1stlevel' : response.xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/a[2]/text()').get(),
                'product_category_2ndlevel' : response.xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/a[3]/text()').get(),
                'product_category_3rdlevel' : response.xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/a[4]/text()').get(),
                'mrp_on_bigbasket' : response.xpath('//*[@id="40161711"]/tr[1]/td[2]/text()[2]').get(),
                'selling_price_bigbasket' : response.xpath('//*[@id="40161711"]/tr[2]/td[2]/text()[2]').get(),
                'about_product' : response.xpath('//*[@id="about_0"]/div[2]/div/div/text()').get().strip(),
                'product_avg_review' : response.xpath('//*[@id="title"]/div[2]/div/div/text()').get(),
                'product_ratings' : response.xpath('//*[@id="title"]/div[2]/div/span/text()[1]').get().replace('Ratings', '').strip(),
                'product_reviews' : response.xpath('//*[@id="title"]/div[2]/div/span/text()[3]').get().strip().replace(' \n                  \n                  Reviews', '').replace('& ', ''),
                # 'EAN_code' : response.xpath('//*[@id="about_2"]/div[2]/div/div/text()[1]').get().strip()

            }
        except:
            yield {
                'product_name' : response.xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/span/text()').get(),
                'product_title' : response.xpath('//*[@id="title"]/h1/text()').extract_first().strip(),
                'product_brand' : response.xpath('//*[@id="title"]/a/text()').extract_first(),
                'image_link_front' : response.xpath('//*[@id="carousel"]/div[1]/img/@src').get(),
                'image_link_back' : response.xpath('//*[@id="carousel"]/div[2]/img/@src').get(),
                # 'image_link_nutritional_info' : response.xpath('//*[@id="carousel"]/div[4]/img/@src').get(),
                # 'image_link_ingredient' : response.xpath('//*[@id="carousel"]/div[3]/img/@src').get(),
                # 'image_link_fssai' : response.xpath('//*[@id="carousel"]/div[5]/img/@src').get(),
                'product_category_1stlevel' : response.xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/a[2]/text()').get(),
                'product_category_2ndlevel' : response.xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/a[3]/text()').get(),
                'product_category_3rdlevel' : response.xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/a[4]/text()').get(),
                # 'mrp_on_bigbasket' : response.xpath('//*[@id="40161711"]/tr[1]/td[2]/text()[2]').get(),
                # 'selling_price_bigbasket' : response.xpath('//*[@id="40161711"]/tr[2]/td[2]/text()[2]').get(),
                # 'about_product' : response.xpath('//*[@id="about_0"]/div[2]/div/div/text()').get().strip(),

                # 'EAN_code' : response.xpath('//*[@id="about_2"]/div[2]/div/div/text()[1]').get().strip()
            }


#for eancode check for the condition and positiona and then scrape....lets see next time
