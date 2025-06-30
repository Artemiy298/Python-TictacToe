def display_board(board):
    print(board[7]+'|'+board[8]+'|' + board[9])
    print(board[4]+'|'+board[5]+'|' + board[6])
    print(board[1]+'|'+board[2]+'|' + board[3])

test_board = ['#', 'X', 'O', 'X', 'O','X','O', 'X', 'O', 'X']
display_board(test_board)

def playerinput():
    marker = ''
    while marker != "X" and  marker != "O":
        marker = input("Do you want to be X or O? ").upper()
    player1 = marker 
    if player1 == "X":
        player2 = 'O'
    else:
        player2 = 'X'
    return player1,player2

# THIS IS THE FIX — save returned values here
player1, player2 = playerinput()

def playerturn(board, marker):
    position = 0
    while position not in range(1,10) or board[position] != ' ':
        pos_input = input("Pick a square position you like to (1-9): ")
        if pos_input.isdigit():
            position = int(pos_input)
        else:
            print("Invalid input, enter a number from 1 to 9.")
    board[position] = marker


def check_winner(board, mark):
    winning_combos = [
        (7,8,9), (4,5,6), (1,2,3),  # rows
        (7,4,1), (8,5,2), (9,6,3),  # columns
        (7,5,3), (1,5,9)            # diagonals
    ]
    for combo in winning_combos: 
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == mark:
            return True
    return False

def check_draw(board):
    return ' ' not in board[1:]

def main():
    board = ['#'] + [' '] * 9  # empty board
    player1, player2 = playerinput()
    current_player = player1

    while True:
        display_board(board)
        playerturn(board, current_player)

        if check_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins! 🎉")
            break

        if check_draw(board):
            display_board(board)
            print("It's a draw! 🤝")
            break

        # Switch player
        current_player = player2 if current_player == player1 else player1

if __name__ == "__main__":
    main()