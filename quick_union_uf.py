from typing import List


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