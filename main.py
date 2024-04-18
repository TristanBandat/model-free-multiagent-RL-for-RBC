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


def play_game(player_1: str, player_2: str, time: int) -> str:
    white_bot_name, white_player_cls = load_player(player_1)
    black_bot_name, black_player_cls = load_player(player_2)

    game = LocalGame(time)

    try:
        winner_color, win_reason, history = play_local_game(white_player_cls(), black_player_cls(), game=game)
        winner = 'Draw' if winner_color is None else chess.COLOR_NAMES[winner_color]
    except:
        traceback.print_exc()
        game.end()
        winner = 'ERROR'
        history = game.get_game_history()

    print('Game Over!')
    print('Winner: {}!'.format(winner))
    try:
        print('Win reason: {}'.format(win_reason))
    except TypeError:
        raise TypeError("Win reason can't be printed")

    # timestamp = datetime.datetime.now().strftime('%Y_%m_%d-%H_%M_%S')
    # replay_path = '{}-{}-{}-{}.json'.format(white_bot_name, black_bot_name, winner, timestamp)
    # print('Saving replay to {}...'.format(replay_path))
    # history.save(replay_path)
    return winner


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
