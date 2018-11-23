def solution(A):
    if A:
        A = [item for item in A if item]
        A.sort()
        for idx, val in enumerate(A):
            if idx + 1 != val:
                return idx + 1
        return A[-1] + 1
    else:
        return 1