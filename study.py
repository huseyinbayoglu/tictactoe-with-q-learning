import matplotlib.pyplot as plt

# Tıklama olayını ele alan işlev
def on_click(event):
    # Tıklanan koordinatları al ve noktayı çiz
    ax.plot(event.xdata, event.ydata, 'ro')
    plt.draw()

# Basit bir grafik oluşturma
fig, ax = plt.subplots()
ax.plot([0, 1, 2, 3], [10, 20, 25, 30])

# Tıklama olayını grafik penceresine bağlama
fig.canvas.mpl_connect('button_press_event', on_click)

plt.show()
