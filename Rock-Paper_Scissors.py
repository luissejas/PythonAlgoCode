import random

if __name__ == '__main__':
    #bEndScore is the final boolean that determines if it exits the code or not
    #bEndgame is the boolean that ends the game
    #bPlayerWin is the boolean that determines the player win AND the score input
    #cPaper is the character defining the Paper input
    #cRock is the character defining the Rock input
    #cScissors is the character defining the Scissors input
    #cPlayer1Input is Player1's input
    #cPlayer2Input is Player2's input later transferred to AI

    bEndScore = False
    bEndGame = False
    bPlayerWin = False
    bInputCheck = False
    bDrawCheck = False
    bContinuationCheck = False
    sContinuation = ""
    cPlayerInput1 = ""
    cPlayerInput2 = ""
    iPlayerVictory = 0
    iAiVictory = 0

    # Introductory Texts
    print("Welcome to Rock Paper Scissors!")
    print("Here are the rules:")
    print("Rock beats Scissors.")
    print("Scissors beats Paper.")
    print("Paper beats Rock.")
    print("For Rock, type Rock. For Paper type Paper. For Scissors type Scissors.")
    print("______________________________")
    print("The inputs will be displayed in the following form:")
    print(" P1 vs AI")
    print("______________________________")

    while bEndScore == False:
        if bEndGame == False:
            print("Player 1, please choose your play!")
            # Player 1 Input Validation
            while bDrawCheck == False:
                while bInputCheck == False:
                    try:
                        cPlayerInput1 = (str(input())).upper()
                        if cPlayerInput1 == 'PAPER' or cPlayerInput1 == 'SCISSORS' or cPlayerInput1 == 'ROCK':
                            bInputCheck = True
                        else:
                            print("Invalid input. Please try again!")
                            bInputCheck = False
                    except ValueError:
                        print("Wrong input, please read the instructions carefully!")

                #AI input
                cPlayerInput2 = str(random.randint(1, 3))
                dAiDictionary = {
                    '1': 'ROCK',
                    '2': 'PAPER',
                    '3': 'SCISSORS'
                }
                # Display of Results
                print(str("(Player1)" + " vs " + "(AI)"))
                print(str(cPlayerInput1) + " vs " + str(dAiDictionary[cPlayerInput2]))

                #Draw Conditions
                if cPlayerInput1 == (dAiDictionary[cPlayerInput2]):
                    print("Draw! You will restart the round!")
                    print("Player 1! Please choose your play!")
                    bDrawCheck = False
                    bInputCheck = False
                else:
                    bDrawCheck = True
            #Winning Conditions
            if cPlayerInput1 == 'ROCK':
                if dAiDictionary[cPlayerInput2] == 'SCISSORS':
                    print("Player 1 has won this round!")
                    iPlayerVictory = iPlayerVictory + 1
                else:
                    print("AI has won this round!")
                    iAiVictory = iAiVictory + 1

            if cPlayerInput1 == 'SCISSORS':
                if dAiDictionary[cPlayerInput2] == 'PAPER':
                    print("Player 1 has won this round!")
                    iPlayerVictory = iPlayerVictory + 1
                else:
                    print("AI has won this round!")
                    iAiVictory = iAiVictory + 1

            if cPlayerInput1 == 'PAPER':
                if dAiDictionary[cPlayerInput2] == 'ROCK':
                    print("Player 1 has won this round!")
                    iPlayerVictory = iPlayerVictory + 1
                else:
                    print("AI has won this round!")
                    iAiVictory = iAiVictory + 1

            print("Current score is (Player 1 - AI):")
            print(str(iPlayerVictory) + " - " + str(iAiVictory))

            #Continuation Check
            while bContinuationCheck == False:
                try:
                    sContinuation = str(input("Do you wish to continue playing? (Y/N)\n")).upper()
                    if sContinuation == 'Y' or sContinuation == 'N':
                        bContinuationCheck = True
                    else:
                        print("Invalid Answer, please input a correct answer!")
                except ValueError:
                    print("Invalid Answer, please input a correct answer!")

            #Action depending on Continuation Choice
            if sContinuation == 'Y':
                bEndScore = False
                bEndGame = False
                bPlayerWin = False
                bInputCheck = False
                bDrawCheck = False
                bContinuationCheck = False
                sContinuation = ""
                cPlayerInput1 = ""
                cPlayerInput2 = ""

            elif sContinuation == 'N':
                print("Thank you for playing the application will now exit!")
                bEndGame = True
                bEndScore = True