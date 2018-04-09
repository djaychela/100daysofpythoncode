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
    print(f'Welcome, player {player}')


if __name__ == '__main__':
    main()