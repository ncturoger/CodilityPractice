def solution(A):
    A.sort()
    for i, val in enumerate(A):
        if (i + 1) != val:
            return 0
    return 1
        