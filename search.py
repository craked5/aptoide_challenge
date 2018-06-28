class AutocompleteSearch:
    def __init__(self):
        self.children = {}  #represents every children that this node contains
        self.word_end = False  #Flag to represent that a word ends at this node

    def insert(self, word):
        for char in word:
            if char not in self.children:
                self.children[char] = AutocompleteSearch()
            self = self.children[char]
        self.word_end = True

    def search(self, prefix):
        results = []
        if self.word_end:
            results.append(prefix)
        for (char, node) in self.children.items():
            results.extend(node.search(prefix + char))
        return results

    def autocomplete_start(self, prefix):
        node = self
        try:
            for char in prefix:
                if char not in node.children:
                    return None
                node = node.children[char]
            return list(node.search(prefix))
        except TypeError as e:
            raise TypeError("Bad char, check the input.", e)