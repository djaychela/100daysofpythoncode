from itertools import combinations, permutations


def friends_teams(list_of_friends, team_size = 2, order_does_matter = False):
    if order_does_matter:
        return permutations(list_of_friends, r=team_size)
    else:
        return combinations(list_of_friends, r=team_size)


team_list = ['Bob','Fred','Stan','Martin']


for team in friends_teams(team_list, 2, False):
    print(team)