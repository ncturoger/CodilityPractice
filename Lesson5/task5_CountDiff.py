# O(B-A)
def solution_1(A, B, K):
    count = 0
    for i in range(A, B+1, 1):
        if i % K == 0:
            count += 1
    return count


# O((B-A)/K)
def solution_2(A, B, K):
    count = 1 if (A == 0 or B == 0) else 0
    judge_num = K
    while(judge_num <= B):
        if judge_num >= A:
            count += 1
        judge_num += K
    return count

# not work
def solution_3(A, B, K):
    count = 1 if (A == 0 or B == 0) else 0
    judge_num = A + (A % K)
    if A == B:
        if judge_num == A and A != 0:
            count += 1
    else:
        while(judge_num <= B):
            if judge_num >= A and A != 0:
                count += 1
            judge_num += K
    return count