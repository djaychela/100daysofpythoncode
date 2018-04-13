import random

roll_menu = ['[r]ock', '[g]un', '[l]ightning', '[d]evil', '[dr]agon', '[w]ater', '[a]ir', '[p]aper', '[sp]onge',
             '[wo]lf', '[t]ree', '[h]uman', '[sn]ake', '[sc]issors', '[f]ire']
roll_choices = ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge',
                'wolf', 'tree', 'human', 'snake', 'scissors', 'fire']
roll_dict = {'r': 'rock', 'g': 'gun', 'l': 'lightning', 'd': 'devil', 'dr': 'dragon', 'w': 'water', 'a': 'air',
             'p': 'paper',
             'sp': 'sponge', 'wo': 'wolf', 't': 'tree', 'h': 'human', 'sn': 'snake', 'sc': 'scissors', 'f': 'fire'}
roll_lose = {'rock': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
             'gun': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
             'lightning': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
             'devil': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
             'dragon': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
             'water': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
             'air': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
             'paper': ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
             'sponge': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
             'wolf': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
             'tree': ['human', 'snake', 'scissors', 'fire', 'rock', 'gun', 'lightning'],
             'human': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
             'snake': ['scissors', 'fire', 'rock', 'gun', 'lightning', 'devil', 'dragon'],
             'scissors': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
             'fire': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air']}


class Player():
    def __init__(self, name):
        self.name = name
        self.roll = None
        self.score = 0

    def generate_roll(self):
        self.roll = random.choice(roll_choices)
        print(f'{self.name} rolls {self.roll.capitalize()}')
        return self.roll

    def input_roll(self):
        roll_menu_text = ','.join(roll_menu)
        roll_choice = None
        while not roll_choice:
            roll = input(f'{self.name} - Enter Roll = {roll_menu_text}: ')
            if roll in roll_dict.keys():
                roll_choice = roll_dict[roll]
        self.roll = roll_choice

    def win_lose(self, other_player_roll):
        if other_player_roll == self.roll:
            return 'draw'
        if other_player_roll in roll_lose[self.roll]:
            return 'lose'
        else:
            return 'win'

    def score_increase(self):
        self.score += 1


def print_header():
    print('****************************')
    print('*                          *')
    print('*   Rock Paper Scissors    *')
    print('*                          *')
    print('****************************')
    print()


def main():
    print_header()
    player = input('Enter your name: ')
    player_1 = Player(name=player)
    player_2 = Player(name='Computer')
    count = 1
    while count <= 3:
        player_1.input_roll()
        player_2.generate_roll()
        result = player_1.win_lose(player_2.roll)
        if result == 'win':
            print(f"That's a win for {player_1.name} - {player_1.roll} beats {player_2.roll}")
            player_1.score_increase()
        elif result == 'lose':
            print(f"That's a win for {player_2.name} - {player_2.roll} beats {player_1.roll}")
            player_2.score_increase()
        else:
            print(f"That's a draw - both players picked {player_1.roll.capitalize()}")
        print(f"Current scores: {player_1.name}: {player_1.score} - {player_2.name}: {player_2.score}")
        count += 1
        if count == 4 and player_1.score == player_2.score:
            count -= 1
    print(f"Final score: {player_1.name}: {player_1.score} - {player_2.name}: {player_2.score}")


if __name__ == '__main__':
    main()
