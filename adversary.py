# adversary.py

class Adversary:
    """ """
    def __init__(self, succ_func, referee):
        """ """
        self.succ_func = succ_func
        self.referee = referee

    def query(self, game_state):
        """ """
        return self.game_BFS(game_state)[-1]

    def game_BFS(self, game_state):
        """ """
        visited = {game_state : None}  # state : predecessor
        queue = self.succ_func(game_state)
        current_state = game_state

        while queue and self.referee(current_state) != 2:
            visited[queue[0]] = current_state
            current_state = queue.pop(0)

            for state in self.succ_func(current_state):
                if state not in visited:
                    queue.append(state)

        path = [current_state]
        while visited[path[-1]]:  # backtrack along the path
            path.append(visited[path[-1]])
            
        return path
