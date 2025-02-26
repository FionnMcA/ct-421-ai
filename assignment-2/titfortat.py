from strategy import Strategy


class TitForTat(Strategy):
    """
    Tit for tat (start friendly and copy the opponents last move)
    """

    def player_move(self, history):
        if not history:
            return 'c'

        opponent_last_move = history[-1]

        return opponent_last_move

    def get_name(self):
        return 'Tit For Tat'

