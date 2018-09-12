import random

def hangman(word):
    wrong = 1
    stages = ["",
              "________         ",
              "|                ",
              "|       |        ",
              "|       O        ",
              "|      /|)       ",
              "|      / )       ",
              "|                "]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman!")

    while win == False:
        ans = input("\nEnter a letter: ")
    
        if ans in rletters:
            index = rletters.index(ans)
            board[index] = ans
            rletters[index] = "$"
        else:
            wrong += 1

        """
        for i in board:
            print(i, end = "")
        """

        print("".join(board))

        """
        for stage in range(wrong):
            print(stages[stage])
        """

        print("\n".join(stages[0:wrong]))
        
        if "_" not in board:
            win = True
            break
        if wrong == len(stages):
            break

    if win == True:
        print("\nCongratulations!")

    else:
        print("\nHung! The answer was \"{}\".".format(word))


word_list = ["apple", "yuki", "dog", "picture", "kitchen", "rose", "rabbit"]
random_word = word_list[random.randint(0, len(word_list) - 1)]
hangman(random_word)




