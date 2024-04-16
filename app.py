from flask import Flask, render_template, request, jsonify
from solver import Puzzle, load_game, solve_clue, check_answer
import os
from solver import all_clues_solved

app = Flask(__name__)

# Initialize the game object
game = Puzzle()

# Load the game from the crossword_puzzle.txt file
current_directory = os.path.dirname(os.path.abspath(__file__))
load_game(os.path.join(current_directory, "crossword_puzzle.txt"), game)

@app.route('/')
def index():
    return render_template('index.html', game=game)

@app.route('/check_answer', methods=['POST'])
def check_answer_route():
    clue_number = int(request.form['clue_number'])
    user_answer = request.form['user_answer'].upper()

    if solve_clue(game, clue_number, user_answer):
        return jsonify({"result": "correct"})
    else:
        correct_letters, misplaced_letters = check_answer(game.clues[clue_number - 1], user_answer)
        return jsonify({
            "result": "wrong",
            "correct_letters": correct_letters,
            "misplaced_letters": misplaced_letters,
            "clue": game.clues[clue_number - 1].to_dict()  # Convert Clue to dictionary
        })
    
@app.route('/check_game_over', methods=['POST'])
def check_game_over():
    if all_clues_solved(game):
        for i in range(game.rows):
            for j in range(game.cols):
                if game.grid[i][j] == '_':
                    game.grid[i][j] = 'X'
        return jsonify({"game_over": True})
    else:
        return jsonify({"game_over": False})

if __name__ == '__main__':
    app.run(debug=True)