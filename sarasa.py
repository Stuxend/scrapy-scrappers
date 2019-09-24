import scrapy
import datetime

class EKOSpider(scrapy.Spider):
    name = "eko_spider"
    start_urls = ['https://www.ekoparty.org/editions/eko15/trainings/index.php']
    
    def parse(self, response):
            articles = response.xpath(".//div[@class='box-text']")
            for article in articles:
                    now = (datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
                    content = article.xpath(".//h2[@class='title cyan']/descendant::text()").extract()
                    yield {'text': content, 'fecha': now}