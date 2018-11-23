def solution(A, K):
    if A:
        origin_list = rotate_list = A

        for i in range(K):
            rotate_list = [origin_list[-1]]
            for item in origin_list[:-1]:
                rotate_list.append(item)
            origin_list = rotate_list
        return rotate_list
    else:
        return []