fState = [[0,1,2],[3,4,5],[6,7,8]]

def helper_x():
    if(fState[0][0] == 'X' and fState[0][1] == 'X' and fState[0][2] == 'X'):
        return True
    elif(fState[1][0] == 'X' and fState[1][1] == 'X' and fState[1][2] == 'X'):
        return True
    elif(fState[2][0] == 'X' and fState[2][1] == 'X' and fState[2][2] == 'X'):
        return True
    elif(fState[0][0] == 'X' and fState[1][0] == 'X' and fState[2][0] == 'X'):
        return True
    elif(fState[0][1] == 'X' and fState[1][1] == 'X' and fState[2][1] == 'X'):
        return True
    elif(fState[0][2] == 'X' and fState[1][2] == 'X' and fState[2][2] == 'X'):
        return True
    elif(fState[0][0] == 'X' and fState[1][1] == 'X' and fState[2][2] == 'X'):
        return True
    elif(fState[0][2] == 'X' and fState[1][1] == 'X' and fState[2][0] == 'X'):
        return True
    else:
        return False    

def helper_z():
    if(fState[0][0] == 'O' and fState[0][1] == 'O' and fState[0][2] == 'O'):
        return True
    elif(fState[1][0] == 'O' and fState[1][1] == 'O' and fState[1][2] == 'O'):
        return True
    elif(fState[2][0] == 'O' and fState[2][1] == 'O' and fState[2][2] == 'O'):
        return True
    elif(fState[0][0] == 'O' and fState[1][0] == 'O' and fState[2][0] == 'O'):
        return True
    elif(fState[0][1] == 'O' and fState[1][1] == 'O' and fState[2][1] == 'O'):
        return True
    elif(fState[0][2] == 'O' and fState[1][2] == 'O' and fState[2][2] == 'O'):
        return True
    elif(fState[0][0] == 'O' and fState[1][1] == 'O' and fState[2][2] == 'O'):
        return True
    elif(fState[0][2] == 'O' and fState[1][1] == 'O' and fState[2][0] == 'O'):
        return True
    else:
        return False    
                                


def printBoard(xState,zState):

    k = 0

    for i in xState:
        if(i == 1):
            fState[int(k/3)][int(k%3)] = 'X'
            # print(f"The value of k : {k} and value of k/3 : {int(k/3)} and and value of k%3 : {int(k%3)}")
        k =  k + 1 
    
    k = 0

    for i in zState:
        if(i == 1):
            fState[int(k/3)][int(k%3)] = 'O'
            # print(f"The value of k : {k} and value of k/3 : {int(k/3)} and and value of k%3 : {int(k%3)}")
        k =  k + 1   


    for x in fState:
        print("\n")
        print("--|----|----|")
        for y in x:
            print(f"{y} | ",end = " ")

    print("\n")
    print("--|----|----|")

    

if __name__ == "__main__":
    print("Welcome to tic tac toe")
    xState = [0,0,0,0,0,0,0,0,0]
    zState = [0,0,0,0,0,0,0,0,0]

    turn = 1

    while(True):

        
        printBoard(xState,zState)


        if(helper_x()):
            print("X won the game")
            break
        elif(helper_z()):
            print("Z won the game")
            break

        

        if(turn == 1):
            print("Its X's chance.......")
            response = int(input("Enter the value of block number of the board : "))
            if(fState[int(response/3)][int(response%3)] != 'X' and fState[int(response/3)][int(response%3)] != 'O'):
                xState[response] = 1
                turn = 1 - turn
            else:
                print(f"Please re-enter the value")
        elif(turn == 0):
            print("Its Z's chance.......")
            response = int(input("Enter the value of block number of the board : "))
            if(fState[int(response/3)][int(response%3)] != 'X' and fState[int(response/3)][int(response%3)] != 'O'):
                zState[response] = 1
                turn = 1 - turn
            else:
                print(f"Please re-enter the value")
                
            

    printBoard(xState,zState)



