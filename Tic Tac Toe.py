if __name__ == '__main__':
    # Define the playing board
    iPosition1 = 1
    iPosition2 = 2
    iPosition3 = 3
    iPosition4 = 4
    iPosition5 = 5
    iPosition6 = 6
    iPosition7 = 7
    iPosition8 = 8
    iPosition9 = 9
    iPlayerTurn = 1
    iPlayerInput = ""
    cPlayerMark = ""
    sNewGame = ""
    bMarkValidation = False
    bGameWon = False
    bInputCheck = False
    bNewGame = False

    # Putting the game board on display
    #print(str(iPosition1) + '|' + str(iPosition2) + '|' + str(iPosition3))
    #print("-+-+-")
    #print(str(iPosition4) + '|' + str(iPosition5) + '|' + str(iPosition6))
    #print("-+-+-")
    #print(str(iPosition7) + '|' + str(iPosition8) + '|' + str(iPosition9))
#Condition to restart the game
    while bNewGame == False:
        # Starting the game
        while bGameWon == False:
            #Actual Board
            print(str(iPosition1) + '|' + str(iPosition2) + '|' + str(iPosition3))
            print("-+-+-")
            print(str(iPosition4) + '|' + str(iPosition5) + '|' + str(iPosition6))
            print("-+-+-")
            print(str(iPosition7) + '|' + str(iPosition8) + '|' + str(iPosition9))
            # Player Prompt
            if iPlayerTurn == 1:
                print("Player 1! Make your move!")
                cPlayerMark = "X"
            else:
                print("Player 2 make your move!")
                cPlayerMark = "O"

            # Input Validation
            while bInputCheck == False:
                try:
                    iPlayerInput = int(input())
                    if iPlayerInput < 0 or iPlayerInput > 9:
                        print("Invalid number! Please try again!")
                        bInputCheck = False
                    else:
                        bInputCheck = True
                except ValueError:
                    print("A letter? You're better than that, pick a number!")
                    bInputCheck = False
            #Change in board
                if iPlayerInput == 1 and iPosition1 == 1:
                    iPosition1 = cPlayerMark
                    bMarkValidation = True
                elif iPlayerInput == 2 and iPosition2 == 2:
                    iPosition2 = cPlayerMark
                    bMarkValidation = True
                elif iPlayerInput == 3 and iPosition3 == 3:
                    iPosition3 = cPlayerMark
                    bMarkValidation = True
                elif iPlayerInput == 4 and iPosition4 == 4:
                    iPosition4 = cPlayerMark
                    bMarkValidation = True
                elif iPlayerInput == 5 and iPosition5 == 5:
                    iPosition5 = cPlayerMark
                    bMarkValidation = True
                elif iPlayerInput == 6 and iPosition6 == 6:
                    iPosition6 = cPlayerMark
                    bMarkValidation = True
                elif iPlayerInput == 7 and iPosition7 == 7:
                    iPosition7 = cPlayerMark
                    bMarkValidation = True
                elif iPlayerInput == 8 and iPosition8 == 8:
                    iPosition8 = cPlayerMark
                    bMarkValidation = True
                elif iPlayerInput == 9 and iPosition9 == 9:
                    iPosition9 = cPlayerMark
                    bMarkValidation = True
                else:
                    print("Try again!")
                    bInputCheck = False

            #Winning Conditions
            if iPosition1 == cPlayerMark and iPosition4 == cPlayerMark and iPosition7 == cPlayerMark:
                print(str(iPosition1) + '|' + str(iPosition2) + '|' + str(iPosition3))
                print("-+-+-")
                print(str(iPosition4) + '|' + str(iPosition5) + '|' + str(iPosition6))
                print("-+-+-")
                print(str(iPosition7) + '|' + str(iPosition8) + '|' + str(iPosition9))
                if cPlayerMark == "X":
                    print("Player 1 has won the game!")
                else:
                    print("Player 2 has won the game")
                bGameWon = True
            elif iPosition1 == cPlayerMark and iPosition2 == cPlayerMark and iPosition3 == cPlayerMark:
                print(str(iPosition1) + '|' + str(iPosition2) + '|' + str(iPosition3))
                print("-+-+-")
                print(str(iPosition4) + '|' + str(iPosition5) + '|' + str(iPosition6))
                print("-+-+-")
                print(str(iPosition7) + '|' + str(iPosition8) + '|' + str(iPosition9))
                if cPlayerMark == "X":
                    print("Player 1 has won the game!")
                else:
                    print("Player 2 has won the game")
                bGameWon = True
            elif iPosition1 == cPlayerMark and iPosition5 == cPlayerMark and iPosition9 == cPlayerMark:
                print(str(iPosition1) + '|' + str(iPosition2) + '|' + str(iPosition3))
                print("-+-+-")
                print(str(iPosition4) + '|' + str(iPosition5) + '|' + str(iPosition6))
                print("-+-+-")
                print(str(iPosition7) + '|' + str(iPosition8) + '|' + str(iPosition9))
                if cPlayerMark == "X":
                    print("Player 1 has won the game!")
                else:
                    print("Player 2 has won the game")
                bGameWon = True
            elif iPosition4 == cPlayerMark and iPosition5 == cPlayerMark and iPosition6 == cPlayerMark:
                print(str(iPosition1) + '|' + str(iPosition2) + '|' + str(iPosition3))
                print("-+-+-")
                print(str(iPosition4) + '|' + str(iPosition5) + '|' + str(iPosition6))
                print("-+-+-")
                print(str(iPosition7) + '|' + str(iPosition8) + '|' + str(iPosition9))
                if cPlayerMark == "X":
                    print("Player 1 has won the game!")
                else:
                    print("Player 2 has won the game")
                bGameWon = True
            elif iPosition7 == cPlayerMark and iPosition8 == cPlayerMark and iPosition9 == cPlayerMark:
                print(str(iPosition1) + '|' + str(iPosition2) + '|' + str(iPosition3))
                print("-+-+-")
                print(str(iPosition4) + '|' + str(iPosition5) + '|' + str(iPosition6))
                print("-+-+-")
                print(str(iPosition7) + '|' + str(iPosition8) + '|' + str(iPosition9))
                if cPlayerMark == "X":
                    print("Player 1 has won the game!")
                else:
                    print("Player 2 has won the game")
                bGameWon = True
            elif iPosition2 == cPlayerMark and iPosition5 == cPlayerMark and iPosition8 == cPlayerMark:
                print(str(iPosition1) + '|' + str(iPosition2) + '|' + str(iPosition3))
                print("-+-+-")
                print(str(iPosition4) + '|' + str(iPosition5) + '|' + str(iPosition6))
                print("-+-+-")
                print(str(iPosition7) + '|' + str(iPosition8) + '|' + str(iPosition9))
                if cPlayerMark == "X":
                    print("Player 1 has won the game!")
                else:
                    print("Player 2 has won the game")
                bGameWon = True
            elif iPosition3 == cPlayerMark and iPosition6 == cPlayerMark and iPosition9 == cPlayerMark:
                print(str(iPosition1) + '|' + str(iPosition2) + '|' + str(iPosition3))
                print("-+-+-")
                print(str(iPosition4) + '|' + str(iPosition5) + '|' + str(iPosition6))
                print("-+-+-")
                print(str(iPosition7) + '|' + str(iPosition8) + '|' + str(iPosition9))
                if cPlayerMark == "X":
                    print("Player 1 has won the game!")
                else:
                    print("Player 2 has won the game")
                bGameWon = True
            elif iPosition7 == cPlayerMark and iPosition5 == cPlayerMark and iPosition3 == cPlayerMark:
                print(str(iPosition1) + '|' + str(iPosition2) + '|' + str(iPosition3))
                print("-+-+-")
                print(str(iPosition4) + '|' + str(iPosition5) + '|' + str(iPosition6))
                print("-+-+-")
                print(str(iPosition7) + '|' + str(iPosition8) + '|' + str(iPosition9))
                if cPlayerMark == "X":
                    print("Player 1 has won the game!")
                else:
                    print("Player 2 has won the game")
                bGameWon = True
            elif iPosition1 != 1 and\
                 iPosition2 != 2 and\
                 iPosition3 != 3 and\
                 iPosition4 != 4 and\
                 iPosition5 != 5 and\
                 iPosition6 != 6 and\
                 iPosition7 != 7 and\
                 iPosition8 != 8 and\
                 iPosition9 != 9:
                print("There was a draw!")
                bGameWon = True

            #  Next Turn
            if bMarkValidation == True:
                if iPlayerTurn == 1:
                    iPlayerTurn = 2
                else:
                    iPlayerTurn = 1
            bInputCheck = False

        sNewGame = input("Would you like to play a new game? (Yes/No)")
        if sNewGame == "No":
            print("Thank you for playing!")
            bNewGame = True
        elif sNewGame == "Yes":
            iPosition1 = 1
            iPosition2 = 2
            iPosition3 = 3
            iPosition4 = 4
            iPosition5 = 5
            iPosition6 = 6
            iPosition7 = 7
            iPosition8 = 8
            iPosition9 = 9
            iPlayerTurn = 1
            iPlayerInput = ""
            cPlayerMark = ""
            sNewGame = ""
            bMarkValidation = False
            bGameWon = False
            bInputCheck = False
            bNewGame = False