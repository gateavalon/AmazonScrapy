# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class AmazonspiderPipeline:

    def __init__(self):
        # self.create_connection()
        # self.create_table()

        # create connection to the DB and collection
        self.conn = pymongo.MongoClient(
            "mongodb+srv://gateavalon:WmmTU2FARI81bUtD@clustergl-6x39r.mongodb.net/<dbname>?retryWrites=true&w=majority")
        db = self.conn['amazonspider']
        self.collection = db['laptoptable']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item


