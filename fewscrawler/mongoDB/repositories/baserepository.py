from mongoDB.context.mongocontext import MongoContext


class BaseRepository:

    def __init__(self, collection_name):
        context = MongoContext()
        self.client = context.client
        self.collection = context.database[collection_name]

    def create(self, entity):
        if entity is not None:
            self.collection.insert(entity)
        else:
            raise Exception("Nothing to save, because entity parameter is None")

    def get(self, entity_id=None):
        if entity_id is None:
            return self.collection .find({})
        else:
            return self.collection .find({"_id": entity_id})

    def update(self, entity):
        if entity is not None:
            # the save() method updates the document if this has an _id property
            # which appears in the collection, otherwise it saves the data
            # as a new document in the collection
            self.collection.save(entity.get_as_json())
        else:
            raise Exception("Nothing to update, because entity parameter is None")

    def delete(self, entity):
        if entity is not None:
            self.collection.remove(entity.get_as_json())
        else:
            raise Exception("Nothing to delete, because entity parameter is None")

