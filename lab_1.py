

import processor.word_processor as word_processor
import processor.trie as Trie

# Requests
searched_word = input("What would you like to search?")
new_search = word_processor.WordProcessor(searched_word)
print('Looking for "'+searched_word+'"')
response = new_search.read_api()
# Gets the first document found
list_response = response['results']
if list_response:
    id_type = new_search.get_id(response)

    # Gets the raw text in content, and then deletes the punctuation from it
    book_content = new_search.get_raw_text(id_type)
    book_content = new_search.clean_punctuation(book_content)
    text_list = new_search.fill_list(book_content)
    full_list = new_search.delete_stopwords(text_list)

    # Build the Tree
    print("\nCreating the Trie . . .")
    trie = Trie.Node()
    highest_values = {}
    for word in full_list:
        last_value = trie.add_subnode(word, trie)
        highest_values[word] = last_value
    print("\nSuccess!")
    # List comprehension that gets a list of all the values sorted from lower to higher
    test = [items for items in sorted(highest_values.values())]
    # Gets the last 3 values, in this case always the biggest 3 values
    last_values = test[-3:]

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
    print("No content was retrieved for "+searched_word+", try with another word.")
