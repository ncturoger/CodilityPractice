def solution_1(X, A):
    position_check_set = [i+1 for i in range(X)]
    for idx, value in enumerate(A):
        if value in position_check_set:
            position_check_set.remove(value)
        if not position_check_set:
            return idx
    return -1


def solution_2(X, A):
    position_check_set = set([i+1 for i in range(X)])
    for idx, value in enumerate(A):
        position_check_set.discard(value)
        if not position_check_set:
            return idx
    return -1     
    
        