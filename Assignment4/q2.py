import matplotlib.pyplot as plt

def draw_line_from_file():
    x, y = [], []
    with open('test.txt') as file:
        for line in file:
            values = line.split()
            x.append(float(values[0]))
            y.append(float(values[1]))
    plt.plot(x, y)
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('Line Plot from File')
    plt.show()

draw_line_from_file()
