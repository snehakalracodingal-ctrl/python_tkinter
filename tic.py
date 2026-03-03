theBoard = {"7":" ","8":" ","9":" ",
            "4":" ","5":" ","6":" ",
            "1":" ","2":" ","3":" "}
board_keys = []
for key in theBoard:
    board_keys.append(key)
def printBoard(Board):
    print(Board["7"] + "|"+Board["8"] + "|" + Board["9"])
    print("-+-+-")
    print(Board["4"] + "|"+Board["5"] + "|"+Board["6"])
    print("-+-+-")
    print(Board["1"] + "|"+Board["2"] + "|"+Board["3"])
def game():
    turn = "X"
    count = 0 
    for i in range(10):
        printBoard(theBoard)
        print("Its your turn" + turn + ".Move to which place")
        move = input()
        if theBoard(move) == " ":
            theBoard(move) == turn
            count += 1
        else:
            print("That place is already filled \n move to another place")
            continue
        if count >= 5:
            if theBoard == ["7"] == ["8"] == ["9"] != " ":
                printBoard(theBoard)
                print("Game over")
                print()
                print("****"+turn+"Won.****")
                break
            elif theBoard == ["4"] == ["5"] == ["6"] != " ":
                printBoard(theBoard)
                print("Game over")
                print()
                print("****"+turn+"Won.****")
                break
            elif theBoard == ["1"] == ["2"] == ["3"] != " ":
                printBoard(theBoard)
                print("Game over")
                print()
                print("****"+turn+"Won.****")
                break
            elif theBoard == ["7"] == ["4"] == ["1"] != " ":
                printBoard(theBoard)
                print("Game over")
                print()
                print("****"+turn+"Won.****")
                break
            elif theBoard == ["8"] == ["5"] == ["2"] != " ":
                printBoard(theBoard)
                print("Game over")
                print()
                print("****"+turn+"Won.****")
                break
            elif theBoard == ["9"] == ["6"] == ["3"] != " ":
                printBoard(theBoard)
                print("Game over")
                print()
                print("****"+turn+"Won.****")
                break
            elif theBoard == ["7"] == ["5"] == ["3"] != " ":
                printBoard(theBoard)
                print("Game over")
                print()
                print("****"+turn+"Won.****")
                break
            elif theBoard == ["9"] == ["5"] == ["1"] != " ":
                printBoard(theBoard)
                print("Game over")
                print()
                print("****"+turn+"Won.****")
                break
        if count == 9:
            print("Game over")
            print("Its A Tie")
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
            restart = input("Do you want to play again? (y/n)")
            if restart == "y" or "Y":
                for key in board_keys:
                    theBoard[key] = " "

                game()
if __name__ =="__main__":
    game()