# %%
import numpy as np

# %%
def ALL_tic_tac_toe(savefile_name, output = False):
    """
    generate all tic-tac-toe games but,
        doesn't care who starts (X or O)
        doesn't care if theres a win, just fills all the nine squares
        impar numbers stand for the first player
        it's justs all the 9! games
    """
    move = 0
    ith_move = np.array([[0,0,0 , 0,0,0 , 0,0,0], [0,0,0 , 0,0,0 , 0,0,0]])
    
    move = 1
    while move < 9:
        all_games = np.array([0,0,0 , 0,0,0 , 0,0,0])
        list_all_games = [all_games]
        for j in range(1, len(ith_move)):
            for i in range(9):
                if ith_move[j][i] != 0:
                    pass
                else:
                    ith_move[j][i] = move
                    list_all_games.append(ith_move[j].copy())
                    ith_move[j][i] = 0
        ith_move = np.vstack(list_all_games)
        #print("Move " + str(move) + " - OK")
        move += 1    

    move = 9
    last_move = np.where(ith_move[1:] == 0, 9, ith_move[1:])
    #print("Move " + str(move) + " - OK")

    np.savetxt(savefile_name, last_move, delimiter=",", fmt="%d")

    if output:
        return "File saved.", len(last_move)

# %%
def TRUE_tic_tac_toe(savefile_name, output=False):
    """
    remove the games from the set of 9! games where there are wins
    """
    def is_there_a_win(ttt):
        # convert 1D array into 2D array (3 by 3)
        TTT = ttt.reshape(3,3)

        # lines to verify for wins (lines, columns, diagonals)
        lines = np.vstack([TTT, np.transpose(TTT), np.diag(TTT), np.diag(np.fliplr(TTT))])
        
        # check sums to see if there is a winner
        X_vs_O = np.where(lines % 2 == 1, 1, -1)
        sums = np.sum(X_vs_O, axis=1)

        # someone won
        if 3 in np.abs(sums):
            # find the winning move
            last_move = np.max(lines, axis=1)
            last_move[np.abs(sums) != 3] = 10
            w_move = min(last_move)
            if w_move % 2 == 1:
                winner = 1
            else:
                winner = 2
            return True, w_move, winner

        # draw game
        else:
            return False, 0
        

    with open("attachment(1)_alltictactoe.csv", "r") as csvfile:
        rows = [line.strip().split(',') for line in csvfile]

    new_games = []
    for row in rows:
        ttt = np.array(row).astype(int)
        win = is_there_a_win(ttt)
        if win[0]:
            ttt[ttt > win[1]] = 0
            new_games.append(np.array(list(ttt) + [win[2]]))
        else:
            new_games.append(np.array(list(ttt) + [0]))

    processed_games = np.vstack(new_games)
    unique_games = np.unique(processed_games, axis=0)

    np.savetxt(savefile_name, unique_games, delimiter=",", fmt="%d")

    if output:
        return "File saved.", len(unique_games)


