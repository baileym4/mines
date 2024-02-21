"""
Mines N-D
"""
#!/usr/bin/env python3

import typing
import doctest



def dump(game):
    """
    Prints a human-readable version of a game (provided as a dictionary)
    """
    keys = ("board", "dimensions", "state", "visible", "mines")
    # ^ Uses only default game keys. If you modify this you will need
    # to update the docstrings in other functions!
    for key in keys:
        val = game[key]
        if isinstance(val, list) and val and isinstance(val[0], list):
            print(f"{key}:")
            for inner in val:
                print(f"    {inner}")
        else:
            print(f"{key}:", val)


# 2-D IMPLEMENTATION


def new_game_2d(nrows, ncolumns, mines):
    """
    Start a new game.

    Return a game state dictionary, with the 'dimensions', 'state', 'board' and
    'visible' fields adequately initialized.

    Parameters:
       nrows (int): Number of rows
       ncolumns (int): Number of columns
       mines (list): List of mines, given in (row, column) pairs, which are
                     tuples

    Returns:
       A game state dictionary

    >>> dump(new_game_2d(2, 4, [(0, 0), (1, 0), (1, 1)]))
    board:
        ['.', 3, 1, 0]
        ['.', '.', 1, 0]
    dimensions: (2, 4)
    state: ongoing
    visible:
        [False, False, False, False]
        [False, False, False, False]
    mines: 3
    """

    return new_game_nd((nrows, ncolumns), mines)


def dig_2d(game, row, col):
    """
    Reveal the cell at (row, col), and, in some cases, recursively reveal its
    neighboring squares.

    Update game['visible'] to reveal (row, col).  Then, if (row, col) has no
    adjacent mines (including diagonally), then recursively reveal (dig up) its
    eight neighbors.  Return an integer indicating how many new squares were
    revealed in total, including neighbors, and neighbors of neighbors, and so
    on.

    The state of the game should be changed to 'defeat' when at least one mine
    is visible on the board after digging (i.e. game['visible'][mine_location]
    == True), 'victory' when all safe squares (squares that do not contain a
    mine) and no mines are visible, and 'ongoing' otherwise.

    Parameters:
       game (dict): Game state
       row (int): Where to start digging (row)
       col (int): Where to start digging (col)

    Returns:
       int: the number of new squares revealed

    >>> game = {'dimensions': (2, 4),
    ...         'board': [['.', 3, 1, 0],
    ...                   ['.', '.', 1, 0]],
    ...         'visible': [[False, True, False, False],
    ...                  [False, False, False, False]],
    ...         'state': 'ongoing', 'mines': 3 }
    >>> dig_2d(game, 0, 3)
    4
    >>> dump(game)
    board:
        ['.', 3, 1, 0]
        ['.', '.', 1, 0]
    dimensions: (2, 4)
    state: victory
    visible:
        [False, True, True, True]
        [False, False, True, True]
    mines: 3

    >>> game = {'dimensions': [2, 4],
    ...         'board': [['.', 3, 1, 0],
    ...                   ['.', '.', 1, 0]],
    ...         'visible': [[False, True, False, False],
    ...                  [False, False, False, False]],
    ...         'state': 'ongoing', 'mines': 3}
    >>> dig_2d(game, 0, 0)
    1
    >>> dump(game)
    board:
        ['.', 3, 1, 0]
        ['.', '.', 1, 0]
    dimensions: [2, 4]
    state: defeat
    visible:
        [True, True, False, False]
        [False, False, False, False]
    mines: 3
    """
    # new code

    return dig_nd(game, (row, col))


