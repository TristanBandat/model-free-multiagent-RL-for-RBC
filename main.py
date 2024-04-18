import numpy as np
import os
import torch
import torch.nn as nn
import torch.nn.functional as F
import random
import argparse
import datetime
import traceback
import chess
import cProfile
from reconchess import *


def main() -> None:
    # TODO: add model name here
    player_1 = ''
    player_2 = ''
    number_of_games_per_color = 2
    time = 900
    player_1_wins = 0
    player_2_wins = 0

    for game_num in range(number_of_games_per_color):
        winner = play_game(player_1, player_2, time)
        if winner == 'white':
            player_1_wins += 1
        else:
            player_2_wins += 1

    for game_num in range(number_of_games_per_color):
        winner = play_game(player_2, player_1, time)
        if winner == 'white':
            player_2_wins += 1
        else:
            player_1_wins += 1

    print(f'Player 1 {player_1} wins: {str(player_1_wins)}')
    print(f'Player 2 {player_2} wins: {str(player_2_wins)}')


if __name__ == "__main__":
    main()

