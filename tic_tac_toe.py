# tic_tac_toe.py

from adversary import Adversary

def main():
    game_state = (
        ' ', ' ', ' ', 
        ' ', ' ', ' ',
        ' ', ' ', ' '
    )
    opponent = Adversary(succ_func, referee)

    turn = 1
    while referee(game_state) == 1:
        if turn == 1:
            print_board(game_state)
            idx = int(input("Your move: "))
            game_state = mod_copy(game_state, idx, 'X')
        else:
            game_state = opponent.query(game_state)

        turn = 1 - turn

    print_board(game_state)
    if referee(game_state) == 2:
        print("You won!!")
    else:
        print("The aversary won :(")
    

def mod_copy(t, i, e):
    """ Return a copy of a tuple t, with index i set to e """
    return t[ :i] + (e,) + t[i+1: ]


def succ_func(game_state):
    successors = []
    for i,cell in enumerate(game_state):
        if cell == ' ':
            next_state = mod_copy(game_state, i, 'O')
            successors.append(next_state)

    return successors

def referee(game_state):
    lines = [
        [0,1,2], [3,4,5], [6,7,8], 
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for line in lines:
        if ('X' == game_state[line[0]] 
                == game_state[line[1]] 
                == game_state[line[2]]):
            return 2
        elif ('O' == game_state[line[0]] 
                == game_state[line[1]] 
                == game_state[line[2]]):
            return 0

    return 1

def print_board(game_state):
    print_row(game_state[0:3])
    print('-----------')
    print_row(game_state[3:6])
    print('-----------')
    print_row(game_state[6:9])
    print()

def print_row(row):
    print(f' {row[0]} ', end='')
    for cell in row[1:]:
        print(f'| {cell} ', end='')
    print()

if __name__ == '__main__':
    main()
