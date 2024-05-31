import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscraper.com"]
    start_urls = ["https://books.toscraper.com"]

    def parse(self, response):
        pass
