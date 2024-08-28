import numpy as np
import matplotlib.pyplot as plt
import random
from time import sleep

# Function to visualize a Tic-Tac-Toe matrix
def visualize_tic_tac_toe(matrix, ax,pause:float=2.):
    ax.clear()  # Clear the previous plot

    # Draw grid lines
    ax.axhline(0.5, color='black', linewidth=2)
    ax.axhline(1.5, color='black', linewidth=2)
    ax.axvline(0.5, color='black', linewidth=2)
    ax.axvline(1.5, color='black', linewidth=2)

    # Plot each cell with the corresponding symbol
    for i in range(3):
        for j in range(3):
            cell_value = matrix[i, j]
            if cell_value == 1:
                ax.text(j, 2-i, 'X', fontsize=24, ha='center', va='center', color='blue')
            elif cell_value == -1:
                ax.text(j, 2-i, 'O', fontsize=24, ha='center', va='center', color='red')

    # Set limits and aspect
    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(-0.5, 2.5)
    ax.set_aspect('equal')

    # Hide the axes
    ax.axis('off')

    plt.draw()  # Update the plot
    plt.pause(pause)  # Pause to allow visualization

def on_click(event):
    global current_player, matrix

    # Tıklanan noktanın koordinatlarını al
    x, y = event.xdata, event.ydata
    print(f"X: {x}, Y: {y}")

    # Eğer geçerli bir hücreye tıklandıysa
    if x is not None and y is not None:
        j = int(x + 0.5)
        i = int(2 - y + 0.5)
        print(f"Satır: {i}, Sütun: {j}")

        # Hücre boşsa, geçerli oyuncunun sembolünü ekle
        if matrix[i, j] == 0:
            matrix[i, j] = current_player
            current_player *= -1  # Sırayı değiştir
            visualize_tic_tac_toe(matrix, ax)

if __name__ == '__main__':  
    """# Initialize the plot
    fig, ax = plt.subplots(figsize=(6, 6))

    # Example usage:
    matrix1 = np.array([1, -1, 0, 0, 1, -1, 1, 0, -1]).reshape(3, 3)
    visualize_tic_tac_toe(matrix1, ax)
        
    plt.show()  # Keep the plot open after all updates"""

    # Tic-Tac-Toe oyun tahtası
    matrix = np.zeros((3, 3))

    # Oyuncu sırası (1: X, -1: O)
    current_player = 1
    # Şekil ve eksenleri oluştur
    fig, ax = plt.subplots()

    # İlk tahtayı çiz
    visualize_tic_tac_toe(matrix, ax)

    # Tıklama olayını yakala
    cid = fig.canvas.mpl_connect('button_press_event', on_click)

    plt.show()