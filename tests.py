import logging
from main import numberOfAvailableDifferentPaths, numberOfAvailableDifferentPathsRecursive


# Iterative approach tests

def test1_numberOfAvailableDifferentPaths():
    board = [4, 3]
    snake = [[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]]
    depth = 3

    logging.info(f'Running \'test1_numberOfAvailableDifferentPaths\', parameters: board={board}, snake={snake}, depth={depth}')
    try:
        assert numberOfAvailableDifferentPaths(board, snake, depth) == 7
    except:
        logging.error('\'test1_numberOfAvailableDifferentPaths\' failed')

def test2_numberOfAvailableDifferentPaths():
    board = [2, 3]
    snake = [[0,2], [0,1], [0,0], [1,0], [1,1], [1,2]]
    depth = 10

    logging.info(f'Running \'test2_numberOfAvailableDifferentPaths\', parameters: board={board}, snake={snake}, depth={depth}')
    try:
        assert numberOfAvailableDifferentPaths(board, snake, depth) == 1
    except:
        logging.error('\'test2_numberOfAvailableDifferentPaths\' failed')

def test3_numberOfAvailableDifferentPaths():
    board = [10, 10]
    snake = [[5,5], [5,4], [4,4], [4,5]]
    depth = 4

    logging.info(f'Running \'test3_numberOfAvailableDifferentPaths\', parameters: board={board}, snake={snake}, depth={depth}')
    try:
        assert numberOfAvailableDifferentPaths(board, snake, depth) == 81
    except:
        logging.error('\'test3_numberOfAvailableDifferentPaths\' failed')



# Recursive approach tests

def test1_numberOfAvailableDifferentPathsRecursive():
    board = [4, 3]
    snake = [[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]]
    depth = 3

    logging.info(f'Running \'test1_numberOfAvailableDifferentPaths\', parameters: board={board}, snake={snake}, depth={depth}')
    try:
        assert numberOfAvailableDifferentPathsRecursive(board, snake, depth) == 7
    except:
        logging.error('\'test1_numberOfAvailableDifferentPaths\' failed')

def test2_numberOfAvailableDifferentPathsRecursive():
    board = [2, 3]
    snake = [[0,2], [0,1], [0,0], [1,0], [1,1], [1,2]]
    depth = 10

    logging.info(f'Running \'test2_numberOfAvailableDifferentPaths\', parameters: board={board}, snake={snake}, depth={depth}')
    try:
        assert numberOfAvailableDifferentPathsRecursive(board, snake, depth) == 1
    except:
        logging.error('\'test2_numberOfAvailableDifferentPaths\' failed')

def test3_numberOfAvailableDifferentPathsRecursive():
    board = [10, 10]
    snake = [[5,5], [5,4], [4,4], [4,5]]
    depth = 4

    logging.info(f'Running \'test3_numberOfAvailableDifferentPaths\', parameters: board={board}, snake={snake}, depth={depth}')
    try:
        assert numberOfAvailableDifferentPathsRecursive(board, snake, depth) == 81
    except:
        logging.error('\'test3_numberOfAvailableDifferentPaths\' failed')



def main():
    logging.info('Starting numberOfAvailableDifferentPaths tests')
    test1_numberOfAvailableDifferentPaths()
    test2_numberOfAvailableDifferentPaths()
    test3_numberOfAvailableDifferentPaths()

    logging.info('Starting numberOfAvailableDifferentPathsRecursive tests')
    test1_numberOfAvailableDifferentPathsRecursive()
    test2_numberOfAvailableDifferentPathsRecursive()
    test3_numberOfAvailableDifferentPathsRecursive()


if __name__ == '__main__':
    logging.basicConfig(level = logging.INFO)
    main()
    