def solution_1(A):
    distinct_set = set()
    if len(A) > 0:
        for idx, item in enumerate(A):
            if idx == 0:
                if len(A) == 1:
                    return 1
                elif item != A[idx + 1]:
                    distinct_set.add(item)
            elif idx == (len(A) - 1):
                if item != A[idx - 1]:
                    distinct_set.add(item)
            else:
                if item != A[idx + 1] and item != A[idx - 1]:
                    distinct_set.add(item)

    return len(distinct_set)

def solution_2(A):
    distinct_set = set()
    if A:
        for item in A:
            distinct_set.add(item)
    
    return len(distinct_set)
        