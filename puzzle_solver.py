# puzzle_solver.py
# 
# In retrospect, I should've started with this implementation first,
# before diving into a 2-player adversarial search. Oh well, at 
# least this works like it should!

class PuzzleSolver:
    ""
    def __init__(self, succ_func, referee):
        """ 
        Arguments:
            succ_func: a function that, given a game state, returns the set
                containing all possible next states. Note that a state must
                be represented with an immutable type (e.g., a tuple).
            referee: a function that determines if the current state is final,
                (i.e., the player/adversary have won) or if the state is neutral.
                For a 1-player puzzle, we return one of the following values:
                    0 => board is in a "lose" state (final)
                    1 => board is neutral (non-final)
                    2 => board is in a "win" state (final)
        """
        self.succ_func = succ_func
        self.referee = referee

    def bfs(self, initial_state):
        visited = { initial_state : None }  # state : predecessor
        queue = [ initial_state ]
        current_state = initial_state

        while queue and self.referee(current_state) < 2:
            current_state = queue.pop(0)
            for next_state in self.succ_func(current_state):
                if next_state not in visited:
                    visited[next_state] = current_state
                    if self.referee(next_state) > 0:
                        queue.append(next_state)

        path = [ current_state ]
        while visited[path[-1]]:  # backtrack along the path
            path.append(visited[path[-1]])

        return path[::-1]