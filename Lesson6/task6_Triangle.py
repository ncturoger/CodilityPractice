def solution(A):
    has_tri = 0
    for x_idx, x_val in enumerate(A):
        for y_idx, y_val in enumerate(A):
            if x_idx > y_idx:
                for z_idx, z_val in enumerate(A):
                    if y_idx > z_idx:
                        if x_val < y_val + z_val and y_val < x_val + z_val and z_val < x_val + y_val:
                            has_tri = 1
    return has_tri
