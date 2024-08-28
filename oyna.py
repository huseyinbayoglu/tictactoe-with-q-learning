from agent import QLearningAgent
from game import TicTacToe
from time import sleep
from utils import visualize_tic_tac_toe
import matplotlib.pyplot as plt

def on_click(event):
    global game

    # Tıklanan noktanın koordinatlarını al
    x, y = event.xdata, event.ydata
    print(f"X: {x}, Y: {y}")

    # Eğer geçerli bir hücreye tıklandıysa
    if x is not None and y is not None:
        j = int(x + 0.5)
        i = int(2 - y + 0.5)
        print(f"Satır: {i}, Sütun: {j}")

        # Hücre boşsa, geçerli oyuncunun sembolünü ekle
        if game.board[i, j] == 0:
            game.board[i, j] = -1
            print(game.board)
            visualize_tic_tac_toe(game.board, ax)


game = TicTacToe()
black = QLearningAgent(epsilon=0., alpha=0.5, gamma=1)
black.load_q_table("q_table_black.npy")
#print(black.q_table)

fig, ax = plt.subplots(figsize=(6, 6))
done = False
while not done:   
    state = game.board.flatten()
    action = black.choose_action(state=black.get_state(state), available_actions=game.get_available_actions())
    _,done,_ = game.step(action=action, player=1)
    visualize_tic_tac_toe(game.board.reshape(3, 3), ax)

    # Tıklama olayını yakala
    cid = fig.canvas.mpl_connect('button_press_event', on_click)
    sleep(4)

