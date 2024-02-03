# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# %%
true_games = pd.read_csv("attachment(2)_truetictactoe.csv", names = (list(range(9))) + ["winner"])

# %%
def first_moves_statistics(_withd, _height):
    # create DF: ex.: row[1] = qty of games that start at sqr1, qty of wins1, wins2 and draws
    first_moves = (true_games == 1).sum().to_frame()[:-1]
    winner1 = []
    winner2 = []
    for i in range(9):
        winner1.append(len(true_games[(true_games[i] == 1) & (true_games["winner"] == 1)]))
        winner2.append(len(true_games[(true_games[i] == 1) & (true_games["winner"] == 2)]))
    first_moves["winner1"] = winner1
    first_moves["winner2"] = winner2
    first_moves["draw"] = first_moves[0] - (first_moves["winner1"] + first_moves["winner2"])


    # set figure to draw bar plots
    plt.figure(figsize=(_withd, _height))
    sns.set(style="whitegrid")

    # set barplots for each situaion: winner1, winner2, draw but group them by square of 1st move
    bar_plot = sns.barplot(x=first_moves.index, y='winner1', data=first_moves,
                        color='blue', label='Player1 wins', alpha=0.85)
    sns.barplot(x=first_moves.index, y='winner2', data=first_moves,
                        color='red', label='Player2 wins', alpha=0.85,
                        bottom=first_moves['winner1'])
    sns.barplot(x=first_moves.index, y='draw', data=first_moves,
                        color='green', label='Draw', alpha=0.85,
                        bottom=first_moves['winner1'] + first_moves['winner2'])

    # add percentage to each barplot of wins1, wins2, draw
    for p in bar_plot.patches:
        width, height = p.get_width(), p.get_height()
        x, y = p.get_xy()
        percentage = height / sum(first_moves[['winner1', 'winner2', 'draw']].iloc[int(p.get_x())].values) * 100
        bar_plot.annotate(f'{percentage:.2f}%',
                        (x + width / 2., y + height / 2.),
                        ha='center', va='center', color='white',
                        xytext=(0, 0),
                        textcoords='offset points')

    # set labels, legend and show it
    plt.xlabel('Square of first move')
    plt.ylabel('Qty of games')
    plt.title('First Moves Statistics')
    plt.legend(loc='upper left', bbox_to_anchor=(1.005, 0.995), borderaxespad=0.)
    plt.show()

# %%



