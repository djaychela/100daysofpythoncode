import itertools
import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    output_list = []
    permutations = _get_permutations_draw(draw)
    for perm in permutations:
        if perm in dictionary:
            output_list.append(perm)
    return output_list


def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    output_list = []
    for i in range(len(draw)):
        possibles = itertools.permutations(draw, r=i)
        for pos in possibles:
            pos2 = ''.join(pos).lower()
            output_list.append(pos2)
    return output_list


draw = ['G', 'A', 'R', 'Y', 'T', 'E', 'V']
print(get_possible_dict_words(draw))
