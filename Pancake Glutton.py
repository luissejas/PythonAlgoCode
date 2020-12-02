def CheckPancakeValue(Player):
    try:
        Player = int(input("Please input the number of pancakes you ate!\n"))

    except ValueError as error:
        print("Wrong input! Please insert a N-U-M-B-E-R!\n")
    while Player <= -1:
        Player = int(input("Wrong input! Please put a positive input!\n"))
    return Player



if __name__ == '__main__':
    # iPlayerNumber is the variable that determines the number of the players
    # iPlayer1 is the variable that assigns a player (1, 2, 3, ..)
    # lPlayerList is the list containing the number of pancakes eaten by the players

    print("Welcome the Pancake Eating Contest! The player that eats the highest amount of pancakes wins!")
    bGoodInput = False
    # Here, we check the number of players and validate the input
    while (bGoodInput == False):
        try:
            iPlayerNumber = int(input("Please enter the number of people participating in the Pancake Eating contest (1-3)\n"))
            bGoodInput = True

        except ValueError as error:
            print("Wrong input! Please insert a N-U-M-B-E-R!\n")
            bGoodInput = False


    while 0 > iPlayerNumber or iPlayerNumber > 3:
            iPlayerNumber = int(input("Wrong input! Please try again!\n"))


    print("Okay, " + str(iPlayerNumber) + " players.\nLet's begin!")
    iPlayer1 = 1
    print("Player 1! Go!")
    iPlayer1 = CheckPancakeValue(iPlayer1)
    lPlayerList = [iPlayer1]




    if iPlayerNumber == 1:
        print("Since there is only one player...")
        print("The player who ate most pancakes is you! You ate a total of " + str(iPlayer1) + " pancakes!")

    if iPlayerNumber == 2:
        print("Player 2! Go!")
        iPlayer2 = 1
        iPlayer2 = CheckPancakeValue(iPlayer2)
        if iPlayer1 > iPlayer2:
            print("Player 1! You sure love to eat! You won this competition with a score of " + str(iPlayer1))
            print("Your lead was by " + str(iPlayer1 - iPlayer2) + " pancakes.")
            print("Player 2, get good!")
        else:
            print("Player 2! You sure love to eat! You won this competition with a score of " + str(iPlayer2))
            print("Your lead was by " + str(iPlayer2 - iPlayer1) + " pancakes.")
            print("Player 1, get good!")

    if iPlayerNumber == 3:
        print("Player 2! Go!")
        iPlayer2 = 1
        iPlayer2 = CheckPancakeValue(iPlayer2)

        print("Player 3! Go!")
        iPlayer3 = 1
        iPlayer3 = CheckPancakeValue(iPlayer3)
        lPlayerList.append(iPlayer2)
        lPlayerList.append(iPlayer3)
        dPlayerBase = dict([
            (iPlayer1, "Player 1"),
            (iPlayer2, "Player 2"),
            (iPlayer3, "Player 3"),
        ])
        lPlayerList.sort(key=int, reverse=True)
        print("First place goes to " + dPlayerBase[lPlayerList[0]] + " with " + str(lPlayerList[0]) + " pancakes!")
        print("Second place goes to " + dPlayerBase[lPlayerList[1]] + " with " + str(lPlayerList[1]) + " pancakes!")
        print("Third place goes to " + dPlayerBase[lPlayerList[2]] + " with " + str(lPlayerList[2]) + " pancakes!")
        print("Thank you for participating!")