class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, path):
        path_arr = path.split('/')
        node = self.root
        for p in path_arr:
            if p in node.children:
                node = node.children[p]
                if node.isEnd:
                    return False
            else:
                node.children[p] = TrieNode()
                node = node.children[p]
        node.isEnd = True
        return True

class Solution:        
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        ans = []
        trie = Trie()

        for f in sorted(folder):
            if trie.insert(f):
                ans.append(f)

        return ans

        # TC: O(nlogn+max(f))
        # SC: O(n*l)
        # Approach: Since we need to match prefixes, Trie will be used here. We will sort folders so that smaller length is picked first. Now create a Trie and iterate for folder. If we encounter end and folder has some path left means we have reached here earlier and end means a folder ended here. So our current folder is a sub folder. We wont add it to ans


        