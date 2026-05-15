class UnionFind:
    def __init__(self, n: int):
        self.parents = {}
        self.rank = {}
        for i in range(n):
            self.parents[i] = i
            self.rank[i] = 0

    # find takes in an identifier and returns the parent of the tree
    def find(self, identifier: int) -> int:
        if identifier not in self.parents:
            return -1
        if self.parents[identifier] != identifier:
            # if we aren't our own parent, we should do path compression to keep things small
            self.parents[identifier] = self.find(self.parents[identifier])
        return self.parents[identifier]

    def union(self, i: int, j: int) -> bool:
        parent_i, parent_j = self.find(i), self.find(j)
        # these are already part of the same tree, 
        if parent_i == parent_j:
            return False

        # We need to union them by their rank. We attach the smaller tree
        # to the bigger tree so that the total tree depth remains unchanged.
        # if trees are equal size, pick one consistently
        if self.rank[parent_i] < self.rank[parent_j]:
            # attach the small tree to the bigger tree
            self.parents[parent_i] = parent_j
        elif self.rank[parent_j] < self.rank[parent_i]:
            # same thing, attach small tree to bigger tree
            self.parents[parent_j] = parent_i
        else:
            # the trees are of equal size, attach i --> j
            # increase j's size by 1
            self.parents[parent_i] = parent_j
            self.rank[parent_j] += 1
        return True

    def print(self):
        for k, v in self.parents.items():
            print(k, ' --> ', v)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))

        # union find all the emails together
        seen_emails = {}
        for i, account in enumerate(accounts):
            name = account[0]
            for email in account[1:]:
                if email in seen_emails:
                    uf.union(i, seen_emails[email])
                else:
                    seen_emails[email] = i
        
        # now go find the account owner for everyone and store it in a dictionary
        emails_by_index: Dict[int, set] = collections.defaultdict(set)
        for i in range(len(accounts)):
            parent = uf.find(i)
            for email in accounts[i][1:]:
                emails_by_index[parent].add(email)
        
        # now format the output
        out: List[List[str]] = []
        for idx, emails in emails_by_index.items():
            result = []
            result.append(accounts[idx][0])
            result.extend(list(emails))
            result.sort()
            out.append(result)
        return out




        