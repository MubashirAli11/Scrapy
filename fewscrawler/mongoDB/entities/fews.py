import datetime


class FewsModel(object):
    title = ""
    description = ""
    category = ""
    Date = datetime.datetime.now()

    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category

