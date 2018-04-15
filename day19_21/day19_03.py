from itertools import permutations, combinations

text_string = 'darren'

print('***** PERMUTATIONS *****')

for perm in permutations(text_string, r=2):
    print(perm)

print('***** COMBINATIONS *****')

for comb in combinations(text_string, r=2):
    print(comb)