from TrieNode import TrieNode

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        current = self.root
        for letter in word:
            index = ord(letter) - ord('a')
            if not current.children[index]:
                current.children[index] = TrieNode()
            current = current.children[index]
        current.isLeaf = True

    def formWords(self, centerLetter):
        words = []

        def dfs(node, containsCenterLetter, curWord):
            if(node.isLeaf and containsCenterLetter):
                words.append(curWord)
            for letter in letters:
                index = ord(letter) - ord('a')
                if node.children[index]:
                    dfs(node.children[index], containsCenterLetter or (letter == centerLetter), curWord + letter)

        dfs(self.root, False, "")

        return words;