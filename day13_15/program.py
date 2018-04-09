from day13_15.actors import Creature, Wizard, Dragon
import random




def print_header():
    print('*******************************************')
    print('*                                         *')
    print('*           WIZARD GAME APP               *')
    print('*                                         *')
    print('*******************************************')
    print()


def game_loop():
    creatures = [
        Creature('Bat', 5),
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Dragon('Black Dragon', 50, scaliness=2, breathes_fire=False),
        Wizard('Evil Wizard',1000),
    ]

    hero = Wizard('Gandalf', 75)

    while True:
        active_creature = random.choice(creatures)

        print('A {} of level {} has appeared from a dark and foggy forest....'
              .format(active_creature.name, active_creature.level))
        print()

        cmd = input('Do you [a]ttack, [r]un or [l]ook around?').lower()

        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
                print("The Wizard defeated {}".format(active_creature.name))
            else:
                print("The Wizard has been defeated by {}".format(active_creature.name))
        elif cmd == 'r':
            print('The Wizard has become unsure of his powers and flees...')
            # TODO: Run
        elif cmd == 'l':
            print('The wizard {} takes in the surrounding and sees:'.format(hero.name))
            for c in creatures:
                print('* {} of level {}'.format(c.name, c.level))

        else:
            print('OK, exiting the game, bye!')
            break


    print('Goodbye!')


def main():
    print_header()
    game_loop()

if __name__ == '__main__':
    main()