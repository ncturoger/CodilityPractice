def solution_1(A):
    for i in range(100000):
        if i+1 not in A:
            return i+1

def solution_2(A):
    A.sort()
    last_number = A[0] - 1 if A[0] < 0 else 0
    for idx, item in enumerate(A):
        print(item)
        if last_number + 1 != item and last_number != item:
            if last_number + 1 > 0:
                return last_number + 1
            
            else:
                if idx == (len(A)-1):
                    if item<0: 
                        return 1
                    else:
                        return last_number + 1 if last_number + 1 > 0 else 1
                else:
                    if item != 1:
                        return 1

        elif idx == (len(A)-1):
            if item<0:
                return 1
            else:
                return item + 1

        last_number = item


def solution_3(A):
    A.sort()
    last_number = A[0] - 1 if A[0] < 0 else 0
    for idx, item in enumerate(A):
        if item > 0:
            if last_number + 1 != item and last_number != item:
                if last_number + 1 > 0:
                    return last_number + 1 if last_number + 1 > 0 else 1
                else:
                    if idx == (len(A)-1):
                        if item == 1:
                            return 2
                        else:
                            return 1
            else:
                if idx == (len(A)-1):
                        return item + 1 if item + 1 > 0 else 1

        else:
            if idx == (len(A)-1):
                return 1
        last_number = item

print(solution_3([-1000000, 1000000]))