import scrapy
from oslusiadasextract.utils import Utils
utils = Utils()


class SpiderlusiadasSpider(scrapy.Spider):
    name = 'spiderlusiadas'
    # start_urls = utils.generate_chants_links()
    start_urls = ['https://oslusiadas.org/i/']

    def parse(self, response):
        array_with_text = response.xpath('//div[@class="uk-panel uk-panel-box estrofe"]/descendant::text()').extract()
        chant = ' '.join(utils.parse_scrapy_response(array_with_text)).strip()
        current_url = response.request.url
        print(chant)
        pass
