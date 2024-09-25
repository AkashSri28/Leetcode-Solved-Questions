class TrieNode:
    def __init__(self):
        self.children = {}  # ch:TrieNode, freq
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, s):
        node = self.root
        for ch in s:
            if ch not in node.children:
                node.children[ch] = [TrieNode(), 1]
            else:
                node.children[ch][1] += 1
            node = node.children[ch][0]
        node.isEnd = True
        
    def search(self, word):
        node = self.root
        res = 0
        for ch in word:
            if ch in node.children:
                res += node.children[ch][1]
                node = node.children[ch][0]  
            else:
                break
        return res

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
            
        ans = []
        for word in words:
            ans.append(trie.search(word))
            
        return ans