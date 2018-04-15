NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    names = [name.title() for name in names]
    return list(set(names))


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    names_reverse = [' '.join(name.title().split()[::-1]) for name in names]
    names_reverse.sort(reverse=True)
    names_forward = [' '.join(name.title().split()[::-1]) for name in names_reverse]
    return names_forward


def shortest_first_name(names):
    """Returns the shortest first name (str)"""
    names = dedup_and_title_case_names(names)
    names_first = [name.title().split()[0] for name in names]
    names_first.sort(key=lambda s: len(s))
    return names_first[0]


print(dedup_and_title_case_names(NAMES))
print(sort_by_surname_desc(NAMES))
print(shortest_first_name(NAMES))