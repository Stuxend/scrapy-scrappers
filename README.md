# scrapy-scrappers
This is a repository of examples of scrappers that I was developing for those who are starting in spcrapy and need some help.


This is a basic description of the scripts.

import scrapy   -> HERE WE NEED TO IMPORT SCRAPY
import datetime as dt    -> HERE WE NEED TO IMPORT datetime in order to get a field with the "scrapy date"

class SPYDER_CHAMP(scrapy.Spider): ## HERE WE NEED TO CREATE A CLASS TO START SCRATCH THE WWW
    name = 'ultimasnoticias' ## SET A NAME TO YOUR SCRAPPER.
    allowed_domains = ['clarin.com']  ## SET A ALLOWED DOMAIN IN ORDER TO KEEP IN THIS DOMAIN.
    start_urls = ['https://www.clarin.com/ultimas-noticias/'] ## THE URL THAT WE START TO SCRAPP. 

    def parse(self, response): #WE CREATE A FUNCTION
        articles = response.xpath("//article[@class='list-format list']") ## START TO SCRATCH THE BOX IN MY SITE WITH THE CLASS "list-format list"
        for noticia in articles: ## START TO SCRATCH EACH FIELD ON THE BOX.
            text = noticia.xpath(
                ".//p[@class='volanta']/text()").extract_first()
            fecha_public = article.xpath(
                ".//p[@class='limit']/text").extract_first()
            fecha_scrap = dt.datetime.today().strftime("%m/%d/%Y")
            contenido = article.xpath(
                ".//p[@class='summary']/text()").extract_first()
            yield {'Titulo Noticia': text, 'fecha publicado': fecha_public, 'fecha scrapper': fecha_scrap, 'Contenido': contenido} ## here I unify my fields and I define a value.
