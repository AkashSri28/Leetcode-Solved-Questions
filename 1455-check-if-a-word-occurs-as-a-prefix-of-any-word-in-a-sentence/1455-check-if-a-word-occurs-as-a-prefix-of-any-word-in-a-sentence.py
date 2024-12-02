class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
                
            node = node.children[ch]
        node.isEnd = True
        
    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
            if node.isEnd:
                return True
        return False
    

    
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        trie = Trie()
        trie.insert(searchWord)
        
        for index, word in enumerate(words):
            if trie.search(word):
                return index+1
            
        return -1
            
        