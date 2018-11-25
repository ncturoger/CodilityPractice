def solution(A):
    inter_count = 0
    for idx, center_1 in enumerate(A):
        for i in range(idx+1, len(A)):
            cent_distance = (i - idx)
            if cent_distance <= A[i] + center_1:
                inter_count += 1
    return inter_count
