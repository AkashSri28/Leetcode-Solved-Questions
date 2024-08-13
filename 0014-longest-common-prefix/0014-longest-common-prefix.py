class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, s):
        node = self.root
        for ch in s:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True
        

    
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for s in strs:
            trie.insert(s)
            
        def find_longest_prefix(trie):
            node = trie.root
            prefix = []
            while len(node.children) == 1 and not node.isEnd:
                key = list(node.children.keys())[0]
                prefix.append(key)
                node = node.children[key]
                
            return "".join(prefix)
            
        return find_longest_prefix(trie)
            
        
        