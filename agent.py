import numpy as np

class QLearningAgent:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.q_table = {}
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
    
    def get_state(self, board):
        return tuple(board)
    
    def choose_action(self, state, available_actions):
        if np.random.uniform(0, 1) < self.epsilon:
            return np.random.choice(available_actions)
        q_values = [self.q_table.get((state, a), 200) for a in available_actions]
        #print(f"Q değerleri: {q_values}")
        max_q = max(q_values)

        return np.random.choice([a for a, q in zip(available_actions, q_values) if q == max_q])
    
    def update_q_table(self, state, action, reward, next_state):
        next_q_values = [self.q_table.get((next_state, a), 0) for a in range(9)]
        max_next_q = max(next_q_values)
        old_q_value = self.q_table.get((state, action), 0)
        new_q_value = old_q_value + self.alpha * (reward + self.gamma * max_next_q - old_q_value)
        self.q_table[(state, action)] = new_q_value
    
    def save_q_table(self, filename):
        np.save(filename, self.q_table)
    
    def load_q_table(self, filename):
        self.q_table = np.load(filename, allow_pickle=True).item()
