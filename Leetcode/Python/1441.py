from typing import List
def buildArray(self, target: List[int], n: int) -> List[str]:
        op = []
        j = 0
        for i in range(1,n+1):
                if j >= len(target):
                    break
                if i == target[j]:
                    op.append("Push")
                    j += 1
                else:
                    op.append("Push")
                    op.append("Pop")
        return op
print(buildArray(None, [1,3], 3))
print(buildArray(None, [1,2,3], 3))