def render_2d_locations(game, all_visible=False):
    """
    Prepare a game for display.

    Returns a two-dimensional array (list of lists) of '_' (hidden squares),
    '.' (mines), ' ' (empty squares), or '1', '2', etc. (squares neighboring
    mines).  game['visible'] indicates which squares should be visible.  If
    all_visible is True (the default is False), game['visible'] is ignored
    and all cells are shown.

    Parameters:
       game (dict): Game state
       all_visible (bool): Whether to reveal all tiles or just the ones allowed
                    by game['visible']

    Returns:
       A 2D array (list of lists)

    >>> game = {'dimensions': (2, 4), 'mines': 3,
    ...         'state': 'ongoing',
    ...         'board': [['.', 3, 1, 0],
    ...                   ['.', '.', 1, 0]],
    ...         'visible':  [[False, True, True, False],
    ...                   [False, False, True, False]]}
    >>> render_2d_locations(game, False)
    [['_', '3', '1', '_'], ['_', '_', '1', '_']]

    >>> render_2d_locations(game, True)
    [['.', '3', '1', ' '], ['.', '.', '1', ' ']]
    """
    return render_nd(game, all_visible)


def render_2d_board(game, all_visible=False):
    """
    Render a game as ASCII art.

    Returns a string-based representation of argument 'game'.  Each tile of the
    game board should be rendered as in the function
        render_2d_locations(game)

    Parameters:
       game (dict): Game state
       all_visible (bool): Whether to reveal all tiles or just the ones allowed
                           by game['visible']

    Returns:
       A string-based representation of game

    >>> render_2d_board({'dimensions': (2, 4), 'mines': 3,
    ...                  'state': 'ongoing',
    ...                  'board': [['.', 3, 1, 0],
    ...                            ['.', '.', 1, 0]],
    ...                  'visible':  [[True, True, True, False],
    ...                            [False, False, True, False]]})
    '.31_\\n__1_'
    """

    array_to_show = render_nd(game, all_visible)
    rows, cols = game["dimensions"]
    final_str = ""
    for r in range(rows):
        if r > 0:
            final_str += "\n"
        for c in range(cols):
            if array_to_show[r][c] == 0:
                add = " "
            else:
                add = str(array_to_show[r][c])
            final_str += add
    return final_str


# N-D IMPLEMENTATION


def new_game_nd(dimensions, mines):
    """
    Start a new game.

    Return a game state dictionary, with the 'dimensions', 'state', 'board' and
    'visible' fields adequately initialized.

    Args:
       dimensions (tuple): Dimensions of the board
       mines (list): mine locations as a list of tuples, each an
                     N-dimensional coordinate

    Returns:
       A game state dictionary

    >>> g = new_game_nd((2, 4, 2), [(0, 0, 1), (1, 0, 0), (1, 1, 1)])
    >>> dump(g)
    board:
        [[3, '.'], [3, 3], [1, 1], [0, 0]]
        [['.', 3], [3, '.'], [1, 1], [0, 0]]
    dimensions: (2, 4, 2)
    state: ongoing
    visible:
        [[False, False], [False, False], [False, False], [False, False]]
        [[False, False], [False, False], [False, False], [False, False]]
    mines: 3
    """

    current_board = create_array(dimensions, 0)
    for coord in mines:
        replace_value(current_board, coord, ".")
        neighbors = get_neighbors(coord, dimensions)
        for neighbor in neighbors:
            current_val = find_value(current_board, neighbor)
            if current_val != ".":
                replace_value(current_board, neighbor, (1 + int(current_val)))
    visible_array = create_array(dimensions, False)

    return {
        "board": current_board,
        "dimensions": dimensions,
        "state": "ongoing",
        "visible": visible_array,
        "mines": len(mines),
    }


