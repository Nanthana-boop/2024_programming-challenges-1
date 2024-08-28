from itertools import combinations_with_replacement

def find_prime_combinations(arr, target_sum):
    result = []
    
    
    for combo in combinations_with_replacement(arr, 2): 
        if sum(combo) == target_sum:
            result.append(list(combo))
    
    return result

arr = [2, 3, 5, 7, 11]
target_sum = 10
output = find_prime_combinations(arr, target_sum)
print(output)
