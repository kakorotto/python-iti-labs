# Your game generates a random number and give only 10 tries for the user to guess that number.
# Get the user input and compare it with the random number.
# Display a hint message to the user in case the user number is smaller or bigger than the random number.
# If the user typed a number out of range(100), display a message that is not allowed and don’t count this as a try.
# if the user typed a number that has been entered before, display a hint message and don’t count this as a try also.
# In case the user entered a correct number within the 10 tries, display a congratulations message and let your
# application guess another random number with the remain number of tries.
# If the user finished his all tries, display a message to ask him if he want to play a gain or not.
# Next time the user open the game , he receives a welcome message tells him the number of games he played, how
# many times he won and how many he lost.

import random
score=0
rand=random.randint(0,100)

games=0
wins=0
lose=0
score=0

def fileRead():
    openFile = open("file.txt", "r")
    readFile=openFile.readline()
    fileValues=readFile.split(",")
    games = fileValues[0]
    wins = fileValues[1]
    lose = fileValues[2]
    score = int(wins) - int(lose)
    openFile.close()

def fileWrite(games, wins, lose):
    line = [str(games),",",str(wins),",",str(lose)]
    openFile = open("file.txt", "w")
    openFile.writelines(line)
    openFile.close()

def printScores():
    print("Score: ", score)
    print("Win: ", wins)
    print("Lose: ", lose)
    print("Total Games: ", games)

def winner():
    print("You won!")
    global score
    score += 1
    global wins
    wins += 1
    global games
    games += 1
    global lose
    fileWrite(games, wins, lose)

def loser():
    print("You Lost!")
    global score
    if score > 0:
        score -= 1
    global lose
    lose += 1
    global games
    games += 1
    global wins
    fileWrite(games, wins, lose)

    print("Score: ", score)
    print("Win: ", wins)
    print("Lose: ", lose)
    print("Games: ", games)

def checkRestart():
    restart = input("Do you want to play again? (y/n) ")
    if restart == "y":
        global rand
        rand=random.randint(0,100)
        startGame(10)
        return True
    else:
        print("Thanks for playing!")
        return False

def startGame(try_number):
    print(rand)
    i = try_number
    while i > 0:
        num = input("Guess a number between 0 and 100: ")
        print(num)
        if num.isdecimal():
            guess = (int)(num)
            if guess == rand:
                winner()
                printScores()
                if checkRestart():
                    return
                break
            elif guess > rand:
                print("The number you've guessed is higher the accurate!")
                i -= 1
            elif guess < rand:
                print("The number you've guessed is lower the accurate!")
                i -= 1
        else:
            print("That's not a number!")
            i -= 1

    loser()
    # printScores()
    if checkRestart():
        return

startGame(10)