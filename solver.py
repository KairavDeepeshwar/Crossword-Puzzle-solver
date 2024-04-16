MAX_ROWS = 10
MAX_COLS = 10
MAX_WORDS = 10

class Clue:
    def __init__(self, direction, row, col, answer, clue):
        self.direction = direction
        self.row = row
        self.col = col
        self.answer = answer
        self.clue = clue
        self.solved = False

    def to_dict(self):
        return {
            "direction": self.direction,
            "row": self.row,
            "col": self.col,
            "answer": self.answer,
            "clue": self.clue,
            "solved": self.solved
        }

class Puzzle:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.numWords = 0
        self.clues = [Clue('', 0, 0, '', '') for _ in range(MAX_WORDS)]
        self.grid = [['_' for _ in range(MAX_COLS)] for _ in range(MAX_ROWS)]

def load_game(filename, game):
    with open(filename, 'r') as file:
        game.rows, game.cols, game.numWords = map(int, file.readline().split())

        for i in range(game.numWords):
            direction, row, col, answer, clue = file.readline().split()
            game.clues[i] = Clue(direction, int(row), int(col), answer, clue)
            game.clues[i].solved = False

        for i in range(game.rows):
            game.grid[i] = ['_' for _ in range(game.cols)]

def solve_clue(game, clue_number, answer):
    index = clue_number - 1

    if game.clues[index].answer == answer:
        game.clues[index].solved = True

        if game.clues[index].direction == 'H':
            for i in range(len(answer)):
                game.grid[game.clues[index].row - 1][game.clues[index].col - 1 + i] = answer[i]
        elif game.clues[index].direction == 'V':
            for i in range(len(answer)):
                game.grid[game.clues[index].row - 1 + i][game.clues[index].col - 1] = answer[i]

        return True
    else:
        return False

def check_answer(clue, user_answer):
    correct_letters = []
    misplaced_letters = []

    for i in range(len(user_answer)):
        if user_answer[i] == clue.answer[i]:
            correct_letters.append(user_answer[i])
        elif user_answer[i] in clue.answer:
            misplaced_letters.append(user_answer[i])

    return correct_letters, misplaced_letters

def all_clues_solved(game):
    return all(clue.solved for clue in game.clues)
MAX_ROWS = 10
MAX_COLS = 10
MAX_WORDS = 10

class Clue:
    def __init__(self, direction, row, col, answer, clue):
        self.direction = direction
        self.row = row
        self.col = col
        self.answer = answer
        self.clue = clue
        self.solved = False

    def to_dict(self):
        return {
            "direction": self.direction,
            "row": self.row,
            "col": self.col,
            "answer": self.answer,
            "clue": self.clue,
            "solved": self.solved
        }

class Puzzle:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.numWords = 0
        self.clues = [Clue('', 0, 0, '', '') for _ in range(MAX_WORDS)]
        self.grid = [['_' for _ in range(MAX_COLS)] for _ in range(MAX_ROWS)]

def load_game(filename, game):
    with open(filename, 'r') as file:
        game.rows, game.cols, game.numWords = map(int, file.readline().split())

        for i in range(game.numWords):
            direction, row, col, answer, clue = file.readline().split()
            game.clues[i] = Clue(direction, int(row), int(col), answer, clue)
            game.clues[i].solved = False

        for i in range(game.rows):
            game.grid[i] = ['_' for _ in range(game.cols)]

def solve_clue(game, clue_number, answer):
    index = clue_number - 1

    if game.clues[index].answer == answer:
        game.clues[index].solved = True

        if game.clues[index].direction == 'H':
            for i in range(len(answer)):
                game.grid[game.clues[index].row - 1][game.clues[index].col - 1 + i] = answer[i]
        elif game.clues[index].direction == 'V':
            for i in range(len(answer)):
                game.grid[game.clues[index].row - 1 + i][game.clues[index].col - 1] = answer[i]

        return True
    else:
        return False

def check_answer(clue, user_answer):
    correct_letters = []
    misplaced_letters = []

    for i in range(len(user_answer)):
        if user_answer[i] == clue.answer[i]:
            correct_letters.append(user_answer[i])
        elif user_answer[i] in clue.answer:
            misplaced_letters.append(user_answer[i])

    return correct_letters, misplaced_letters

def all_clues_solved(game):
    return all(clue.solved for clue in game.clues)
