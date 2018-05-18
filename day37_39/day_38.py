import research

def main():
    print('Alcohol Consumption Worldwide...')

    research.init()

    print('Countries that drink the most')
    drink_most = research.drink_most()
    for idx, drink in enumerate(drink_most[:5],1):
        print(f"{idx} : {drink.country} - {drink.total_litres_of_pure_alcohol}")

    print('Countries that drink the least')
    drink_least = research.drink_least()
    for idx, drink in enumerate(drink_least[:5],1):
        print(f"{idx} : {drink.country} - {drink.total_litres_of_pure_alcohol}")

    print('Countries that drink the least - non-zero')
    drink_least = research.drink_nonzero_least()
    for idx, drink in enumerate(drink_least[:5], 1):
        print(f"{idx} : {drink.country} - {drink.total_litres_of_pure_alcohol}")

    print('Countries that drink the most spirits')
    drinks = research.most_spirits()
    for idx, drink in enumerate(drinks[:5], 1):
        print(f"{idx} : {drink.country} - {drink.spirit_servings} servings")

    print('Countries that drink the least spirits')
    drinks = research.least_spirits()
    for idx, drink in enumerate(drinks[:5], 1):
        print(f"{idx} : {drink.country} - {drink.spirit_servings} servings")

    print('Countries that drink the least spirits')
    drinks = research.least_nonzero_spirits()
    for idx, drink in enumerate(drinks[:5], 1):
        print(f"{idx} : {drink.country} - {drink.spirit_servings} servings")


if __name__ == '__main__':
    main()