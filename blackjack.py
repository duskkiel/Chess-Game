from carddeck import Deck
import time

print("Welcome to Blackjack!")


def main():
    deck = Deck()

    # Define how many players are playing
    playerNum = eval(input("How many players do you want to play with? (1-5): "))
    playerMoney = []
    for i in range(playerNum):
        playerMoney.append(100)
    print("Number of Players: " + str(playerNum))
    done = False
    while done is False:
        numList = 1

        # Define the bets for each player
        playerBets = []
        for i in range(playerNum):
            betAmount = eval(
                input("\nTotal: $" + str(playerMoney[i]) + "\nHow much does Player " + str(numList) + " want to bet: "))
            while betAmount > playerMoney[i]:
                print("Not enough funds.")
                betAmount = eval(input("How much does Player " + str(numList) + " want to bet: "))
            while betAmount < 5 and playerMoney[i] >= 5:
                print("Minimum bet is $5.")
                betAmount = eval(input("How much does Player " + str(numList) + " want to bet: "))
            if betAmount >= 5 or playerMoney[i] < 5:
                playerBets.append(betAmount)
                numList += 1

        numList = 1
        print("")
        for i in range(playerNum):
            print("Player " + str(numList) + " Amount: $" + str(playerMoney[i]) + "\n" +
                  "   Bet Amount: $" + str(playerBets[i]))
            numList += 1
        time.sleep(1)

        # Shuffle Deck and deal cards to players and dealer
        deck.shuffle()
        print("\n" + "-Deck Shuffled-" + "\n")
        tableCards = []
        secretCard = []
        for i in range(playerNum + 1):
            tableCards.append([])
        for i in range(playerNum + 1):
            tableCards[i].append(deck.draw())
        for i in range(playerNum):
            tableCards[i].append(deck.draw())
        secretCard.append(deck.draw())
        print("Cards On the Table: ")
        numList = 1
        for i in range(playerNum + 1):
            print("   " + str(numList) + " - " + str(tableCards[i]))
            numList += 1
        print("(Dealer's 2nd Card is present, just flipped over.)")
        print("")

        # Players Hit or Stand
        handValueList = []
        turnDone = False
        playerTurn = 0
        while turnDone is False:
            print("\nPlayer " + str(playerTurn + 1) + " Hand: " + str(tableCards[playerTurn]))
            handValue = 0
            for i in range(len(tableCards[playerTurn])):
                cardValue = tableCards[playerTurn][i].getCardValue()
                if cardValue > 10:
                    cardValue = 10
                if cardValue == 1 and handValue <= 10:
                    cardValue = 11
                handValue += cardValue
            print("   Total Point Value: " + str(handValue))
            if handValue > 21:
                print("BUST!")
                time.sleep(1)
                handValueList.append(handValue)
                playerTurn += 1
                if playerTurn == playerNum:
                    break
            else:
                action = eval(input("1) Hit \n2) Stand \nChoose an action: "))
                if action == 1:
                    tableCards[playerTurn].append(deck.draw())
                elif action == 2 and playerTurn == (playerNum - 1):
                    handValueList.append(handValue)
                    playerTurn += 1
                    break
                elif action == 2:
                    handValueList.append(handValue)
                    playerTurn += 1

        # Dealer's Turn
        tableCards[-1].append(secretCard.pop())
        print("\nDealer 1st Card: " + str(tableCards[-1][0]))
        time.sleep(1)
        print("Dealer 2nd Card: " + str(tableCards[-1][1]))
        time.sleep(1)
        print("\nDealer Hand: " + str(tableCards[playerTurn]))
        dealerTurn = False
        while dealerTurn is False:
            handValue = 0
            for i in range(len(tableCards[playerTurn])):
                cardValue = tableCards[playerTurn][i].getCardValue()
                if cardValue > 10:
                    cardValue = 10
                if cardValue == 1 and handValue <= 10:
                    cardValue = 11
                handValue += cardValue
            print("   Total Point Value: " + str(handValue) + "\n")
            if handValue < 17:
                print("The dealer draws a card.")
                tableCards[playerTurn].append(deck.draw())
                time.sleep(1)
            elif handValue >= 17 and handValue <= 21:
                print("The dealer holds.\n")
                break
            if handValue > 21:
                print("The dealer BUSTS!\n")
                break
        handValueList.append(handValue)
        time.sleep(1)

        # Compare Hand Values with Dealer Value
        newList = []
        playerComp = 1
        for i in range(len(handValueList) - 1):
            time.sleep(1)
            print("\nPlayer " + str(playerComp) + ": " + str(handValueList[i]))
            print("Dealer: " + str(handValueList[-1]))
            playerComp += 1
            if handValueList[i] < handValueList[-1] and handValueList[-1] <= 21:
                newAmount = playerMoney[i] - playerBets[i]
                newList.append(newAmount)
                print("You lost :(")
            elif handValueList[i] == handValueList[-1] and handValueList[i] <= 21:
                newList.append(playerMoney[i])
                print("Draw. Nothing much happens...")
            elif handValueList[i] > handValueList[-1] and handValueList[i] <= 21:
                newAmount = playerMoney[i] + playerBets[i]
                newList.append(newAmount)
                print("Dang, you won!!!")
            elif handValueList[i] <= 21 and handValueList[-1] > 21:
                newAmount = playerMoney[i] + playerBets[i]
                newList.append(newAmount)
                print("The dealer busted and you were under 21. You Win!!!")
            elif handValueList[i] > 21 and handValueList[-1] <= 21:
                newAmount = playerMoney[i] - playerBets[i]
                newList.append(newAmount)
                print("You busted and the dealer didn't. You Lose.")
            elif handValueList[i] > 21 and handValueList[-1] > 21:
                newAmount = playerMoney[i] - playerBets[i]
                newList.append(newAmount)
                print("You both busted. But you're the player, so you lose.")
            else:
                print("Um...I didn't account for this combination...sorry?")
        print("")
        time.sleep(1)
        playerMoney = newList
        moneyNum = 1
        for i in range(playerNum):
            print("Player " + str(moneyNum) + ": $" + str(playerMoney[i]))
            moneyNum += 1
        for i in range(len(playerMoney)):
            if playerMoney[i] == 0:
                playerMoney[i].pop()

        # Repeat Option
        again = eval(input("\n1) Yes \n2) No \nWould you like to play again?:"))
        if again == 1:
            done = False
        elif again == 2:
            winnerList = ["   Player " + str(i + 1) + " " for i in range(playerNum)]
            print("\nThank you for playing!\n")
            for i in range(len(playerMoney) - 1):
                currMinIndex = i
                for j in range(i + 1, len(playerMoney)):
                    if playerMoney[currMinIndex] < playerMoney[j]:
                        currMinIndex = j
                if currMinIndex != i:
                    playerMoney[i], playerMoney[currMinIndex] = playerMoney[currMinIndex], playerMoney[i]
                    winnerList[i], winnerList[currMinIndex] = winnerList[currMinIndex], winnerList[i]
            print("Final Scores: ")
            for i in range(len(playerMoney)):
                print(winnerList[i] + ": $" + str(playerMoney[i]))
            break


main()
