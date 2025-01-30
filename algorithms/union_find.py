"""
See which items belong to a group:

N = [0,1,1,8,8,0,0,1,8,8]

for i in set(N):
    print(f"{[j for j in range(len(N)) if N[j] == i ]} are connected.")

>>>

[0, 5, 6] are connected.
[1, 2, 7] are connected.
[3, 4, 8, 9] are connected.
"""

from typing import List


class QuickFindUF:
    def __init__(self, N: List[int]):
        self.id = N

    def connected(self, p: int, q: int) -> bool:
        return self.id[p] == self.id[q]

    def union(self, p: int, q: int) -> None:
        pid = self.id[p]
        qid = self.id[q]
        for i in range(len(self.id)):
            if self.id[i] == pid:
                self.id[i] = qid


class QuickUnionUF:
    def __init__(self, N: List[int]) -> None:
        self.id = N

    def _root(self, i: int) -> int:
        while i != self.id[i]:
            i = self.id[i]
        return i

    def connected(self, p: int, q: int) -> bool:
        return self._root(p) == self._root(q)

    def union(self, p: int, q: int) -> None:
        i = self._root(p)
        j = self._root(q)
        self.id[i] = j