def dig_nd(game, coordinates, recurse=False):
    """
    Recursively dig up square at coords and neighboring squares.

    Update the visible to reveal square at coords; then recursively reveal its
    neighbors, as long as coords does not contain and is not adjacent to a
    mine.  Return a number indicating how many squares were revealed.  No
    action should be taken and 0 returned if the incoming state of the game
    is not 'ongoing'.

    The updated state is 'defeat' when at least one mine is visible on the
    board after digging, 'victory' when all safe squares (squares that do
    not contain a mine) and no mines are visible, and 'ongoing' otherwise.

    Args:
       coordinates (tuple): Where to start digging

    Returns:
       int: number of squares revealed

    >>> g = {'dimensions': (2, 4, 2),
    ...      'board': [[[3, '.'], [3, 3], [1, 1], [0, 0]],
    ...                [['.', 3], [3, '.'], [1, 1], [0, 0]]],
    ...      'visible': [[[False, False], [False, True], [False, False],
    ...                [False, False]],
    ...               [[False, False], [False, False], [False, False],
    ...                [False, False]]],
    ...      'state': 'ongoing', 'mines': 3}
    >>> dig_nd(g, (0, 3, 0))
    8
    >>> dump(g)
    board:
        [[3, '.'], [3, 3], [1, 1], [0, 0]]
        [['.', 3], [3, '.'], [1, 1], [0, 0]]
    dimensions: (2, 4, 2)
    state: ongoing
    visible:
        [[False, False], [False, True], [True, True], [True, True]]
        [[False, False], [False, False], [True, True], [True, True]]
    mines: 3
    >>> g = {'dimensions': (2, 4, 2),
    ...      'board': [[[3, '.'], [3, 3], [1, 1], [0, 0]],
    ...                [['.', 3], [3, '.'], [1, 1], [0, 0]]],
    ...      'visible': [[[False, False], [False, True], [False, False],
    ...                [False, False]],
    ...               [[False, False], [False, False], [False, False],
    ...                [False, False]]],
    ...      'state': 'ongoing', 'mines': 3}
    >>> dig_nd(g, (0, 0, 1))
    1
    >>> dump(g)
    board:
        [[3, '.'], [3, 3], [1, 1], [0, 0]]
        [['.', 3], [3, '.'], [1, 1], [0, 0]]
    dimensions: (2, 4, 2)
    state: defeat
    visible:
        [[False, True], [False, True], [False, False], [False, False]]
        [[False, False], [False, False], [False, False], [False, False]]
    mines: 3
    """

    def recursive_helper(coordinates):
        revealed = 0
        game_board = game["board"]
        visible_board = game["visible"]
        dim = game["dimensions"]
        val = find_value(visible_board, coordinates)
        if val or game["state"] != "ongoing":
            return 0
        if find_value(game_board, coordinates) == ".":
            replace_value(visible_board, coordinates, True)
            game["state"] = "defeat"
            return 1
        if find_value(game_board, coordinates) != 0:
            replace_value(visible_board, coordinates, True)
            return 1

        replace_value(visible_board, coordinates, True)
        neighbors = get_neighbors(coordinates, dim)
        revealed += 1
        for neighbor in neighbors:
            if neighbor == coordinates:
                continue
            revealed += recursive_helper(neighbor)
        return revealed

    uncovered = recursive_helper(coordinates)

    if victory_check(game):
        game["state"] = "victory"

    return uncovered


def victory_check(game):
    """
    Determines if the game has been won
    """
    num_mines = game["mines"]
    dimension = game["dimensions"]
    coord_list = get_all_coords(dimension)
    visible_board = game["visible"]
    true_count = 0
    tile_count = len(coord_list)
    for coord in coord_list:
        if find_value(visible_board, coord):
            true_count += 1
        else:
            if find_value(game["board"], coord) != ".":
                return False
    return (true_count + num_mines) == tile_count


def render_nd(game, all_visible=False):
    """
    Prepare the game for display.

    Returns an N-dimensional array (nested lists) of '_' (hidden squares), '.'
    (mines), ' ' (empty squares), or '1', '2', etc. (squares neighboring
    mines).  The game['visible'] array indicates which squares should be
    visible.  If all_visible is True (the default is False), the game['visible']
    array is ignored and all cells are shown.

    Args:
       all_visible (bool): Whether to reveal all tiles or just the ones allowed
                           by game['visible']

    Returns:
       An n-dimensional array of strings (nested lists)

    >>> g = {'dimensions': (2, 4, 2),
    ...      'board': [[[3, '.'], [3, 3], [1, 1], [0, 0]],
    ...                [['.', 3], [3, '.'], [1, 1], [0, 0]]],
    ...      'visible': [[[False, False], [False, True], [True, True],
    ...                [True, True]],
    ...               [[False, False], [False, False], [True, True],
    ...                [True, True]]],
    ...      'state': 'ongoing'}
    >>> render_nd(g, False)
    [[['_', '_'], ['_', '3'], ['1', '1'], [' ', ' ']],
     [['_', '_'], ['_', '_'], ['1', '1'], [' ', ' ']]]

    >>> render_nd(g, True)
    [[['3', '.'], ['3', '3'], ['1', '1'], [' ', ' ']],
     [['.', '3'], ['3', '.'], ['1', '1'], [' ', ' ']]]
    """
    dimension = game["dimensions"]
    render = create_array(dimension, 0)
    visible_board = game["visible"]
    game_board = game["board"]
    coords = get_all_coords(dimension)
    if all_visible:
        # filter through all options and put in string version
        for coord in coords:
            val = find_value(game_board, coord)
            if val == 0:
                replace_value(render, coord, " ")
            else:
                replace_value(render, coord, str(val))
    else:
        for coord in coords:
            if find_value(visible_board, coord) is True:
                val = find_value(game_board, coord)
                if val == 0:
                    replace_value(render, coord, " ")
                else:
                    replace_value(render, coord, str(val))
            else:
                replace_value(render, coord, "_")

    return render


