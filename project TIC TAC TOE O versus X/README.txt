# Tic Tac Toe (Python Console Game)

### Project Goal
The goal of this project is to demonstrate primary Python basics  such as functions, list indexing, input validation, and control flow by building a simple two-player Tic Tac Toe game.

## About
This is a console-based Tic Tac Toe game where two players alternate turns placing their markers (X or O) on a 3x3 board. The game checks for wins or draws and announces the result.

## Python Concepts Demonstrated
- **Functions:** The code is organized into reusable functions like `display_board()`, `playerinput()`, `playerturn()`, and `check_winner()`.
- **Lists and Indexing:** The game board is represented as a list with 10 elements (index 0 unused) to simplify position mapping.
- **Input Validation:** Players must enter valid positions (numbers 1-9) that aren’t already occupied.
- **Control Flow:** Loops and conditionals handle turn-taking, input checking, and game status evaluation (win/draw).

## How to Run
1. Make sure Python 3.x is installed on your computer.
2. Download the `milestone.py` file.
3. Run the game in your terminal or command prompt:
```bash
python tictactoe.py

Made by Artem.