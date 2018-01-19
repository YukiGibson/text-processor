
class Node:
    """Represents a node of the tree"""

    def __init__(self):
        """Initializes a Node"""
        self.values = 0
        self.sons = {}

    def get_son(self, search_index):
        return self.sons[search_index]

    def increase_counter(self):
        """Increase the counter on the last leaf"""
        self.values = self.values + 1

    def add_subnode(self, word, root):
        """Adds the subnodes"""
        son = root
        # print('\tAdding the word ' + word + " into the Trie")
        for i in range(0, len(word)):
            if word[i] in son.sons.keys():
                # print('index #'+str(i)+', letter ' + word[i] + ' exists as a subnode, changing the node')
                son = son.sons[word[i]]
            else:
                # print('index #'+str(i)+', letter '+word[i]+' does not exists as a subnode, creating new node')
                son.sons[word[i]] = Node()
                son = son.sons[word[i]]
        son.increase_counter()
        # print('The word ' + word + " has a values of " + str(son.values))
        return son.values

