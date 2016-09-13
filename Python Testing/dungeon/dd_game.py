"""Dungeon Game
Explore a dungeon to find a hidden door and escape. But be careful!
The grue is hiding somewhere inside!

Created: 2016
Updated: 2016
Author: Brian Weber
"""

import os
import random

GAME_DIMENSIONS = (5, 5)
player = {'location': None, 'path': []}


def clear():
    """Clear the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def build_cells(width, height):
    """Create and return a "width" x "height" grid of two-tuples
    
    >>> cells = build_cells(2, 2)
    >>> len(cells)
    4
    
    """
    cells = []
    for y in range(height):
        for x in range(width):
            cells.append((x, y))
    return cells


def get_locations(cells):
    """Randomly pick starting locations for the monster, the door, 
    and the player.
    
    >>> cells = build_cells(2, 2)
    >>> m, d, p = get_locations(cells)
    >>> m != d and d != p
    True
    >>> d in cells
    True
    
    """
    monster = random.choice(cells)
    door = random.choice(cells)
    player = random.choice(cells)

    if monster == door or monster == player or door == player:
        monster, door, player = get_locations(cells)

    return monster, door, player


def get_moves(player):
    """Based on the tuple of the player's position, return the list
    of acceptable moves.
    
    >>> GAME_DIMENSIONS = (2, 2)
    >>> get_moves((0,2))                                               
    ['RIGHT', 'UP', 'DOWN']
    
    """
    x, y = player
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    if x == 0:
        moves.remove('LEFT')
    if x == GAME_DIMENSIONS[0] - 1:
        moves.remove('RIGHT')
    if y == 0:
        moves.remove('UP')
    if y == GAME_DIMENSIONS[1] - 1:
        moves.remove('DOWN')
    return moves


def move_player(player, move):
    """Move player within the cells drawn.
    
    
    
    
    """
    x, y = player['location']
    player['path'].append((x, y))
    if move == 'LEFT':
        x -= 1
    elif move == 'UP':
        y -= 1
    elif move == 'RIGHT':
        x += 1
    elif move == 'DOWN':
        y += 1
    return x, y


def draw_map():
    print(' _'*GAME_DIMENSIONS[0])
    row_end = GAME_DIMENSIONS[0]
    tile = '|{}'
    for index, cell in enumerate(cells):
        if index % row_end < row_end - 1:
            if cell == player['location']:
                print(tile.format('X'), end='')
            elif cell in player['path']:
                print(tile.format('.'), end='')
            else:
                print(tile.format('_'), end='')
        else:
            if cell == player['location']:
                print(tile.format('X|'))
            elif cell in player['path']:
                print(tile.format('.|'))
            else:
                print(tile.format('_|'))

def play():
    cells = build_cells(*GAME_DIMENSIONS)
    monster, door, player['location'] = get_locations(cells)

    while True:
        clear()

        print("WELCOME TO THE DUNGEON!")
        moves = get_moves(player['location'])

        draw_map(cells)

        print("\nYou're currently in room {}".format(player['location']))
        print("\nYou can move {}".format(', '.join(moves)))
        print("Enter QUIT to quit")

        move = input("> ")
        move = move.upper()

        if move in ['QUIT', 'Q']:
            break

        if move not in moves:
            print("\n** Walls are hard! Stop running into them! **\n")
            continue

        player['location'] = move_player(player, move)

        if player['location'] == door:
            print("\n** You escaped! **\n")
            break
        elif player['location'] == monster:
            print("\n** You got eaten! **\n")
            break

if __name__ == '__main__':
    play()