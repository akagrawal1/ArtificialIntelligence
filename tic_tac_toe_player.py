import random
import operator

# a4.py

# ...

#if __name__ == '__main__':
 # play_a_new_game()

def play_a_new_game():
    #Turn turn_flag 0 when its players turn. Turn flag = 1 when its computers turn
    turn_flag = 0
    #endgame_flag = 1 when one player wins, loses or ties
    endgame_flag = 0
    #Hashmap entries: 2 = blank space, 1 = users token, 0 = computers token
    gameboard = {1:2, 2:2, 3:2, 4:2, 5:2, 6:2, 7:2, 8:2, 9:2}
    print("Here's how the game works:")
    print("You - the user - goes first and selects a value between 1-9, 1 being the coordinate location for top left, 9 being the bottom right (3 is top right, 7 is bottom left)")
    print("After your turn the computer will play its turn, display the board for you and ask you for another turn")
    print("On the board, a 2 represents a blank space - meaning you can play your turn there")
    print("A 1 on the board represents the user (your) token, and a 0 represents the computers token")
    while(endgame_flag == 0):
        if(goal_check(gameboard, 0)):
            print("The comptuer won")
            break
        elif(goal_check(gameboard, 1)):
            print("The user won")
            break
        else:
            possible_turns = populate_possible_turns(gameboard)
            if(len(possible_turns) == 0):
                print("It's a tie")
                break
            player_turn = input("Enter a value between 1-9: ")
            if(int(player_turn) < 1 or int(player_turn) > 9):
                print("Invalid input")
            else:
                gameboard[int(player_turn)] = 1
                if(goal_check(gameboard, 1)):
                    print("The user won")
                    break
                else:
                    possible_turns = populate_possible_turns(gameboard)
                    if(len(possible_turns) == 0):
                        print("It's a tie")
                        break
                    simulated_games = dict()
                    for location in possible_turns:
                        simulated_games[location] = simulator(gameboard, 10000, possible_turns, location)
                    computers_choice = max(simulated_games.items(), key=operator.itemgetter(1))[0]
                    gameboard[int(computers_choice)] = 0
                    print_gameboard(gameboard)

def simulator(gameboard, n, possible_turns, index):
    # count = 0
    # for i in range(n):
    #     count += random.choice([-1, 0, 1])
    # return count
    count = 0
    for i in range(n):
        temp_gameboard = clone_gameboard(gameboard)
        temp_gameboard[index] = 0
        possible_turns = populate_possible_turns(gameboard)
        player_turn = True
        while(not(goal_check(temp_gameboard, 0) or goal_check(temp_gameboard, 1)) and len(possible_turns) is not 0):
            users_turn = random.choice(possible_turns)
            temp_gameboard[users_turn] = 1 if player_turn else 0
            possible_turns = populate_possible_turns(temp_gameboard)
            player_turn = not player_turn
        if(goal_check(temp_gameboard , 0)):
            count += 2
        elif(goal_check(temp_gameboard, 1)):
            count -= 1
        elif(len(possible_turns) == 0):
            count += 1
    return count


def clone_gameboard(gameboard):
    cloned_gameboard = dict()
    for index, item in gameboard.items():
        cloned_gameboard[index] = item
    return cloned_gameboard

def print_gameboard(gameboard):
    for i in range(1,10):
        if(i == 4 or i == 7):
            print("")
        print(gameboard[i], end="")
        print(" ", end="")
    print("")

def goal_check(gameboard, player):
    if(\
    (gameboard[1] == player and gameboard[2] == player and gameboard[3] == player)\
    or (gameboard[4] == player and gameboard[5] == player and gameboard[6] == player)\
    or (gameboard[7] == player and gameboard[8] == player and gameboard[9] == player)\
    or (gameboard[1] == player and gameboard[4] == player and gameboard[7] == player)\
    or (gameboard[2] == player and gameboard[5] == player and gameboard[8] == player)\
    or (gameboard[3] == player and gameboard[6] == player and gameboard[9] == player)\
    or (gameboard[1] == player and gameboard[5] == player and gameboard[9] == player)\
    or (gameboard[3] == player and gameboard[5] == player and gameboard[7] == player)\
    ):
        #return true if the player wins
        return True
    else:
        return False

def populate_possible_turns(gameboard):
    possible_turns = []
    for location in gameboard:
        if gameboard[location] == 2:
            possible_turns.append(location)
    return possible_turns


play_a_new_game()
