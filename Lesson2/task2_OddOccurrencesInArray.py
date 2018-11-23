def solution_1(A):
    for item in set(A):
        if A.count(item) % 2 != 0:
            return item

from collections import Counter
def solution_2(A):
    for item, ocurrence in Counter(A).items():
        if ocurrence % 2 != 0:
            return item