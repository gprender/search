# wgc.py
# Wolf-Goat-Cabbage problem
# 
# Problem explanation from Wikipedia:
#
# Once upon a time a farmer went to a market and purchased a wolf, a goat, and a cabbage. 
# On his way home, the farmer came to the bank of a river and rented a boat. But crossing 
# the river by boat, the farmer could carry only himself and a single one of his purchases: 
# the wolf, the goat, or the cabbage.
# If left unattended together, the wolf would eat the goat, or the goat would eat the cabbage.
# The farmer's challenge was to carry himself and his purchases to the far bank of the river, 
# leaving each purchase intact. How did he do it?

from puzzle_solver import PuzzleSolver

def main():
    # positions of the  Wolf / Goat / Cabbage / Boat  (0 => initial shore)
    initial_state = ( 0, 0, 0, 0 )   
    solver = PuzzleSolver(succ_func, referee)

    soln = solver.bfs(initial_state)

    print(soln)


def succ_func(state):
    successors = []

    # take one of the wolf/goat/cabbage across the river
    for idx,val in enumerate(state[:3]):
        if val == state[3]:
            succ = tuple(
                (1-e) if (i in {idx,3}) else e 
                for i,e in enumerate(state)
            )
            successors.append(succ)

    # cross the river with an empty boat
    successors.append(state[:3] + (1 - state[3],))

    return successors


def referee(state):
    # win state: all actors are on the goal shore
    if all(1 == e for e in state):
        return 2

    # lose states: wolf/goat or goat/cabbage left alone
    if ((state[0] == state[1] != state[3]) 
        or (state[1] == state[2] != state[3])):
        return 0
    
    # neutral state
    return 1


def print_board(state):
    ''' TODO: think up a more aesthetic way to output the puzzle's state'''
    pass


if __name__ == '__main__':
    main()
