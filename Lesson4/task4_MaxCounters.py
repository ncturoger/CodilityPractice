def solution_1(N, A):
    counters = [0 for i in range(N)]
    for operation in A:
        if operation == N+1:
            max_value = max(counters)
            counters = [max_value for i in range(N)]
        else:
            counters[operation-1] += 1
    return counters

from collections import Counter
def solution_2(N, A):
    if N+1 in A:
        counters = [0 for i in range(N)]
        max_index = max([n for n, x in enumerate(A) if x==N+1])
        operations = Counter([i for i in A[:max_index] if i != N+1]).values()
        if operations:
            max_value = max(operations)
            counters = [max_value for i in range(N)] 
        for operation in A[max_index+1:]:
            counters[operation-1] += 1
        return counters

    else:
        counters = [0 for i in range(N)]
        for operation in A:
            counters[operation-1] += 1
        return counters

def solution_3(N, A):
    if N+1 in A:
        counters = [0 for i in range(N)]
        max_index = max([n for n, x in enumerate(A) if x==N+1])
        for index, operation in enumerate(A):
            if operation == N+1:


            else:
                counters[operation-1] += 1
