import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    # allowed_domains = ['imdb.com']
    start_urls = ['http://imdb.com/']

    def parse(self, response):
        filmes = response.css('.cli-children')
        titulos = response.css('.cli-children a')
        
        pass
