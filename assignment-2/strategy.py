
class Strategy():

    def __init__(self, name, first_move, responses, memory_size=1, friedman = False):
        self.name = name
        self.first_move = first_move # First move is either (1 = C, 0 = D)
        self.responses = responses
        self.history = []
        self.memory_size = memory_size
        self.friedman = friedman
        self.remain_defecting = False


    def player_move(self):
        if len(self.history) < self.memory_size:
            return self.first_move
        last_move = tuple(self.history[-self.memory_size:])
        if self.remain_defecting: # If It's a friedman like strategy where they remain defecting after 1 defect
            return 0
        return self.responses[last_move]

    def update_history(self, opp_move):
        self.history.append(opp_move)
        if self.friedman and opp_move == 0:
            self.remain_defecting = True


    def get_name(self):
        pass