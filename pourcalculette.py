import random
import time


def debug(whattodebug):
    print("\u001b[31;1m(⚠️Debug⚠️)\u001b[0m " + whattodebug + " \u001b[31;1m(⚠️Debug⚠️)\u001b[0m")


# Basic Tasks
askWhichGameStarted = False

while not askWhichGameStarted:
    askWhichGame = input("What game do you want to play :\n   1 -> TikTakToe\n   2 -> Dame (Not finished)\n   3 -> Chess (Not finished)\n\nAnswer : ")
    if askWhichGame == str(1):
        ######
        askWhichGameStarted = True
        ######

        started = False
        isPlaying = True
        player = "X"
        move = "NONE"

        # 1000000000 = used for X / 1000000001 = used for O
        availableMoves = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        panel = "\n   0 | 1 | 2  \n  ---+---+--- \n   3 | 4 | 5  \n  ---+---+--- \n   6 | 7 | 8  "
        doesComputPlay = False
        playWithComputDataAnswer = "NONE"
        playerHasPlayed = False
        computerHasPlayed = False
        errorForComput = random.choice(seq=(2, 3, 4))
        toErrorForComput = 0


        def fireWork():
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("   •")
            time.sleep(0.5)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("  \\|/\n  — —\n  /|\\")
            time.sleep(0.5)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(" \\ | /\n\n —   —\n\n / | \\")
            time.sleep(0.5)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


        print("\nBonjour bienvenue\n sur le MorPion \n   du genie\n   (Ulysse)")

        start = input("\n  Voulez vous\n  commencer ?\n  -----------\n     ")

        if "oui" in start:
            playWithComputDataAnswer = input(" Jouer contre\n l'ordinateur ?\n  -----------\n     ")
            if playWithComputDataAnswer == "oui":
                doesComputPlay = True
            else:
                pass

            started = True
        else:
            print("\n  Au revoir !!!")

        while started:
            while isPlaying:
                if not doesComputPlay:
                    move = input(panel + "\n\n Quel mouvement\n      (" + player + ")\n-----------------\n       ")

                elif not playerHasPlayed:
                    move = input(panel + "\n\n Quel mouvement\n      (X)\n-----------------\n       ")
                    if int(move) in availableMoves:
                        playerHasPlayed = True
                        computerHasPlayed = False

                elif not computerHasPlayed:
                    if toErrorForComput == errorForComput:
                        errorForComput = random.choice(seq=(2, 3, 4))
                        toErrorForComput = 0

                        move = str(random.choice(seq=(0, 1, 2, 3, 4, 5, 6, 7, 8)))
                        if int(move) in availableMoves:
                            toErrorForComput = toErrorForComput + 1
                            computerHasPlayed = True
                            playerHasPlayed = False

                    elif availableMoves[0] == 1000000000 and availableMoves[1] == 1000000000 and \
                            availableMoves[2] != 1000000001 and availableMoves[2] != 1000000000:
                        move = "2"
                        if int(move) in availableMoves:
                            toErrorForComput = toErrorForComput + 1
                            computerHasPlayed = True
                            playerHasPlayed = False

                    elif availableMoves[1] == 1000000000 and availableMoves[2] == 1000000000 and \
                            availableMoves[0] != 1000000001 and availableMoves[0] != 1000000000:
                        move = "0"
                        if int(move) in availableMoves:
                            toErrorForComput = toErrorForComput + 1
                            computerHasPlayed = True
                            playerHasPlayed = False

                    elif availableMoves[3] == 1000000000 and availableMoves[4] == 1000000000 and \
                            availableMoves[5] != 1000000001 and availableMoves[5] != 1000000000:
                        move = "5"
                        if int(move) in availableMoves:
                            toErrorForComput = toErrorForComput + 1
                            computerHasPlayed = True
                            playerHasPlayed = False

                    elif availableMoves[5] == 1000000000 and availableMoves[4] == 1000000000 and \
                            availableMoves[3] != 1000000001 and availableMoves[3] != 1000000000:
                        move = "3"
                        if int(move) in availableMoves:
                            toErrorForComput = toErrorForComput + 1
                            computerHasPlayed = True
                            playerHasPlayed = False

                    elif availableMoves[6] == 1000000000 and availableMoves[7] == 1000000000 and \
                            availableMoves[8] != 1000000001 and availableMoves[8] != 1000000000:
                        move = "8"
                        if int(move) in availableMoves:
                            toErrorForComput = toErrorForComput + 1
                            computerHasPlayed = True
                            playerHasPlayed = False

                    elif availableMoves[8] == 1000000000 and availableMoves[7] == 1000000000 and \
                            availableMoves[6] != 1000000001 and availableMoves[6] != 1000000000:
                        move = "6"
                        if int(move) in availableMoves:
                            toErrorForComput = toErrorForComput + 1
                            computerHasPlayed = True
                            playerHasPlayed = False

                    elif availableMoves[0] == 1000000000 and availableMoves[4] == 1000000000 and \
                            availableMoves[8] != 1000000001 and availableMoves[8] != 1000000000:
                        move = "8"
                        if int(move) in availableMoves:
                            toErrorForComput = toErrorForComput + 1
                            computerHasPlayed = True
                            playerHasPlayed = False

                    elif availableMoves[8] == 1000000000 and availableMoves[4] == 1000000000 and \
                            availableMoves[0] != 1000000001 and availableMoves[0] != 1000000000:
                        move = "0"
                        if int(move) in availableMoves:
                            toErrorForComput = toErrorForComput + 1
                            computerHasPlayed = True
                            playerHasPlayed = False

                    elif availableMoves[0] == 1000000000 and availableMoves[3] == 1000000000 and \
                            availableMoves[6] != 1000000001 and availableMoves[6] != 1000000000:
                        move = "6"
                        if int(move) in availableMoves:
                            toErrorForComput = toErrorForComput + 1
                            computerHasPlayed = True
                            playerHasPlayed = False

                    elif availableMoves[6] == 1000000000 and availableMoves[3] == 1000000000 and \
                            availableMoves[0] != 1000000001 and availableMoves[0] != 1000000000:
                        move = "0"
                        if int(move) in availableMoves:
                            toErrorForComput = toErrorForComput + 1
                            computerHasPlayed = True
                            playerHasPlayed = False

                    elif availableMoves[1] == 1000000000 and availableMoves[4] == 1000000000 and \
                            availableMoves[7] != 1000000001 and availableMoves[7] != 1000000000:
                        move = "7"
                        if int(move) in availableMoves:
                            toErrorForComput = toErrorForComput + 1
                            computerHasPlayed = True
                            playerHasPlayed = False

                    elif availableMoves[7] == 1000000000 and availableMoves[4] == 1000000000 and \
                            availableMoves[1] != 1000000001 and availableMoves[1] != 1000000000:
                        move = "1"
                        if int(move) in availableMoves:
                            toErrorForComput = toErrorForComput + 1
                            computerHasPlayed = True
                            playerHasPlayed = False

                    elif availableMoves[2] == 1000000000 and availableMoves[5] == 1000000000 and \
                            availableMoves[8] != 1000000001 and availableMoves[8] != 1000000000:
                        move = "8"
                        if int(move) in availableMoves:
                            toErrorForComput = toErrorForComput + 1
                            computerHasPlayed = True
                            playerHasPlayed = False

                    elif availableMoves[8] == 1000000000 and availableMoves[5] == 1000000000 and \
                            availableMoves[2] != 1000000001 and availableMoves[2] != 1000000000:
                        move = "2"
                        if int(move) in availableMoves:
                            toErrorForComput = toErrorForComput + 1
                            computerHasPlayed = True
                            playerHasPlayed = False

                    elif availableMoves[0] == 1000000000 and availableMoves[2] == 1000000000 and \
                            availableMoves[1] != 1000000001 and availableMoves[1] != 1000000000:
                        move = "1"
                        if int(move) in availableMoves:
                            toErrorForComput = toErrorForComput + 1
                            computerHasPlayed = True
                            playerHasPlayed = False

                    elif availableMoves[3] == 1000000000 and availableMoves[5] == 1000000000 and \
                            availableMoves[4] != 1000000001 and availableMoves[4] != 1000000000:
                        move = "4"
                        if int(move) in availableMoves:
                            toErrorForComput = toErrorForComput + 1
                            computerHasPlayed = True
                            playerHasPlayed = False

                    elif availableMoves[6] == 1000000000 and availableMoves[8] == 1000000000 and \
                            availableMoves[7] != 1000000001 and availableMoves[7] != 1000000000:
                        move = "7"
                        if int(move) in availableMoves:
                            toErrorForComput = toErrorForComput + 1
                            computerHasPlayed = True
                            playerHasPlayed = False

                    elif availableMoves[0] == 1000000000 and availableMoves[6] == 1000000000 and \
                            availableMoves[3] != 1000000001 and availableMoves[3] != 1000000000:
                        move = "3"
                        if int(move) in availableMoves:
                            toErrorForComput = toErrorForComput + 1
                            computerHasPlayed = True
                            playerHasPlayed = False

                    elif availableMoves[1] == 1000000000 and availableMoves[7] == 1000000000 and \
                            availableMoves[4] != 1000000001 and availableMoves[4] != 1000000000:
                        move = "4"
                        if int(move) in availableMoves:
                            toErrorForComput = toErrorForComput + 1
                            computerHasPlayed = True
                            playerHasPlayed = False

                    elif availableMoves[2] == 1000000000 and availableMoves[8] == 1000000000 and \
                            availableMoves[5] != 1000000001 and availableMoves[5] != 1000000000:
                        move = "5"
                        if int(move) in availableMoves:
                            toErrorForComput = toErrorForComput + 1
                            computerHasPlayed = True
                            playerHasPlayed = False

                    elif availableMoves[6] == 1000000000 and availableMoves[4] == 1000000000 and \
                            availableMoves[2] != 1000000001 and availableMoves[2] != 1000000000:
                        move = "2"
                        if int(move) in availableMoves:
                            toErrorForComput = toErrorForComput + 1
                            computerHasPlayed = True
                            playerHasPlayed = False

                    elif availableMoves[6] == 1000000000 and availableMoves[2] == 1000000000 and \
                            availableMoves[4] != 1000000001 and availableMoves[4] != 1000000000:
                        move = "4"
                        if int(move) in availableMoves:
                            toErrorForComput = toErrorForComput + 1
                            computerHasPlayed = True
                            playerHasPlayed = False

                    elif availableMoves[0] == 1000000000 and availableMoves[8] == 1000000000 and \
                            availableMoves[4] != 1000000001 and availableMoves[4] != 1000000000:
                        move = "4"
                        if int(move) in availableMoves:
                            toErrorForComput = toErrorForComput + 1
                            computerHasPlayed = True
                            playerHasPlayed = False

                    elif availableMoves[8] == 1000000000 and availableMoves[4] == 1000000000 and \
                            availableMoves[0] != 1000000001 and availableMoves[0] != 1000000000:
                        move = "0"
                        if int(move) in availableMoves:
                            toErrorForComput = toErrorForComput + 1
                            computerHasPlayed = True
                            playerHasPlayed = False

                    elif availableMoves[6] == 1000000000 and availableMoves[2] == 1000000000 and \
                            availableMoves[4] != 1000000001 and availableMoves[4] != 1000000000:
                        move = "4"
                        if int(move) in availableMoves:
                            toErrorForComput = toErrorForComput + 1
                            computerHasPlayed = True
                            playerHasPlayed = False

                    else:
                        move = str(random.choice(seq=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)))
                        if int(move) in availableMoves:
                            toErrorForComput = toErrorForComput + 1
                            computerHasPlayed = True
                            playerHasPlayed = False

                if int(move) in availableMoves:
                    if player == "X":
                        availableMoves[int(move)] = 1000000000
                    elif player == "O":
                        availableMoves[int(move)] = 1000000001

                    panel = panel.replace(str(move), player)

                    if player == "X":
                        player = "O"
                    elif player == "O":
                        player = "X"

                    # Detects if win Horizontal axis
                    if "X | X | X" in panel or "O | O | O" in panel:

                        if player == "X":
                            player = "O"
                        elif player == "O":
                            player = "X"

                        print("\n\n\n\n\n\n\n\n    You WON\n   Player (" + player + ")")
                        print(panel)

                        time.sleep(2)
                        fireWork()
                        fireWork()
                        fireWork()
                        fireWork()
                        fireWork()

                        isPlaying = False
                        started = False

                    # Detects if win on Vertical axis
                    elif availableMoves[0] == 1000000000 and availableMoves[3] == 1000000000 and availableMoves[
                        6] == 1000000000 or availableMoves[0] == 1000000001 and availableMoves[3] == 1000000001 and \
                            availableMoves[6] == 1000000001:

                        if player == "X":
                            player = "O"
                        elif player == "O":
                            player = "X"

                        print("\n\n\n\n\n\n\n\n    You WON\n   Player (" + player + ")")
                        print(panel)

                        time.sleep(2)
                        fireWork()
                        fireWork()
                        fireWork()
                        fireWork()
                        fireWork()

                        isPlaying = False
                        started = False

                    elif availableMoves[1] == 1000000000 and availableMoves[4] == 1000000000 and availableMoves[
                        7] == 1000000000 or availableMoves[1] == 1000000001 and availableMoves[4] == 1000000001 and \
                            availableMoves[7] == 1000000001:

                        if player == "X":
                            player = "O"
                        elif player == "O":
                            player = "X"

                        print("\n\n\n\n\n\n\n\n    You WON\n   Player (" + player + ")")
                        print(panel)

                        time.sleep(2)
                        fireWork()
                        fireWork()
                        fireWork()
                        fireWork()
                        fireWork()

                        isPlaying = False
                        started = False

                    elif availableMoves[2] == 1000000000 and availableMoves[5] == 1000000000 and availableMoves[
                        8] == 1000000000 or availableMoves[2] == 1000000001 and availableMoves[5] == 1000000001 and \
                            availableMoves[8] == 1000000001:

                        if player == "X":
                            player = "O"
                        elif player == "O":
                            player = "X"

                        print("\n\n\n\n\n\n\n\n    You WON\n   Player (" + player + ")")
                        print(panel)

                        time.sleep(2)
                        fireWork()
                        fireWork()
                        fireWork()
                        fireWork()
                        fireWork()

                        isPlaying = False
                        started = False

                    # Detects if win on Diagonal axis (Left to Right)
                    elif availableMoves[0] == 1000000000 and availableMoves[4] == 1000000000 and availableMoves[
                        8] == 1000000000 or availableMoves[0] == 1000000001 and availableMoves[4] == 1000000001 and \
                            availableMoves[8] == 1000000001:

                        if player == "X":
                            player = "O"
                        elif player == "O":
                            player = "X"

                        print("\n\n\n\n\n\n\n\n    You WON\n   Player (" + player + ")")
                        print(panel)

                        time.sleep(2)
                        fireWork()
                        fireWork()
                        fireWork()
                        fireWork()
                        fireWork()

                        isPlaying = False
                        started = False

                    # Detects if win on Diagonal axis (Right to left)
                    elif availableMoves[2] == 1000000000 and availableMoves[4] == 1000000000 and availableMoves[
                        6] == 1000000000 or availableMoves[2] == 1000000001 and availableMoves[4] == 1000000001 and \
                            availableMoves[6] == 1000000001:

                        if player == "X":
                            player = "O"
                        elif player == "O":
                            player = "X"

                        print("\n\n\n\n\n\n\n\n    You WON\n   Player (" + player + ")")
                        print(panel)

                        time.sleep(2)
                        fireWork()
                        fireWork()
                        fireWork()
                        fireWork()
                        fireWork()

                        isPlaying = False
                        started = False

                    # Detects if TIE
                    elif availableMoves[0] != 0 and availableMoves[1] != 1 and availableMoves[2] != 2 and \
                            availableMoves[
                                3] != 3 and availableMoves[4] != 4 and availableMoves[5] != 5 and availableMoves[
                        6] != 6 and \
                            availableMoves[7] != 7 and availableMoves[8] != 8:
                        print("\n\n\n\n\n\n\n\n     TIE")
                        print(panel)

                        isPlaying = False
                        started = False

                    else:
                        pass
    # Ulysse si tu ouvre ça c'est pas drôle.

    elif askWhichGame == str(2):

        ######
        askWhichGameStarted = True
        ######

        whosPlaying = "W"

        finished = False

        damePanelA = ["\u001b[31;1mB \u001b[0m", "1A", "\u001b[31;1mB \u001b[0m", "3A", "\u001b[31;1mB \u001b[0m", "5A", "\u001b[31;1mB \u001b[0m", "7A", "\u001b[31;1mB \u001b[0m", "9A"]
        damePanelB = ["0B", "\u001b[31;1mB \u001b[0m", "2B", "\u001b[31;1mB \u001b[0m", "4B", "\u001b[31;1mB \u001b[0m", "6B", "\u001b[31;1mB \u001b[0m", "8B", "\u001b[31;1mB \u001b[0m"]
        damePanelC = ["\u001b[31;1mB \u001b[0m", "1C", "\u001b[31;1mB \u001b[0m", "3C", "\u001b[31;1mB \u001b[0m", "5C", "\u001b[31;1mB \u001b[0m", "7C", "\u001b[31;1mB \u001b[0m", "9C"]
        damePanelD = ["0D", "\u001b[31;1mB \u001b[0m", "2D", "\u001b[31;1mB \u001b[0m", "4D", "\u001b[31;1mB \u001b[0m", "6D", "\u001b[31;1mB \u001b[0m", "8D", "\u001b[31;1mB \u001b[0m"]
        damePanelE = ["0E", "1E", "2E", "3E", "4E", "5E", "6E", "7E", "8E", "9E"]
        damePanelF = ["0F", "1F", "2F", "3F", "4F", "5F", "6F", "7F", "8F", "9F"]
        damePanelG = ["\u001b[32;1mW \u001b[0m", "1G", "\u001b[32;1mW \u001b[0m", "3G", "\u001b[32;1mW \u001b[0m", "5G", "\u001b[32;1mW \u001b[0m", "7G", "\u001b[32;1mW \u001b[0m", "9G"]
        damePanelH = ["0H", "\u001b[32;1mW \u001b[0m", "2H", "\u001b[32;1mW \u001b[0m", "4H", "\u001b[32;1mW \u001b[0m", "6H", "\u001b[32;1mW \u001b[0m", "8H", "\u001b[32;1mW \u001b[0m"]
        damePanelI = ["\u001b[32;1mW \u001b[0m", "1I", "\u001b[32;1mW \u001b[0m", "3I", "\u001b[32;1mW \u001b[0m", "5I", "\u001b[32;1mW \u001b[0m", "7I", "\u001b[32;1mW \u001b[0m", "9I"]
        damePanelJ = ["0J", "\u001b[32;1mW \u001b[0m", "2J", "\u001b[32;1mW \u001b[0m", "4J", "\u001b[32;1mW \u001b[0m", "6J", "\u001b[32;1mW \u001b[0m", "8J", "\u001b[32;1mW \u001b[0m"]

        lineSeparation = "————+————+————+————+————+————+————+————+————+————\n"

        damePanelAnswerChoosePiece = input(
            " " + damePanelA[0] + " | " + damePanelA[1] + " | " + damePanelA[2] + " | " + damePanelA[3] + " | " +
            damePanelA[
                4] + " | " + damePanelA[5] + " | " + damePanelA[6] + " | " + damePanelA[7] + " | " + damePanelA[
                8] + " | " +
            damePanelA[9] + " " + "\n" + lineSeparation + " " + damePanelB[0] + " | " + damePanelB[1] + " | " +
            damePanelB[2] + " | " + damePanelB[3] + " | " + damePanelB[
                4] + " | " + damePanelB[5] + " | " + damePanelB[6] + " | " + damePanelB[7] + " | " + damePanelB[
                8] + " | " +
            damePanelB[9] + " " + "\n" + lineSeparation + " " + damePanelC[0] + " | " + damePanelC[1] + " | " +
            damePanelC[2] + " | " + damePanelC[3] + " | " + damePanelC[
                4] + " | " + damePanelC[5] + " | " + damePanelC[6] + " | " + damePanelC[7] + " | " + damePanelC[
                8] + " | " +
            damePanelC[9] + " " + "\n" + lineSeparation + " " + damePanelD[0] + " | " + damePanelD[1] + " | " +
            damePanelD[2] + " | " + damePanelD[3] + " | " + damePanelD[
                4] + " | " + damePanelD[5] + " | " + damePanelD[6] + " | " + damePanelD[7] + " | " + damePanelD[
                8] + " | " +
            damePanelD[9] + " " + "\n" + lineSeparation + " " + damePanelE[0] + " | " + damePanelE[1] + " | " +
            damePanelE[2] + " | " + damePanelE[3] + " | " + damePanelE[
                4] + " | " + damePanelE[5] + " | " + damePanelE[6] + " | " + damePanelE[7] + " | " + damePanelE[
                8] + " | " +
            damePanelE[9] + " " + "\n" + lineSeparation + " " + damePanelF[0] + " | " + damePanelF[1] + " | " +
            damePanelF[2] + " | " + damePanelF[3] + " | " + damePanelF[
                4] + " | " + damePanelF[5] + " | " + damePanelF[6] + " | " + damePanelF[7] + " | " + damePanelF[
                8] + " | " +
            damePanelF[9] + " " + "\n" + lineSeparation + " " + damePanelG[0] + " | " + damePanelG[1] + " | " +
            damePanelG[2] + " | " + damePanelG[3] + " | " + damePanelG[
                4] + " | " + damePanelG[5] + " | " + damePanelG[6] + " | " + damePanelG[7] + " | " + damePanelG[
                8] + " | " +
            damePanelG[9] + " " + "\n" + lineSeparation + " " + damePanelH[0] + " | " + damePanelH[1] + " | " +
            damePanelH[2] + " | " + damePanelH[3] + " | " + damePanelH[
                4] + " | " + damePanelH[5] + " | " + damePanelH[6] + " | " + damePanelH[7] + " | " + damePanelH[
                8] + " | " +
            damePanelH[9] + " " + "\n" + lineSeparation + " " + damePanelI[0] + " | " + damePanelI[1] + " | " +
            damePanelI[2] + " | " + damePanelI[3] + " | " + damePanelI[
                4] + " | " + damePanelI[5] + " | " + damePanelI[6] + " | " + damePanelI[7] + " | " + damePanelI[
                8] + " | " +
            damePanelI[9] + " " + "\n" + lineSeparation + " " + damePanelJ[0] + " | " + damePanelJ[1] + " | " +
            damePanelJ[2] + " | " + damePanelJ[3] + " | " + damePanelJ[
                4] + " | " + damePanelJ[5] + " | " + damePanelJ[6] + " | " + damePanelJ[7] + " | " + damePanelJ[
                8] + " | " +
            damePanelJ[9] + " \n\nQuel pion voulez vous bouger (Exemple : 1J) : ")

        bs = 0
        ws = 0

        canIGoTheir = False
        whichColor = "2"

        dameWLock = {"J": "I", "I": "H", "H": "G", "G": "F", "F": "E", "E": "D", "D": "C", "C": "B", "B": "A"}
        dameBLock = {"A": "B", "B": "C", "C": "D", "D": "E", "E": "F", "F": "G", "G": "H", "H": "I", "I": "J"}

        while not finished:

            pionPlaceNumb = damePanelAnswerChoosePiece.join([i for i in damePanelAnswerChoosePiece if i not in ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")])
            pionPlaceLetter = damePanelAnswerChoosePiece.join([i for i in damePanelAnswerChoosePiece if i not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")])

            if damePanelAnswerChoosePiece not in damePanelA and damePanelAnswerChoosePiece not in damePanelB and damePanelAnswerChoosePiece not in damePanelC and damePanelAnswerChoosePiece not in damePanelD and damePanelAnswerChoosePiece not in damePanelE and damePanelAnswerChoosePiece not in damePanelF and damePanelAnswerChoosePiece not in damePanelG and damePanelAnswerChoosePiece not in damePanelH and damePanelAnswerChoosePiece not in damePanelI and damePanelAnswerChoosePiece not in damePanelJ:
                if globals()["damePanel" + pionPlaceLetter][int(pionPlaceNumb)] == "\u001b[3" + whichColor + ";1m" + whosPlaying + " \u001b[0m":
                    damePanelAnswerChoosePiece2 = input("Ou voulez vous allez (Exemple : 1J ou \"change\" pour changer de pion) : ")

                    while not canIGoTheir:
                        whereToPlaceNumb = damePanelAnswerChoosePiece2.join([i for i in damePanelAnswerChoosePiece2 if i not in ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")])
                        whereToPlaceLetter = damePanelAnswerChoosePiece2.join([i for i in damePanelAnswerChoosePiece2 if i not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")])

                        if damePanelAnswerChoosePiece2 == "change":
                            canIGoTheir = True

                        elif whosPlaying == "W":
                            if globals()["damePanel" + whereToPlaceLetter][int(whereToPlaceNumb)] != "\u001b[32;1m" + whosPlaying + " \u001b[0m" and whereToPlaceLetter != pionPlaceLetter:
                                if int(whereToPlaceNumb) == int(pionPlaceNumb) + 1 or int(whereToPlaceNumb) == int(pionPlaceNumb) - 1:
                                    if whereToPlaceLetter == dameWLock[pionPlaceLetter]:
                                        if damePanelAnswerChoosePiece2 in damePanelA and damePanelAnswerChoosePiece2 in damePanelB and damePanelAnswerChoosePiece2 in damePanelC and damePanelAnswerChoosePiece2 in damePanelD and damePanelAnswerChoosePiece2 in damePanelE and damePanelAnswerChoosePiece2 in damePanelF and damePanelAnswerChoosePiece2 in damePanelG and damePanelAnswerChoosePiece2 in damePanelH and damePanelAnswerChoosePiece2 in damePanelI and damePanelAnswerChoosePiece2 in damePanelJ:
                                            globals()["damePanel" + pionPlaceLetter][int(pionPlaceNumb)] = damePanelAnswerChoosePiece
                                            globals()["damePanel" + whereToPlaceLetter][int(whereToPlaceNumb)] = "\u001b[32;1m" + whosPlaying + " \u001b[0m"

                                            if whosPlaying == "W":
                                                whosPlaying = "B"
                                                whichColor = "1"
                                            elif whosPlaying == "B":
                                                whosPlaying = "W"
                                                whichColor = "2"

                                            canIGoTheir = True

                                        else:
                                            globals()["damePanel" + pionPlaceLetter][
                                                int(pionPlaceNumb)] = damePanelAnswerChoosePiece
                                            globals()["damePanel" + whereToPlaceLetter][
                                                int(whereToPlaceNumb)] = "\u001b[32;1m" + whosPlaying + " \u001b[0m"

                                            if whosPlaying == "W":
                                                whosPlaying = "B"
                                                whichColor = "1"
                                            elif whosPlaying == "B":
                                                whosPlaying = "W"
                                                whichColor = "2"

                                            canIGoTheir = True

                                    else:
                                        print("\nVous ne pouvez pas allez la\n")
                                        damePanelAnswerChoosePiece2 = input(
                                            "Ou voulez vous allez (Exemple : 1J ou \"change\" pour changer de pion) : ")
                                        whereToPlaceNumb = damePanelAnswerChoosePiece2.join(
                                            [i for i in damePanelAnswerChoosePiece2 if
                                             i not in ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")])
                                        whereToPlaceLetter = damePanelAnswerChoosePiece2.join(
                                            [i for i in damePanelAnswerChoosePiece2 if
                                             i not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")])

                                else:
                                    print("\nVous ne pouvez pas allez la\n")
                                    damePanelAnswerChoosePiece2 = input(
                                        "Ou voulez vous allez (Exemple : 1J ou \"change\" pour changer de pion) : ")
                                    whereToPlaceNumb = damePanelAnswerChoosePiece2.join(
                                        [i for i in damePanelAnswerChoosePiece2 if
                                         i not in ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")])
                                    whereToPlaceLetter = damePanelAnswerChoosePiece2.join(
                                        [i for i in damePanelAnswerChoosePiece2 if
                                         i not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")])


                            else:
                                print("\nVous ne pouvez pas allez la\n")
                                damePanelAnswerChoosePiece2 = input(
                                    "Ou voulez vous allez (Exemple : 1J ou \"change\" pour changer de pion) : ")
                                whereToPlaceNumb = damePanelAnswerChoosePiece2.join(
                                    [i for i in damePanelAnswerChoosePiece2 if
                                     i not in ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")])
                                whereToPlaceLetter = damePanelAnswerChoosePiece2.join(
                                    [i for i in damePanelAnswerChoosePiece2 if
                                     i not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")])

                        elif whosPlaying == "B":
                            if globals()["damePanel" + whereToPlaceLetter][int(whereToPlaceNumb)] != "\u001b[31;1m" + whosPlaying + " \u001b[0m" and whereToPlaceLetter != pionPlaceLetter:
                                if int(whereToPlaceNumb) == int(pionPlaceNumb) + 1 or int(whereToPlaceNumb) == int(pionPlaceNumb) - 1:
                                    if whereToPlaceLetter == dameBLock[pionPlaceLetter]:
                                        if damePanelAnswerChoosePiece2 in damePanelA and damePanelAnswerChoosePiece2 in damePanelB and damePanelAnswerChoosePiece2 in damePanelC and damePanelAnswerChoosePiece2 in damePanelD and damePanelAnswerChoosePiece2 in damePanelE and damePanelAnswerChoosePiece2 in damePanelF and damePanelAnswerChoosePiece2 in damePanelG and damePanelAnswerChoosePiece2 in damePanelH and damePanelAnswerChoosePiece2 in damePanelI and damePanelAnswerChoosePiece2 in damePanelJ:
                                            globals()["damePanel" + pionPlaceLetter][int(pionPlaceNumb)] = damePanelAnswerChoosePiece
                                            globals()["damePanel" + whereToPlaceLetter][int(whereToPlaceNumb)] = "\u001b[31;1m" + whosPlaying + " \u001b[0m"

                                            if whosPlaying == "W":
                                                whosPlaying = "B"
                                                whichColor = "1"
                                            elif whosPlaying == "B":
                                                whosPlaying = "W"
                                                whichColor = "2"

                                            canIGoTheir = True

                                        else:
                                            globals()["damePanel" + pionPlaceLetter][
                                                int(pionPlaceNumb)] = damePanelAnswerChoosePiece
                                            globals()["damePanel" + whereToPlaceLetter][
                                                int(whereToPlaceNumb)] = "\u001b[31;1m" + whosPlaying + " \u001b[0m"

                                            if whosPlaying == "W":
                                                whosPlaying = "B"
                                                whichColor = "1"
                                            elif whosPlaying == "B":
                                                whosPlaying = "W"
                                                whichColor = "2"
                                            canIGoTheir = True

                                    else:
                                        print("\nVous ne pouvez pas allez la\n")
                                        damePanelAnswerChoosePiece2 = input(
                                            "Ou voulez vous allez (Exemple : 1J ou \"change\" pour changer de pion) : ")
                                        whereToPlaceNumb = damePanelAnswerChoosePiece2.join(
                                            [i for i in damePanelAnswerChoosePiece2 if
                                             i not in ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")])
                                        whereToPlaceLetter = damePanelAnswerChoosePiece2.join(
                                            [i for i in damePanelAnswerChoosePiece2 if
                                             i not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")])

                                else:
                                    print("\nVous ne pouvez pas allez la\n")
                                    damePanelAnswerChoosePiece2 = input(
                                        "Ou voulez vous allez (Exemple : 1J ou \"change\" pour changer de pion) : ")
                                    whereToPlaceNumb = damePanelAnswerChoosePiece2.join(
                                        [i for i in damePanelAnswerChoosePiece2 if
                                         i not in ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")])
                                    whereToPlaceLetter = damePanelAnswerChoosePiece2.join(
                                        [i for i in damePanelAnswerChoosePiece2 if
                                         i not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")])


                            else:
                                print("\nVous ne pouvez pas allez la\n")
                                damePanelAnswerChoosePiece2 = input(
                                    "Ou voulez vous allez (Exemple : 1J ou \"change\" pour changer de pion) : ")
                                whereToPlaceNumb = damePanelAnswerChoosePiece2.join(
                                    [i for i in damePanelAnswerChoosePiece2 if
                                     i not in ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")])
                                whereToPlaceLetter = damePanelAnswerChoosePiece2.join(
                                    [i for i in damePanelAnswerChoosePiece2 if
                                     i not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")])

                elif globals()["damePanel" + pionPlaceLetter][int(pionPlaceNumb)] == "\u001b[3" + whichColor + ";1m♛\u001b[0m":
                    debug("Hey veuilliez utiliser \"change\" les dâmes marches toujours pas !")
                    damePanelAnswerChoosePiece2 = input("Ou voulez vous allez (Exemple : 1J ou \"change\" pour changer de pion) : ")

                    while not canIGoTheir:
                        whereToPlaceNumb = damePanelAnswerChoosePiece2.join([i for i in damePanelAnswerChoosePiece2 if i not in ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")])
                        whereToPlaceLetter = damePanelAnswerChoosePiece2.join([i for i in damePanelAnswerChoosePiece2 if i not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")])

                        if damePanelAnswerChoosePiece2 == "change":
                            canIGoTheir = True

                        elif whosPlaying == "W":
                            if globals()["damePanel" + whereToPlaceLetter][int(whereToPlaceNumb)] != "\u001b[32;1m" + whosPlaying + " \u001b[0m" and whereToPlaceLetter != pionPlaceLetter:
                                if int(whereToPlaceNumb) == int(pionPlaceNumb) + 1 or int(whereToPlaceNumb) == int(pionPlaceNumb) - 1:
                                    if damePanelAnswerChoosePiece2 in damePanelA and damePanelAnswerChoosePiece2 in damePanelB and damePanelAnswerChoosePiece2 in damePanelC and damePanelAnswerChoosePiece2 in damePanelD and damePanelAnswerChoosePiece2 in damePanelE and damePanelAnswerChoosePiece2 in damePanelF and damePanelAnswerChoosePiece2 in damePanelG and damePanelAnswerChoosePiece2 in damePanelH and damePanelAnswerChoosePiece2 in damePanelI and damePanelAnswerChoosePiece2 in damePanelJ:
                                        globals()["damePanel" + pionPlaceLetter][int(pionPlaceNumb)] = damePanelAnswerChoosePiece
                                        globals()["damePanel" + whereToPlaceLetter][int(whereToPlaceNumb)] = "\u001b[32;1m" + whosPlaying + " \u001b[0m"

                                        if whosPlaying == "W":
                                            whosPlaying = "B"
                                            whichColor = "1"
                                        elif whosPlaying == "B":
                                            whosPlaying = "W"
                                            whichColor = "2"

                                        canIGoTheir = True

                                    else:
                                        globals()["damePanel" + pionPlaceLetter][
                                            int(pionPlaceNumb)] = damePanelAnswerChoosePiece
                                        globals()["damePanel" + whereToPlaceLetter][
                                            int(whereToPlaceNumb)] = "\u001b[32;1m" + whosPlaying + " \u001b[0m"

                                        if whosPlaying == "W":
                                            whosPlaying = "B"
                                            whichColor = "1"
                                        elif whosPlaying == "B":
                                            whosPlaying = "W"
                                            whichColor = "2"

                                        canIGoTheir = True

                                else:
                                    print("\nVous ne pouvez pas allez la\n")
                                    damePanelAnswerChoosePiece2 = input(
                                        "Ou voulez vous allez (Exemple : 1J ou \"change\" pour changer de pion) : ")
                                    whereToPlaceNumb = damePanelAnswerChoosePiece2.join(
                                        [i for i in damePanelAnswerChoosePiece2 if
                                         i not in ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")])
                                    whereToPlaceLetter = damePanelAnswerChoosePiece2.join(
                                        [i for i in damePanelAnswerChoosePiece2 if
                                         i not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")])


                            else:
                                print("\nVous ne pouvez pas allez la\n")
                                damePanelAnswerChoosePiece2 = input(
                                    "Ou voulez vous allez (Exemple : 1J ou \"change\" pour changer de pion) : ")
                                whereToPlaceNumb = damePanelAnswerChoosePiece2.join(
                                    [i for i in damePanelAnswerChoosePiece2 if
                                     i not in ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")])
                                whereToPlaceLetter = damePanelAnswerChoosePiece2.join(
                                    [i for i in damePanelAnswerChoosePiece2 if
                                     i not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")])

                        elif whosPlaying == "B":
                            if globals()["damePanel" + whereToPlaceLetter][int(whereToPlaceNumb)] != "\u001b[31;1m" + whosPlaying + " \u001b[0m" and whereToPlaceLetter != pionPlaceLetter:
                                if int(whereToPlaceNumb) == int(pionPlaceNumb) + 1 or int(whereToPlaceNumb) == int(pionPlaceNumb) - 1:
                                    if damePanelAnswerChoosePiece2 in damePanelA and damePanelAnswerChoosePiece2 in damePanelB and damePanelAnswerChoosePiece2 in damePanelC and damePanelAnswerChoosePiece2 in damePanelD and damePanelAnswerChoosePiece2 in damePanelE and damePanelAnswerChoosePiece2 in damePanelF and damePanelAnswerChoosePiece2 in damePanelG and damePanelAnswerChoosePiece2 in damePanelH and damePanelAnswerChoosePiece2 in damePanelI and damePanelAnswerChoosePiece2 in damePanelJ:
                                        globals()["damePanel" + pionPlaceLetter][int(pionPlaceNumb)] = damePanelAnswerChoosePiece
                                        globals()["damePanel" + whereToPlaceLetter][int(whereToPlaceNumb)] = "\u001b[31;1m" + whosPlaying + " \u001b[0m"

                                        if whosPlaying == "W":
                                            whosPlaying = "B"
                                            whichColor = "1"
                                        elif whosPlaying == "B":
                                            whosPlaying = "W"
                                            whichColor = "2"

                                        canIGoTheir = True

                                    else:
                                        globals()["damePanel" + pionPlaceLetter][
                                            int(pionPlaceNumb)] = damePanelAnswerChoosePiece
                                        globals()["damePanel" + whereToPlaceLetter][
                                            int(whereToPlaceNumb)] = "\u001b[31;1m" + whosPlaying + " \u001b[0m"

                                        if whosPlaying == "W":
                                            whosPlaying = "B"
                                            whichColor = "1"
                                        elif whosPlaying == "B":
                                            whosPlaying = "W"
                                            whichColor = "2"
                                        canIGoTheir = True

                                else:
                                    print("\nVous ne pouvez pas allez la\n")
                                    damePanelAnswerChoosePiece2 = input(
                                        "Ou voulez vous allez (Exemple : 1J ou \"change\" pour changer de pion) : ")
                                    whereToPlaceNumb = damePanelAnswerChoosePiece2.join(
                                        [i for i in damePanelAnswerChoosePiece2 if
                                         i not in ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")])
                                    whereToPlaceLetter = damePanelAnswerChoosePiece2.join(
                                        [i for i in damePanelAnswerChoosePiece2 if
                                         i not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")])


                            else:
                                print("\nVous ne pouvez pas allez la\n")
                                damePanelAnswerChoosePiece2 = input(
                                    "Ou voulez vous allez (Exemple : 1J ou \"change\" pour changer de pion) : ")
                                whereToPlaceNumb = damePanelAnswerChoosePiece2.join(
                                    [i for i in damePanelAnswerChoosePiece2 if
                                     i not in ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")])
                                whereToPlaceLetter = damePanelAnswerChoosePiece2.join(
                                    [i for i in damePanelAnswerChoosePiece2 if
                                     i not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")])

                else:
                    print("\nIl n\'y a pas de pions la\n")

            else:
                print("\nIl n\'y a pas de pions la\n")

            bs = damePanelA.count("\u001b[31;1mB \u001b[0m") + damePanelB.count(
                "\u001b[31;1mB \u001b[0m") + damePanelC.count("\u001b[31;1mB \u001b[0m") + damePanelD.count(
                "\u001b[31;1mB \u001b[0m") + damePanelE.count("\u001b[31;1mB \u001b[0m") + damePanelF.count(
                "\u001b[31;1mB \u001b[0m") + damePanelG.count("\u001b[31;1mB \u001b[0m") + damePanelH.count(
                "\u001b[31;1mB \u001b[0m") + damePanelI.count("\u001b[31;1mB \u001b[0m") + damePanelJ.count(
                "\u001b[31;1mB \u001b[0m")
            bs += damePanelA.count("\u001b[31;1m♛\u001b[0m") + damePanelB.count(
                "\u001b[31;1m♛\u001b[0m") + damePanelC.count("\u001b[31;1m♛\u001b[0m") + damePanelD.count(
                "\u001b[31;1m♛\u001b[0m") + damePanelE.count("\u001b[31;1m♛\u001b[0m") + damePanelF.count(
                "\u001b[31;1m♛\u001b[0m") + damePanelG.count("\u001b[31;1m♛\u001b[0m") + damePanelH.count(
                "\u001b[31;1m♛\u001b[0m") + damePanelI.count("\u001b[31;1m♛\u001b[0m") + damePanelJ.count(
                "\u001b[31;1m♛\u001b[0m")

            ws = damePanelA.count("\u001b[32;1mW \u001b[0m") + damePanelB.count(
                "\u001b[32;1mW \u001b[0m") + damePanelC.count("\u001b[32;1mW \u001b[0m") + damePanelD.count(
                "\u001b[32;1mW \u001b[0m") + damePanelE.count("\u001b[32;1mW \u001b[0m") + damePanelF.count(
                "\u001b[32;1mW \u001b[0m") + damePanelG.count("\u001b[32;1mW \u001b[0m") + damePanelH.count(
                "\u001b[32;1mW \u001b[0m") + damePanelI.count("\u001b[32;1mW \u001b[0m") + damePanelJ.count(
                "\u001b[32;1mW \u001b[0m")

            ws += damePanelA.count("\u001b[32;1m♛\u001b[0m") + damePanelB.count(
                "\u001b[31;1m♛\u001b[0m") + damePanelC.count("\u001b[31;1m♛\u001b[0m") + damePanelD.count(
                "\u001b[31;1m♛\u001b[0m") + damePanelE.count("\u001b[31;1m♛\u001b[0m") + damePanelF.count(
                "\u001b[31;1m♛\u001b[0m") + damePanelG.count("\u001b[31;1m♛\u001b[0m") + damePanelH.count(
                "\u001b[31;1m♛\u001b[0m") + damePanelI.count("\u001b[31;1m♛\u001b[0m") + damePanelJ.count(
                "\u001b[31;1m♛\u001b[0m")

            if bs == 0:
                finished = True
            if ws == 0:
                finished = True

            damePanelA = [x.replace("\u001b[32;1mW \u001b[0m", "\u001b[32;1m♛\u001b[0m") for x in damePanelA]
            damePanelJ = [x.replace("\u001b[31;1mB \u001b[0m", "\u001b[31;1m♛\u001b[0m") for x in damePanelJ]

            if not finished:
                damePanelAnswerChoosePiece = input(
                    " " + damePanelA[0] + " | " + damePanelA[1] + " | " + damePanelA[2] + " | " +
                    damePanelA[
                        3] + " | " + damePanelA[
                        4] + " | " + damePanelA[5] + " | " + damePanelA[6] + " | " + damePanelA[7] + " | " +
                    damePanelA[
                        8] + " | " +
                    damePanelA[9] + " " + "\n" + lineSeparation + " " + damePanelB[0] + " | " + damePanelB[
                        1] + " | " +
                    damePanelB[2] + " | " + damePanelB[3] + " | " + damePanelB[
                        4] + " | " + damePanelB[5] + " | " + damePanelB[6] + " | " + damePanelB[7] + " | " +
                    damePanelB[
                        8] + " | " +
                    damePanelB[9] + " " + "\n" + lineSeparation + " " + damePanelC[0] + " | " + damePanelC[
                        1] + " | " +
                    damePanelC[2] + " | " + damePanelC[3] + " | " + damePanelC[
                        4] + " | " + damePanelC[5] + " | " + damePanelC[6] + " | " + damePanelC[7] + " | " +
                    damePanelC[
                        8] + " | " +
                    damePanelC[9] + " " + "\n" + lineSeparation + " " + damePanelD[0] + " | " + damePanelD[
                        1] + " | " +
                    damePanelD[2] + " | " + damePanelD[3] + " | " + damePanelD[
                        4] + " | " + damePanelD[5] + " | " + damePanelD[6] + " | " + damePanelD[7] + " | " +
                    damePanelD[
                        8] + " | " +
                    damePanelD[9] + " " + "\n" + lineSeparation + " " + damePanelE[0] + " | " + damePanelE[
                        1] + " | " +
                    damePanelE[2] + " | " + damePanelE[3] + " | " + damePanelE[
                        4] + " | " + damePanelE[5] + " | " + damePanelE[6] + " | " + damePanelE[7] + " | " +
                    damePanelE[
                        8] + " | " +
                    damePanelE[9] + " " + "\n" + lineSeparation + " " + damePanelF[0] + " | " + damePanelF[
                        1] + " | " +
                    damePanelF[2] + " | " + damePanelF[3] + " | " + damePanelF[
                        4] + " | " + damePanelF[5] + " | " + damePanelF[6] + " | " + damePanelF[7] + " | " +
                    damePanelF[
                        8] + " | " +
                    damePanelF[9] + " " + "\n" + lineSeparation + " " + damePanelG[0] + " | " + damePanelG[
                        1] + " | " +
                    damePanelG[2] + " | " + damePanelG[3] + " | " + damePanelG[
                        4] + " | " + damePanelG[5] + " | " + damePanelG[6] + " | " + damePanelG[7] + " | " +
                    damePanelG[
                        8] + " | " +
                    damePanelG[9] + " " + "\n" + lineSeparation + " " + damePanelH[0] + " | " + damePanelH[
                        1] + " | " +
                    damePanelH[2] + " | " + damePanelH[3] + " | " + damePanelH[
                        4] + " | " + damePanelH[5] + " | " + damePanelH[6] + " | " + damePanelH[7] + " | " +
                    damePanelH[
                        8] + " | " +
                    damePanelH[9] + " " + "\n" + lineSeparation + " " + damePanelI[0] + " | " + damePanelI[
                        1] + " | " +
                    damePanelI[2] + " | " + damePanelI[3] + " | " + damePanelI[
                        4] + " | " + damePanelI[5] + " | " + damePanelI[6] + " | " + damePanelI[7] + " | " +
                    damePanelI[
                        8] + " | " +
                    damePanelI[9] + " " + "\n" + lineSeparation + " " + damePanelJ[0] + " | " + damePanelJ[
                        1] + " | " +
                    damePanelJ[2] + " | " + damePanelJ[3] + " | " + damePanelJ[
                        4] + " | " + damePanelJ[5] + " | " + damePanelJ[6] + " | " + damePanelJ[7] + " | " +
                    damePanelJ[
                        8] + " | " +
                    damePanelJ[9] + " \n\nQuel pion voulez vous bouger (Exemple : 1J) : ")

                canIGoTheir = False



    elif askWhichGame == str(3):
        print("\nNot finished\n# Please Excuse Me for Bugs #\n")

    else:
        print("\nCe jeu n'existe pas\n")

# Second program Ulysse Coispellier has ever created on (December, 13th 2021)
