
class Node:
    """Represents a node of the tree"""

    def __init__(self):
        """Initializes a Node"""
        self.values = 0
        self.subnode = {}

    def get_son(self, search_index):
        return self.subnode[search_index]

    def increase_counter(self):
        """Increase the counter on the last leaf"""
        self.values = self.values + 1

    def add_subnode(self, word, root):
        """Adds the subnodes"""
        current_node = root
        for i in range(0, len(word)):
            if word[i] in current_node.subnode.keys():
                current_node = current_node.subnode[word[i]]
            else:
                current_node.subnode[word[i]] = Node()
                current_node = current_node.subnode[word[i]]
        current_node.increase_counter()
        return current_node.values

    def build_trie(self, full_list):
        trie = Node()
        highest_values = {}
        for word in full_list:
            last_value = trie.add_subnode(word, trie)
            highest_values[word] = last_value
        return highest_values
