import math
def solution(X, Y, D):
    step = 0
    if X <= Y:
        dist = Y - X
        step = math.ceil(dist / D)
    return int(step)

print(solution(1, 5, 2))
