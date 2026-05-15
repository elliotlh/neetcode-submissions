class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        seen: Set[str] = set(['0000'])
        queue: deque[str] = collections.deque(['0000'])
        invalid: Set[str] = set(deadends)
        if '0000' in invalid:
            return -1
        turns: int = 0
        while queue:
            states_to_explore = len(queue)
            for i in range(states_to_explore):
                current_state = queue.popleft()
                for neighbor in self.generateNeighboringStates(current_state):
                    if neighbor in seen or neighbor in invalid:
                        continue
                    if neighbor == target:
                        return turns + 1
                    seen.add(neighbor)
                    queue.append(neighbor)
            turns += 1
        return -1

    def generateNeighboringStates(self, state: str) -> List[str]:
        results: List[str] = []
        for i in range(4):
            results.extend(self.generateNeighboringStatesAtPosition(state, i))
        return results

    def generateNeighboringStatesAtPosition(self, state: str, position: int) -> List[str]:
        number_neighbors = self.generateNeighboringStateForNumber(state[position])
        results: List[str] = []
        for neighbor in number_neighbors:
            results.append(state[0:position] + neighbor + state[position+1:])
        return results

    def generateNeighboringStateForNumber(self, num: str) -> List[str]:
        numeric = int(num)
        if numeric == 0:
            return ['9', '1']
        elif numeric == 9:
            return ['8', '0']
        return [str(numeric - 1), str(numeric + 1)]


        
        