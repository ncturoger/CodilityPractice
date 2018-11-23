
def solution(N):
    zero_count = 0
    gap_list = []
    bin_N = '{0:b}'.format(N)
    print(bin_N)
    for i in bin_N:
        if i == '1':
            if zero_count > 0:
               gap_list.append(zero_count)
            zero_count = 0

        else:
            zero_count += 1
    
    return max(gap_list)

        



print(solution(1041))