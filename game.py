import random

numlist = [0 , 5, 10, 15, 20]

machineScore = 0
playerScore = 0

def welcome():
    print("Welcome to the four hands guessing game!")
    print("Would you like to start guessing first, or would you like me to start?")
    beginGame()

def machineGame():
    print("Great! I will start this round.")
    randomTotal = random.choice(numlist)
    if randomTotal == 0:
        randomX = 0
        randomY = 0
    else:
        randomTotalList = list(range(5, randomTotal+5, 5))
        if len(randomTotalList) == 1:
            randomX = 0
            randomY = 5
        else:
            randomX = randomTotalList[0]
            randomY = randomTotalList[0]
    print("I have made my guess.")

    userHand1 = int(input("What is the value of your first hand? Enter 0 or 5 here: "))


    while userHand1 != 0 and userHand1 != 5:
        print("Your hand must be valid!")
        userHand1 = int(input("What is the value of your first hand? Enter 0 or 5 here: "))

    userHand2 = int(input("What is the value of your second hand? Enter 0 or 5 here: "))

    while userHand2 != 0 and userHand2 != 5:
        print("Your hand must be valid!")
        userHand2 = int(input("What is the value of your first hand? Enter 0 or 5 here: "))

    total = randomX + randomY + userHand1 + userHand2
    print("My hands are " + str(randomX) + " and " + str(randomY) + ".")
    print("Your hands are " + str(userHand1) + ' and ' + str(userHand2) + ".")
    print("Our total is " + str(total) + ".")
    print("My guess was " + str(randomTotal) + ".")
    if total == randomTotal:
        print("I guessed correctly, so I win this round!")
        global machineScore
        global playerScore
        machineScore = machineScore + 1
        print("Computer: " + str(machineScore) + " Player: " + str(playerScore))
        response = int(input("Would you like to play again? 1 = Yes, 2 = No "))

        while response != 1 and response != 2:
            print("Please enter a valid number: ")
            response = int(input("Would you like to play again? 1 = Yes, 2 = No "))
        if response == 1:
                humanGame()
        elif response == 2:
            print("Thanks for playing!")
            exit()

    else:
        print("Ok, your turn!")
        humanGame()

def humanGame():
    print("Alright, you will start this round.")
    randomTotal = random.choice(numlist)
    if randomTotal == 0:
        randomX = 0
        randomY = 0
    else:
        randomTotalList = list(range(5, randomTotal+5, 5))
        if len(randomTotalList) == 1:
            randomX = 0
            randomY = 5
        else:
            randomX = randomTotalList[0]
            randomY = randomTotalList[0]
    userHand1 = int(input("What is the value of your first hand? Enter 0 or 5 here: "))

    while userHand1 != 0 and userHand1 != 5:
        print("Your hand must be valid!")
        userHand1 = int(input("What is the value of your first hand? Enter 0 or 5 here: "))

    userHand2 = int(input("What is the value of your second hand? Enter 0 or 5 here: "))

    while userHand2 != 0 and userHand2 != 5:
        print("Your hand must be valid!")
        userHand2 = int(input("What is the value of your second hand? Enter 0 or 5 here: "))

    userTotal = int(input("What is your guess of the total value? Enter here: "))

    while userTotal < userHand1 + userHand2:
        print("Your total value must be greater or equal to the sum of your hands!")
        userTotal = int(input("What is your guess of the total value? Enter here: "))
    while userTotal not in [0, 5, 10, 15, 20]:
        print("Your hand must be valid!")
        userTotal = int(input("What is your guess of the total value? Enter here: "))

    total = randomX + randomY + userHand1 + userHand2
    print("My hands are " + str(randomX) + " and " + str(randomY) + ".")
    print("Your hands are " + str(userHand1) + ' and ' + str(userHand2) + ".")
    print("Our total is " + str(total) + ".")
    print("Your guess was " + str(userTotal) + ".")
    if total == userTotal:
        print("Good guess! You win this round!")
        global machineScore
        global playerScore
        playerScore = playerScore + 1
        print("Computer: " + str(machineScore) + " Player: " + str(playerScore))

        response = int(input("Would you like to play again? 1 = Yes, 2 = No "))

        while response != 1 and response != 2:
            print("Please enter a valid number: ")
            response = int(input("Would you like to play again? 1 = Yes, 2 = No "))
        if response == 1:
            machineGame()
        elif response == 2:
            print("Thanks for playing!")
            exit()

    else:
        print("Alright, my turn!")
        machineGame()

def beginGame():
    var = int(input("Please type 1 for me to start, and type 2 if you would like to go first: "))
    if var == 1:
        machineGame()
    elif var == 2:
        humanGame()
    else:
        print("Please try to input a valid response, 1 or 2.")
        beginGame()

welcome()