def find_value(array, coord):
    """
    Finds the value in an N-d array of the coords
    """
    if len(coord) == 1:
        return array[coord[0]]
    else:
        first = coord[0]
        rest = coord[1:]
        current_level = array[first]
        return find_value(current_level, rest)


def replace_value(array, coord, value):
    """
    replaces value at coords with those values
    """
    if len(coord) == 1:
        ind = coord[0]
        array[ind] = value
    else:
        first = coord[0]
        rest = coord[1:]
        current_level = array[first]
        replace_value(current_level, rest, value)


def create_array(dimension, value):
    """
    creates a new N-d array with dimensions
    """
    if len(dimension) == 1:
        amount = dimension[0]
        return [value] * amount
    else:
        return [create_array(dimension[1:], value) for i in range(dimension[0])]


def get_neighbors(coord, dimension):
    """
    finds the neighbors of a given coordinate
    """
    if len(coord) == 1:
        val1 = coord[0]
        val2 = coord[0] - 1
        val3 = coord[0] + 1
        vals = [val1, val2, val3]
        return [
            (val,) for val in vals if 0 <= val < dimension[0]
        ]  # if val >= 0 and val < dimension[0]
    else:
        neighbors_list = []
        neighbors = get_neighbors(coord[1:], dimension[1:])
        first_element = get_neighbors((coord[0],), (dimension[0],))
        for neighbor in neighbors:
            for first in first_element:
                neighbors_list.append(first + neighbor)
        return neighbors_list


def get_all_coords(dimension):
    """
    gets all possible coords in a given board
    """
    if len(dimension) == 1:
        return [(i,) for i in range(dimension[0])]
    else:
        coord_list = []
        coords = get_all_coords(dimension[1:])
        first = dimension[0]
        for coord in coords:
            for val in range(first):
                coord_list.append((val,) + coord)
        return coord_list


if __name__ == "__main__":
    # Test with doctests. Helpful to debug individual lab.py functions.
    _doctest_flags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
    doctest.testmod(optionflags=_doctest_flags)  # runs ALL doctests

    # Alternatively, can run the doctests JUST for specified function/methods,
    # e.g., for render_2d_locations or any other function you might want.  To
    # do so, comment out the above line, and uncomment the below line of code.
    # This may be useful as you write/debug individual doctests or functions.
    # Also, the verbose flag can be set to True to see all test results,
    # including those that pass.
    #
    # doctest.run_docstring_examples(
    #     #render_2d_locations,
    #     render_2d_board,
    #    new_game_nd,
    #    globals(),
    #     optionflags=_doctest_flags,
    #     verbose=False
    # )
ans = create_array([2, 2], 6)
# print(ans)

array = [[[1, 0], [2, 0], [3, 0]], [[4, 0], [5, 0], [6, 0]]]
# ans1 = print(find_value(array, (1, 2, 0)))

# final = replace_value(array, (1, 2, 0), 8)
# print(array)
# n = get_neighbors((0, 3), (2, 6))
# print(n)
# coord_test = get_all_coords((3, 1, 1))
# print(coord_test) # slayed
