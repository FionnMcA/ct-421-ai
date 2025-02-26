
class PrisonersDilema:

    def __init__(self, strat1, strat2, rounds):
        self.strat1 = strat1
        self.strat2 = strat2
        self.rounds = rounds
        self.p1_history = []
        self.p2_history = []
        self.p1_score = 0
        self.p2_score = 0
        self.payoff_matrix = {
            ('c', 'c'): (3, 3),
            ('c', 'd'): (0, 5),
            ('d', 'c'): (5, 0),
            ('d', 'd'): (1, 1)
        }

    def play_round(self):
        move1 = self.strat1.player_move(self.p2_history)
        move2 = self.strat2.player_move(self.p1_history)

        self.p1_history.append(move1)
        self.p2_history.append(move2)

        p1_points, p2_points = self.payoff_matrix.get((move1, move2))

        self.p1_score += p1_points
        self.p2_score += p2_points



    def play_game(self):
        for _ in range(self.rounds):
            self.play_round()
        print(self.p1_history)
        print(self.p2_history)
        return self.p1_score, self.p2_score