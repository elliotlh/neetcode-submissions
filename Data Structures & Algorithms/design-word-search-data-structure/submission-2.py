class TrieNode:
    def __init__(self, is_word: bool = False):
        self.children = {}
        self.is_word = is_word

class Trie:
    def __init__(self):
        self._root = TrieNode(False)

    def addWord(self, word: str) -> None:
        curr = self._root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True

    def getNextNodesForCharacter(self, from_node: TrieNode, char: str) -> List[TrieNode]:
        if not from_node:
            return []
        if char != '.':
            if char not in from_node.children:
                return []
            return [from_node.children[char]]
        options: List[TrieNode] = []
        for child in from_node.children.values():
            options.append(child)
        return options

    def getRoot(self) -> TrieNode:
        return self._root

class WordDictionary:
    def __init__(self):
        self._trie = Trie()

    def addWord(self, word: str) -> None:
        self._trie.addWord(word)

    def search(self, word: str) -> bool:
        if word == "":
            return False
        word_idx = 0
        current_node = self._trie.getRoot()
        viable_children = collections.deque(self._trie.getNextNodesForCharacter(current_node, word[word_idx]))
        word_idx += 1
        while viable_children:
            options_in_level = len(viable_children)
            for _ in range(options_in_level):
                child = viable_children.popleft()
                # case 1: these are all candidate children, return true if any of them are words
                if word_idx == len(word):
                    if child.is_word:
                        return True
                # otherwise we know we need to go deeper into the BFS
                else:
                    viable_children.extend(self._trie.getNextNodesForCharacter(child, word[word_idx]))
            word_idx += 1
        return False



        
