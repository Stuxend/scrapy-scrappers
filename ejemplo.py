import scrapy
import datetime as dt

class ClarinSpiderUltimas(scrapy.Spider):
    name = 'ultimasnoticias'
    allowed_domains = ['clarin.com']
    start_urls = ['https://www.clarin.com/ultimas-noticias/']

    def parse(self, response):
        articles = response.xpath("//article[@class='list-format list']")
        for article in articles:
            text = article.xpath(
                ".//p[@class='volanta']/text()").extract_first()
            fecha_public = article.xpath(
                ".//div[@class='fecha pull-left col-lg-2 col-md-2 no-p']/p[1]/text()").extract_first()
            fecha_scrap = dt.datetime.today().strftime("%m/%d/%Y")
            contenido = article.xpath(
                ".//p[@class='summary']/text()").extract_first()
            yield {'Titulo Noticia': text, 'fecha publicado': fecha_public, 'fecha scrapper': fecha_scrap, 'Contenido': contenido}
