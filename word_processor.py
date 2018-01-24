from collections import OrderedDict
import requests
import re


class WordProcessor:
    """Makes the requests and then clean the data"""

    def __init__(self, text, stopwords_list):
        self.text = text
        self.stopwords_list = stopwords_list

    def delete_stopwords(self, content):
        """Brings the stopwords list and then deletes the stopwords on it"""
        final_list = []
        while content:
            text_word = content.pop().lower().strip()
            if text_word not in self.stopwords_list:
                final_list.append(text_word)

        return final_list

    def clean_punctuation(self):
        """With Regulars Expressions, the main text is cleaned of punctuations"""
        no_punctuation = re.compile(r'[\,\.\"\!\?\;\:\-\(\)]+')
        clean_text = no_punctuation.sub(r' ', self.text)
        # [\,\.\"\!\?\;\:\-\(\)]+ <- looks for punctuation and characters such as , . " ! ? ; : - ( )
        return clean_text

    def fill_list(self, content):
        """Creates a list of words from the cleaned text"""
        word_list = re.findall(r'[A-Za-z]+', content)
        return word_list


