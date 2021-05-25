# adversary.py

class Adversary:
    """ """
    def __init__(self, succ_func, referee):
        """ 
        Arguments:
            succ_func: a function that, given a game state, returns the set
                containing all possible next states. Note that a state must
                be represented with an immutable type (e.g., a tuple).
            referee: a function that determines if the current state is final,
                (i.e., the player/adversary have won) or if the state is neutral.
                We use the following return values to indicate this check:
                    0 => adversary has won
                    1 => board is neutral (non-final state)
                    2 => player has won
        """
        self.succ_func = succ_func
        self.referee = referee

    def query(self, game_state):
        """ """
        return self.game_BFS(game_state)[-2]

    def game_BFS(self, game_state):
        """ """
        visited = { game_state : None }  # state : predecessor
        queue = [ game_state ]
        current_state = game_state

        while queue and self.referee(current_state) != 0:
            current_state = queue.pop(0)
            for next_state in self.succ_func(current_state):
                if next_state not in visited:
                    visited[next_state] = current_state
                    queue.append(next_state)

        path = [ current_state ]
        while visited[path[-1]]:  # backtrack along the path
            path.append(visited[path[-1]])
            
        return path
