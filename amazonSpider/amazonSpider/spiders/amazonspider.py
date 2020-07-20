import scrapy
from ..items import AmazonspiderItem

class AmazonspiderSpider(scrapy.Spider):
    name = 'amazonspider'
    allowed_domains = ['amazon.com']
    start_urls = [
        'https://www.amazon.com.au/s?k=laptop&dc&qid=1595242056&rnid=5373057051&ref=sr_pg_1'
    ]

    def parse(self, response):

        items = AmazonspiderItem()

        product_img = response.css('.s-image::attr(src)').extract()
        product_price = response.css('span.a-offscreen::text').extract()
        product_name = response.css('.a-text-normal::text').extract()

        items['product_img'] = product_img
        items['product_price'] = product_price
        items['product_name'] = product_name

        yield items

        # nextpage = response.css('li.a-last a::attr(href)').get()
        # if nextpage is not None:
        #     yield response.follow(nextpage, callback=self.parse)

