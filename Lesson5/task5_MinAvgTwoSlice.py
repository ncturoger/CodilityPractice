def solution(A):
    smallest = 10000
    smallest_idx = 0
    for i in range(len(A)):
        for j in range(len(A)-1):
            first_index = i
            second_index = j + 1
            if first_index < second_index:
                average_value = sum(A[first_index:second_index+1]) / (second_index - first_index + 1)
                if average_value < smallest:
                    smallest_idx = first_index
                    smallest = average_value

    return smallest_idx

print(solution([4, 2, 2, 5, 1, 5, 8]))