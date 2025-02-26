from itertools import product
from prisonersdilema import PrisonersDilema
from alwaysc import AlwaysC
from alwaysd import AlwaysD
from titfortat import TitForTat


def play_all_strategies():
    strategies = [
        AlwaysC(),
        AlwaysD(),
        TitForTat()
    ]

    rounds = 10

    for strat1, strat2 in product(strategies, repeat=2):
        pd = PrisonersDilema(strat1, strat2, rounds)
        p1_points, p2_points = pd.play_game()

        print(f"{strat1.get_name()} - {p1_points} vs {strat2.get_name()} = {p2_points}")

if __name__ == '__main__':
    play_all_strategies()