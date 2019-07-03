import os


class ESSettings():
    ''' Elasticsearch Settings
    '''
    INDEX = os.environ.get('ES_INDEX')
    ELASTIC_CREDENTIALS = (os.environ.get('ES_USER'), os.environ.get('ES_PASSWORD'))
    HOST = os.environ.get('ES_HOST')
    PORT = os.environ.get('ES_PORT',9200)

    def __init__(self):
        self.__validate_credentials()
        self.__validate_index()
        self.__validate_host()

    def __validate_credentials(self):
        user, password = self.ELASTIC_CREDENTIALS

        if user is None:
            raise ValueError("ES_USER should not be empty")

        if password is None:
            raise ValueError("ES_PASSWORD should not be empty")

    def __validate_index(self):
        if self.INDEX is None:
            raise ValueError("ES_INDEX should not be empty")

    def __validate_host(self):
        if self.HOST is None:
            raise ValueError("ES_HOST should not be empty")
