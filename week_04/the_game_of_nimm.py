def main():
    """
    You should write your code here. 
    """
    stones = 20
    player = 1

    while stones > 0:
        print(f"There are {stones} stones left.")

        remove = int(input(f"Player {player} would you like to remove 1 or 2 stones? "))

        # Keep asking until input is valid
        while remove != 1 and remove != 2:
            remove = int(input("Please enter 1 or 2: "))

        stones = stones - remove
        print()

        # If no stones remain, current player loses
        if stones == 0:
            if player == 1:
                print("Player 2 wins!")
            else:
                print("Player 1 wins!")
        else:
            # Switch players
            if player == 1:
                player = 2
            else:
                player = 1


if __name__ == '__main__':
    main()