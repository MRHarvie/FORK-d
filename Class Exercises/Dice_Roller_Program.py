from DRC import Die, Dice

def main():
    print("The Dice Roller program\n")

    # Get the input
    num_dice = int(input("Enter the number of dice to roll: "))

    dice = Dice()
    for _ in range(num_dice):
        die = Die()
        dice.addDie(die)

    choice = 'y'
    while choice.lower() == 'y':
        dice.rollAll()

        print("YOUR ROLL: ", end="")
        for die in dice.list_die:
            print(die.value, end=' ')
        print()

        choice = input("Roll again? (y/n): ")

    print("Bye!")

if __name__ == "__main__":
    main()
