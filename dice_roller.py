import random
def main():
    dice_rolls = 2
    dice_sum = 0
    for i in range(0, dice_rolls):
        roll = random.randint(1,6)
    #dice_sum = dice_sum + roll
        dice_sum += roll
        if roll ==1:
            print(f'You rolled a {roll}! Critical fail!')
        elif roll ==6:
            print(f'You rolled a {roll}! Critical succes!')
        else:
            print(f'You rolled a {roll}')
    print(f'Your sum is {dice_sum}')


if __name__== "__main__":
  main()
