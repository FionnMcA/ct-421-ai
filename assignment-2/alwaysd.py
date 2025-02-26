from strategy import Strategy


class AlwaysD(Strategy):
    """
        Always defect the opponent
    """

    def player_move(self, history):
        return 'd'

    def get_name(self):
        return 'Always Defect'