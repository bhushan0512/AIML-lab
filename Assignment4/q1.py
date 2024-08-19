import matplotlib.pyplot as plt

def draw_line():
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]
    plt.plot(x, y)
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('Line Plot Example')
    plt.show()

draw_line()
