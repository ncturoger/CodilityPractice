# n**3
def solution(A):
    A.sort()
    product_list = []
    for idx, item in enumerate(A[:-2]):
        for i in range(idx+2, len(A)):
            product_list.append(item * A[idx + 1] * A[i])
    if product_list:
        return max(product_list)

