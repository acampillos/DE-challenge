def manhattanDistance(u, v):
    '''Manhattan distance between two vectors.

    Given two vectors u and v of size n, let their Manhattan distance be
    .. math::

        d(u, v) = \sum_{i=1}^{n} |u_{i} - v_{i}|

    Parameters
    ----------
    u : list of int
        A point in XY plane
    v : tuple or list of int
        Another point in XY plane

    Returns
    ----------
    int 
        Manhattan distance between u and v
    '''
    return sum(map(lambda x,y: abs(x-y), zip(u, v)))

def inBoard(position, board):
    '''Return if a pair of coordinates (i,j) is part of the board.
    Checks if the given position is inside the board boundaries.

    Parameters
    ----------
    position : list of int or tuple of int
        Pair of coordinates
    board : list of int or tuple of int
        Pair of values describing the dimensions of the board.
        board[0] is the number of rows, board[1] is the number of columns.

    Returns
    ----------
    bool 
        True if the position is part of the board. False if not.
    '''
    m = board[0]
    n = board[1]

    return (0 <= position[0] and position[0] <= m-1) and (0 <= position[1] and position[1] <= n-1)

def adjacentCellsPositions(cell):
    '''Vertically or horizontally adjacent cells to the given cell.

    Parameters
    ----------
    cell : list of int or tuple of int
        Cell whose adjacents cells we want to know

    Returns
    ----------
    list of list of int
        Adjacent cells (coordinates) of the given cell.
        Returned cells are the right, left, upper and lower cells of the given one.
    '''
    i = cell[0]
    j = cell[1]

    # right, left, up, down
    return [[i+1,j], [i-1,j], [i, j-1], [i, j+1]]

def moveSnake(snake, position):
    '''Returns a new snake by moving the given one in the direction of the given position.
    Snake's head takes the new position and the following body cells take the previous body cells positions.

    Parameters
    ----------
    snake : list of list of int
        Snake's cells coordinates in the board
    position : list of int
        Pair of coordinates

    Returns
    ----------
    list of list or list of tuple
        Snake moved in the direction of the given position
    '''
    if position not in adjacentCellsPositions(snake[0]):
        raise Exception('Snake\'s head new position must be adjacent to the current one.')

    return [position] + snake[:-1]

def numberOfAvailableDifferentPathsRecursive(board, snake, depth):
    '''Returns the number of distinct valid paths of length equal to depth that the snake can make.

    Parameters
    ----------
    board : list of int or tuple of int
        Pair of values describing the dimensions of the board.
        board[0] is the number of rows, board[1] is the number of columns.
    snake : list of list of int
        Snake's cells coordinates in the board
    depth : int
        Paths' depth (max length)

    Returns
    ----------
    totalDifferentPaths : int
        Number of distinct valid paths of length equal to depth that the snake can make
    '''
    head = snake[0]

    if depth == 0:
        return 1

    totalDifferentPaths = 0

    for position in adjacentCellsPositions(head):
        if inBoard(position, board):
            if (position not in snake[1:-1]): # snake's body (head = snake[0], tail = snake[-1])
                movedSnake = moveSnake(snake, position)
                totalDifferentPaths += numberOfAvailableDifferentPaths(board, movedSnake, depth-1)

    return totalDifferentPaths

def numberOfAvailableDifferentPaths(board, snake, depth):
    '''Returns the number of distinct valid paths of length equal to depth that the snake can make.

    Parameters
    ----------
    board : list of int or tuple of int
        Pair of values describing the dimensions of the board.
        board[0] is the number of rows, board[1] is the number of columns.
    snake : list of list of int
        Snake's cells coordinates in the board
    depth : int
        Paths' depth (max length)

    Returns
    ----------
    totalDifferentPaths : int
        Number of distinct valid paths of length equal to depth that the snake can make
    '''
    totalDifferentPaths = 0

    stack = []
    stack.append((snake, depth))

    while len(stack)>0:
        movedSnake, d = stack.pop()
        head = movedSnake[0]
    
        if d == 0:
            totalDifferentPaths += 1
            continue

        for position in adjacentCellsPositions(head):
            if inBoard(position, board):
                if (position not in movedSnake[1:-1]): # snake's body (head = snake[0], tail = snake[-1])
                    stack.append((moveSnake(movedSnake, position), d-1))

    return totalDifferentPaths