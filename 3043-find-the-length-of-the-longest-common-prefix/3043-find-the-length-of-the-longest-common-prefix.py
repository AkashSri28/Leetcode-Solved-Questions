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
        
    def search(self, word):
        node = self.root
        res = 0
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
                res += 1
            else:
                break
        return res


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        if len(arr2) < len(arr1):
            arr1, arr2 = arr2, arr1
            
        trie = Trie()
        for a in arr2:
            trie.insert(str(a))
        
        mini = 0
        for w in arr1:
            l = trie.search(str(w))
            mini = max(mini, l)
            
        return mini
        