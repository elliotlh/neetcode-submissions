from dataclasses import dataclass
class TrieNode:
    def __init__(self):
        self.full_word = ''
        self.is_word = False
        self.children = {}

    def can_be_deleted(self) -> bool:
        # node can be deleted if its not a word and it has no children
        return not self.is_word and len(self.children) == 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word: str) -> None:
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode()
            curr_node = curr_node.children[char]
        curr_node.is_word = True
        curr_node.full_word = word
        return

    def remove(self, word: str) -> None:
        curr_node = self.root
        stack: List[Tuple[TrieNode, str]] = []
        for char in word:
            # add to stack 1st
            stack.append((curr_node, char))
            # then recurse into child
            curr_node = curr_node.children[char]
        # always unmark child
        curr_node.is_word = False
        curr_node.full_word = ''
        while stack:
            parent, char = stack.pop()
            if curr_node.can_be_deleted():
                del parent.children[char]
                curr_node = parent
            else:
                break

    def get_next(self, node: TrieNode, char: str) -> Optional[TrieNode]:
        if char not in node.children:
            return None
        return node.children[char]

@dataclass(frozen=True)
class Point:
    row: int
    col: int

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.add(word)
        visited: Set[Point] = set()
        results: Set[str] = set()
        def dfs(coord: Point, curr_node: TrieNode):
            if coord.row < 0 or coord.row >= len(board):
                return
            if coord.col < 0 or coord.col >= len(board[0]):
                return
            if coord in visited:
                return
            visited.add(coord)
            char = board[coord.row][coord.col]
            next_node = trie.get_next(curr_node, char)
            if not next_node:
                visited.discard(coord)
                return
            if next_node.is_word:
                results.add(next_node.full_word)
            next_points = self.getNextPoints(coord)
            for point in next_points:
                dfs(point, next_node)
            visited.discard(coord)

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(Point(i, j), trie.root)

        return list(results)


    def getNextPoints(self, coord: Point) -> List[Point]:
        points = []
        points.append(Point(coord.row - 1, coord.col))
        points.append(Point(coord.row + 1, coord.col))
        points.append(Point(coord.row, coord.col - 1))
        points.append(Point(coord.row, coord.col + 1))
        return points
