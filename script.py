import sys

try:
    import requests
except ImportError:
    sys.exit(
        'requests was not properly installed. Try again. Are you sure you are in a venv?')


def get_fantasy_points(player, pos):
    if player.get('position') == pos:
        return player.get('fantasy_points').get('ppr')
