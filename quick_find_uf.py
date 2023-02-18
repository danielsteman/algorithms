from typing import List

N = [0,1,1,8,8,0,0,1,8,8]

for i in set(N):
    print(f"{[j for j in range(len(N)) if N[j] == i ]} are connected.")

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


qf = QuickFindUF(N)
print(qf.id)
print(qf.connected(6,5))
qf.union(4,5)
print(qf.id)

