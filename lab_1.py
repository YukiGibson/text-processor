

import processor.word_processor as word_processor
import processor.api_requests as api
import processor.trie as Trie

# Requests

server = "http://codelab.subvertic.com/api/v1/document/query"
searched_word = input("What would you like to search?")
msj_content = {"q": searched_word}
new_requests = api.ApiRequests(server=server, msj_key=msj_content)

print('Looking for "'+searched_word+'"')
if new_requests.has_content():
    raw_text = new_requests.get_raw_text()
    stopwords_list = new_requests.get_stopwords()

    new_search = word_processor.WordProcessor(text=raw_text, stopwords_list=stopwords_list)
    book_content = new_search.clean_punctuation()
    text_list = new_search.fill_list(book_content)
    full_list = new_search.delete_stopwords(text_list)

    # Build the Tree
    print("\nCreating the Trie . . .")
    new_trie = Trie.Node()
    highest_values = new_trie.build_trie(full_list)
    print("\nSuccess!")

    # Appends each item sorted in order to get the last values
    sorted_list = []
    for items in sorted(highest_values.values()):
        sorted_list.append(items)

    last_values = sorted_list[-3:]

    # In order to associate the value with the word,
    max_values = {}
    for key, value in highest_values.items():
        if value in last_values:
            max_values[key] = value

    # Prints the 3 most relevant words in the text
    sorted(max_values.values(), reverse=True)
    print("\tThe 3 most relevant words on the text are:")
    for key, value in max_values.items():
        print("Word: '" + key + "'. Times that appear in the text: " + str(value) + " times")
else:
    print('No content was found')


