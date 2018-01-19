from collections import OrderedDict
import requests
import re


class WordProcessor():
    """Makes the requests and then clean the data"""

    def __init__(self, keyword):
        self.keyword = keyword
        self.text = ""

    def read_api(self):
        """Consumes the api that brings the books found"""
        url = "http://codelab.subvertic.com/api/v1/document/query"
        data = {"q": self.keyword}
        response = {}
        response = requests.post(url, json=data)
        print("post() : status " + str(response.status_code))
        return response.json()

    def delete_stopwords(self, content):
        """Brings the stopwords list and then deletes the stopwords on it"""
        url = "http://codelab.subvertic.com/api/v1/stopwords/en"
        response = requests.get(url)
        stopwords = response.json()
        print("get(stopwords) : status " + str(response.status_code))
        print("Length of content before remove(): " + str(len(content)))
        stopwords_list = stopwords['swlist']
        counter = 1

        verifier = OrderedDict()

        final_list = []

        while content:
            text_word = content.pop().lower().strip()
            if text_word not in stopwords_list:
                if text_word in verifier.keys():
                    verifier[text_word] = verifier[text_word] + 1
                else:
                    verifier[text_word] = 1
                counter = counter + 1
                final_list.append(text_word)

        print("Length of content after pop(): " + str(len(final_list)) + ".")
        return final_list

    def clean_punctuation(self, content):
        """With Regulars Expressions, the main text is cleaned of punctuations"""
        no_punctuation = re.compile(r'[\,\.\"\!\?\;\:\-\(\)]+')
        clean_text = no_punctuation.sub(r' ', content)
        # [\,\.\"\!\?\;\:\-\(\)]+ <- looks for punctuation and characters such as , . " ! ? ; : - ( )
        return clean_text

    def get_id(self, content):
        """If more than one document is found, adds an incremental number to the key name"""
        id_type = {}
        counter = 0
        for value in content.values():
            for indexes in value:
                # print(indexes['_type'] + " " + indexes["_id"])
                counter = counter + 1
                id_type['_type_' + str(counter)] = indexes['_type']
                id_type['_id_' + str(counter)] = indexes['_id']
        # print("Obtaining the document with an id: " + id_type['_id_1'])
        return id_type

    def get_raw_text(self, content):
        """Will make a GET in order to get the content of the book"""
        if content['_id_1']:
            url = "http://codelab.subvertic.com/api/v1/document/" + content['_type_1'] + \
                  "/content/" + content['_id_1']
            response = {}
            response = requests.get(url)
            test = {}
            test = response.json()
            for key, value in test.items():
                if '_source' in key:
                    return value['content']

    def fill_list(self, content):
        """Using re.findall(), creates a list of words from the cleaned text"""
        word_list = re.findall(r'[A-Za-z]+', content)
        return word_list


