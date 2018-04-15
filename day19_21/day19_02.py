from itertools import product

text_string = 'spoon'

for letter in product(text_string, repeat=len(text_string)):
    print(*letter)