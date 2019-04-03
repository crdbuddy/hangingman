import random
HANGMAN_PICS = ['''我的状态：很高兴''', '''我的状态：高兴''','''我的状态：低落''','''我的状态：恐慌''','''我的状态：死亡''']

words = "today happy teacher wonderful school holiday homework coffee ".split()

def getRandomWord(wordList):
    wordIndex = random.randint(0, len(words) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print("尝试过的字符:", end= "")

    for letter in missedLetters:
        print(letter, end = " ")
    print()

    blanks = "0" * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=" ")
    print()

def getGuess(alreadyGuessed):
    while True:
        print("猜一个字母吧。")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("只输入一个字符。")
        elif guess in alreadyGuessed:
            print("你已经猜过了这个字符。")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("请只输入字母。")
        else:
            return guess

def playAgain():
    print("再玩一次？（y/n）")
    return input().lower().startswith('y')


print("恐怖字符游戏")
missedLetters = ""
correctLetters = ""
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print(f"恭喜你，你已经找到了 '{secretWord}' 这个秘密了！")
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMAN_PICS) -1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print("你的竞猜已经完毕！\n经过 " + str(len(missedLetters)) + ' 次竞猜有 ' + str(len(correctLetters)) + ' 次才对, 答案是 "' + secretWord + '"')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ""
            correctLetters = ""
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
