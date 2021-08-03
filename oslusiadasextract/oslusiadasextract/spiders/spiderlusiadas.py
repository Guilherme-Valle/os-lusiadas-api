import scrapy

class SpiderlusiadasSpider(scrapy.Spider):
    name = 'spiderlusiadas'
    start_urls = ['https://oslusiadas.org/i/2']

    def parse(self, response):
        array_with_text = response.xpath('//div[@class="uk-panel uk-panel-box estrofe"]/descendant::text()').extract()
        array_with_text[0] = ''
        array_with_text[1] = ''
        array_with_text = list(filter(lambda x: x != "\n", array_with_text))
        chant = ' '.join(array_with_text).strip()
        pass
