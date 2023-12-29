import scrapy


class ImdbSpider(scrapy.Spider):
  name = 'imdb'
  # allowed_domains = ['imdb.com']
  start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

  def parse(self, response):
      for filmes in response.css('.cli-children'):
        yield{
          'titulo': filmes.css('.cli-children a').get()[118:-9],
          'ano': filmes.css('.cli-title-metadata-item::text').get(),
          'nota': response.css('.ratingGroup--imdb-rating, .ipc-icon--star-inline, #text::text').get()[31:34]
        }
