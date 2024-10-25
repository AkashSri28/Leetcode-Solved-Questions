class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, folder):
        path = [path for path in folder.split('/') if path]
        node = self.root
        for p in path:
            if p not in node.children:
                node.children[p] = TrieNode()
                node = node.children[p]
            else:
                node = node.children[p]
                if node.isEnd:
                    return False
            
        node.isEnd = True
        return True
        
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key=lambda x:len(x))
        
        trie = Trie()
        ans = []
        for f in folder:
            if trie.insert(f):
                ans.append(f)
        
        return ans
        