import time

def Inverse(sUserWord):
    iUserWordCharacterCount = len(sUserWord) - 1 # get last array index
    sUserInvertedWordList = list() #The list of the inverted word
    sUserInvertedWord = "" #The final inverted word

    for l in range(iUserWordCharacterCount,-1,-1): #l is [3]
        #print(sUserWord[l])
        sUserInvertedWordList.extend(sUserWord[l])

    sUserInvertedWord = "".join(sUserInvertedWordList)
    #print(sUserInvertedWord)
    return(sUserInvertedWord)


if __name__ == '__main__':
    # sUserWord: Word that the user inputs
    # iUserWordCharacterCount: The count of the characters
    # sUserInvertedWord: Inverts the word of the user
    # iUserSentenceListCount: Counts the number of items in the list
    # sUserSentenceOldList: The string presented as a list
    # sUserSentenceNewList: New string presented as a list
    # sUserSentenceNewWord


    sUserWord = input("Please enter a word \n") # get input, sUser Word is normal word
    sUserNewSentenceList = list()
    sUserSentenceNewWord = str()
    sUserOldSentenceList = sUserWord.split(" ")
    iUserSentenceListCount = len(sUserOldSentenceList) - 1

    for x in range(iUserSentenceListCount, -1, -1):
        sUserNewSentenceList.extend(Inverse(sUserOldSentenceList[x]))
        sUserNewSentenceList.extend(" ")


    sUserSentenceNewWord = "".join(sUserNewSentenceList)
    print(sUserSentenceNewWord)