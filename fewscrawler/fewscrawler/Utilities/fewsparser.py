from lxml import html
from mongoDB.entities.fews import FewsModel


class Parser:

    @staticmethod
    def parse_web_content(web_response):
        entity = FewsModel(str(web_response.css('title::text').extract()), "description", "category")
        return entity



