def solution(S, P, Q):
    impact_value_dict = {'A': 1,'C': 2,'G': 3,'T': 4}
    impact_value_list = []
    for idx, per_start in enumerate(P):
        start = per_start
        end = Q[idx]
        impact_value = min([impact_value_dict[item] for item in S[start:end+1]])
        impact_value_list.append(impact_value)
    return impact_value_list

print(solution_2('CAGCCTA', [2, 5, 0], [4, 5, 6]))