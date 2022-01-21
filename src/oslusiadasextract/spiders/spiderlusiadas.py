import scrapy
from oslusiadasextract.utils import Utils
from oslusiadasextract.dbconnections.mongo_connection import MongoConnection

utils = Utils()
mongo_connection = MongoConnection()


class SpiderlusiadasSpider(scrapy.Spider):
    name = 'spiderlusiadas'
    start_urls = utils.generate_chants_links()

    def parse(self, response):
        array_with_text = response.xpath('//div[@class="uk-panel uk-panel-box estrofe"]/descendant::text()').extract()

        current_url = response.request.url
        chant_info = utils.parse_chant_url(current_url)
        chant_text = ' '.join(utils.parse_scrapy_response(array_with_text)).strip()

        print(chant_info['chant_number'])
        print(chant_info['stranza'])
        print(chant_text)

        mongo_connection.insert_chant({"chant_number": chant_info['chant_number'],
                                       "stranza": chant_info['stranza'],
                                        "text": chant_text})
        pass
