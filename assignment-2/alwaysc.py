from strategy import Strategy


class AlwaysC(Strategy):
    """
    Always cooperate with the opponent
    """

    def player_move(self, history):
        return 'c'

    def get_name(self):
        return 'Always Cooperate'