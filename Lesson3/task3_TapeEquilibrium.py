def solution_1(A):
    mix_difference = 2001
    for i in range(len(A)):
        a_part = A[:i]
        b_part = A[i:]
        if a_part and b_part:
            diff = abs(sum(a_part) - sum(b_part))
            if diff < mix_difference:
                mix_difference = diff
    return mix_difference


def solution_2(A):
    list_sum = sum(A)
    iter_sum = 0
    min_diff = 2001
    for item in A[:-1]:
        iter_sum += item
        diff = abs(list_sum - (iter_sum * 2))
        if diff < min_diff:
            min_diff = diff
    return min_diff
