from game import TicTacToe
from agent import QLearningAgent
from tqdm import tqdm
import random
import numpy as np

def train_agent(episodes,agent1=None,agent2=None):
    env = TicTacToe()
    agent_black = QLearningAgent()
    agent_white = QLearningAgent()

    if agent1 != None:
        agent_black.load_q_table(filename=agent1)
        print(f"Q table loaded from {agent1}")
    if agent2 != None:
        agent_white.load_q_table(filename=agent2)
        print(f"Q table loaded from {agent2}")

    for _ in tqdm(range(episodes)):
        state = env.reset()
        done = False
        while not done:
            state = env.board.flatten()
            available_actions = env.get_available_actions()
            action = agent_black.choose_action(agent_black.get_state(state), available_actions)
            next_state, done, winner = env.step(action, player=1)
            reward_black = 1 if winner == 1 else -1 if winner == -1 else 0
            reward_white = -reward_black
            if not done:
                state_white = env.board.flatten() 
                action_white = agent_white.choose_action(agent_white.get_state(state_white), available_actions=env.get_available_actions())
                next_state,done,winner = env.step(action_white, player=-1)
                reward_black = 1 if winner == 1 else -1 if winner == -1 else 0
                reward_white = -reward_black

            #print(f"Güncelleme öncesi bu state,action ve q değeri\n{state.reshape(3,3)}\n {action}\t{agent.q_table.get((agent.get_state(state), action), 'değer yok')}")
            agent_black.update_q_table(agent_black.get_state(state), action, reward_black, agent_black.get_state(next_state))
            agent_white.update_q_table(agent_white.get_state(state_white), action_white, reward_white, agent_white.get_state(next_state))
            #print(f"Güncelleme sonrası bu state,action ve q değeri\n{state.reshape(3,3)}\n {action}\t{agent.q_table.get((agent.get_state(state), action), 'değer yok')}")
            state = next_state
            
    agent_black.save_q_table('q_table_black.npy')
    agent_white.save_q_table('q_table_white.npy')

    

train_agent(700000,'q_table_black.npy','q_table_white.npy')

