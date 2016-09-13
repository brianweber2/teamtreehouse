import logging
import random

logging.basicConfig(filename='game.log', level=logging.DEBUG)

player = {'location': None, 'path': []}
cells = [(0, 0), (0, 1), (0, 2),
         (1, 0), (1, 1), (1, 2),
         (2, 0), (2, 1), (2, 2)]

def get_locations():
    monster = random.choice(cells)
    door = random.choice(cells)
    start = random.choice(cells)

    if monster == door or monster == start or door == start:
        monster, door, start = get_locations()

    return monster, door, start


def get_moves(player):
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    if player in [(0, 0), (1, 0), (2, 0)]:
        moves.remove('LEFT')
    if player in [(0, 0), (0, 1), (0, 2)]:
        moves.remove('UP')
    if player in [(0, 2), (1, 2), (2, 2)]:
        moves.remove('RIGHT')
    if player in [(2, 0), (2, 1), (2, 2)]:
        moves.remove('DOWN')
    return moves


def move_player(player, move):
    x, y = player['location']
    player['path'].append((x, y))
    if move == 'LEFT':
        player['location'] = x, y - 1
    elif move == 'UP':
        player['location'] = x - 1, y
    elif move == 'RIGHT':
        player['location'] = x, y + 1
    elif move == 'DOWN':
        player['location'] = x + 1, y
    return player


def draw_map():
    print(' _ _ _')
    tile = '|{}'
    for idx, cell in enumerate(cells):
        if idx in [0, 1, 3, 4, 6, 7]:
            if cell == player['location']:
                print(tile.format('X'), end='')
            elif cell in player['path']:
                print(tile.format('.'), end='')
            else:
                print(tile.format('_'), end='')
        else:
            if cell == player:
                print(tile.format('X|'))
            elif cell in player['path']:
                print(tile.format('.|'))
            else:
                print(tile.format('_|'))


monster, door, player['location'] = get_locations()
logging.info('monster: {}; door: {}; player: {}'.format(monster, door, player['location']))

while True:
    moves = get_moves(player['location'])
    print("Welcome to the dungeon!")
    print("You're currently in room {}".format(player['location']))

    draw_map()

    print("\nYou can move {}".format(', '.join(moves)))
    print("Enter QUIT to quit")

    move = input("> ")
    move = move.upper()

    if move == 'QUIT':
        break

    if not move in moves:
        print("\n** Walls are hard! Stop running into them! **\n")
        continue

    player = move_player(player, move)
    if player['location'] == door:
        print("\n** You escaped! **\n")
        break
    elif player['location'] == monster:
        print("\n** You got eaten! **\n")
        break
    else:
        continue
