import scrapy
from fewscrawler.Utilities.fewsparser import Parser
from mongoDB.repositories.fewsrepository import FewsRepository


class FewsCrawler(scrapy.Spider):
    name = "fews"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        parser = Parser()
        entity = parser.parse_web_content(response)
        document = self.to_document(entity)
        fews_repository = FewsRepository()
        fews_repository.create(document)

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def to_document(self, obj):
        return dict(
            title=obj.title,
            description=obj.description,
            category=obj.category,
            Date=obj.Date,
        )




