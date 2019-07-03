import json

from elasticsearch import Elasticsearch

from settings import ESSettings


class ElasticSearch():
    client = None
    settings = None

    def __init__(self):
        self.settings = ESSettings()
        self.__set_client()

    def __set_client(self):
        self.client = Elasticsearch([self.settings.HOST], port=self.settings.PORT,
                    http_auth=self.settings.ELASTIC_CREDENTIALS, verify_certs=False)

    def insert(self, data):
        self.client.index(index=self.settings.INDEX, doc_type='item', body=data)
