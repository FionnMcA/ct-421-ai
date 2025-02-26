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

    total_results = {
        strategy.get_name(): {
        'total_points': 0
        }
        for strategy in strategies
    }

    rounds = 10

    for strat1, strat2 in product(strategies, repeat=2):
        pd = PrisonersDilema(strat1, strat2, rounds)
        p1_points, p2_points = pd.play_game()

        print(f"{strat1.get_name()} - {p1_points} vs {strat2.get_name()} = {p2_points}")

        total_results[strat1.get_name()]['total_points'] += p1_points
        total_results[strat2.get_name()]['total_points'] += p2_points

    print(total_results)

if __name__ == '__main__':
    play_all_strategies()
