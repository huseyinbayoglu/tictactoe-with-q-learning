from agent import QLearningAgent
from game import TicTacToe
from time import sleep

game = TicTacToe()
black = QLearningAgent(epsilon=0., alpha=0.5, gamma=1)
black.load_q_table("q_table_black.npy")
#print(black.q_table)


done = False
while not done:   
    state = game.board.flatten()
    action = black.choose_action(state=black.get_state(state), available_actions=game.get_available_actions())
    _,done,_ = game.step(action=action, player=1)
    print(game.board.reshape(3, 3))
    action = int(input("Press your move"))
    _,done,_ = game.step(action=action, player=-1)
