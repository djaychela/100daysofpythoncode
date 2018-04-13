import random

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def pairs_gen():
    for i in range(10):
        name_1 = random.choice(NAMES).split()[0].title()
        name_2 = random.choice(NAMES).split()[0].title()
        output = name_1 + ' teams up with ' + name_2
        yield output

names_title = [name.title() for name in NAMES]
print(names_title)
names_reverse = [' '.join(name.title().split()[::-1]) for name in NAMES]
print(names_reverse)
pairs = pairs_gen()
for _ in range(10):
    print(next(pairs))