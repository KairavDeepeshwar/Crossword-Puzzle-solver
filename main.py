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

def print_puzzle(game):
    print("\nCurrent Puzzle:\n")
    print("     ", end="")
    for i in range(1, game.cols + 1):
        print(f"{i} ", end="")
    print("\n   -----------")
    for i in range(game.rows):
        print(f"{i + 1}  | ", end="")
        for j in range(game.cols):
            print(f"{game.grid[i][j]} ", end="")
        print()

def print_unsolved_clues(game):
    print("\nUnsolved Clues:\n------------------------")
    print("#\tDirection\tRow/Col\tClue")

    for i, clue in enumerate(game.clues, start=1):
        if not clue.solved:
            print(f"{i}:\t{clue.direction}\t\t{clue.row} / {clue.col}\t{clue.clue}")

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

if __name__ == "__main__":
    game = Puzzle()
    filename = "C:\\Users\\meera\\Documents\\BTech CSE spl. AIML\\VS code\\DSA Project\\crossword_puzzle.txt"

    try:
        load_game(filename, game)
        print(f"Loading game file {filename}")
        print(f"Game is {game.rows} rows x {game.cols} cols with {game.numWords} words")

        print_puzzle(game)
        print_unsolved_clues(game)

        while True:
            clue_number = int(input("\nEnter clue to solve, or -1 to exit: "))

            if clue_number == -1:
                break

            answer = input("Enter your solution: ").upper()

            if solve_clue(game, clue_number, answer):
                print("Correct answer")
            else:
                print("Wrong answer")
                correct_letters, misplaced_letters = check_answer(game.clues[clue_number - 1], answer)
                if correct_letters:
                    print(f"Correctly matched letters: {', '.join(correct_letters)}")
                else:
                    print("No letters are correctly matched")
                if misplaced_letters:
                    print(f"Letters available but wrongly matched: {', '.join(misplaced_letters)}")
                else:
                    print("No letters are available but wrongly matched")

            print_puzzle(game)
            print_unsolved_clues(game)

        print("Game over, you win!")
        print_puzzle(game)

    except Exception as e:
        print(f"An error occurred: {e}")
