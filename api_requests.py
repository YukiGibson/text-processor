import requests


class ApiRequests:

    def __init__(self, server, msj_key = ""):
        self.server = server
        self.msj_key = msj_key

    def new_request(self, new_server, msj_key=""):
        self.server = new_server
        self.msj_key = msj_key

    def make_post(self):
        response = requests.post(self.server, json=self.msj_key)
        return response.json()

    def make_get(self):
        response = requests.get(self.server)
        return response.json()

    def has_content(self):
        content = self.make_post()
        result = content['results']
        if result:
            return True
        else:
            return False

    def concatenate_id(self):
        """If more than one document is found, adds an incremental number to the key name"""
        content = self.make_post()
        id_type = {}
        counter = 0
        for value in content.values():
            for indexes in value:
                counter = counter + 1
                id_type['_type_' + str(counter)] = indexes['_type']
                id_type['_id_' + str(counter)] = indexes['_id']
        return id_type

    def get_raw_text(self):
        """Using the first key of the first document found, returns the raw text of it"""
        content = self.concatenate_id()
        if content['_id_1']:
            url = "http://codelab.subvertic.com/api/v1/document/" + content['_type_1'] + \
                  "/content/" + content['_id_1']
            self.new_request(url)
            response = self.make_get()
            for key, value in response.items():
                if '_source' in key:
                    return value['content']

    def get_stopwords(self):
        """Gets the list of stopwords in english"""
        url = "http://codelab.subvertic.com/api/v1/stopwords/en"
        self.new_request(url)
        response = self.make_get()
        stopwords = response
        stopwords_list = stopwords['swlist']
        return stopwords_list