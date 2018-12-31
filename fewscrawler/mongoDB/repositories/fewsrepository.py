import datetime
from mongoDB.repositories.baserepository import BaseRepository


class FewsRepository(BaseRepository):
    def __init__(self):
        BaseRepository.__init__(self, "Fews")

    def get_daily_fews(self):
        return self.database.entitys.find({"_date_time": str(datetime.datetime.now())})
