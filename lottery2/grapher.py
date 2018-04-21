import matplotlib.pyplot as plt


def get_data(gram):

    fil = open(str(gram)+'.txt','r')

    data = fil.readlines()

    for x in range(len(data)):
        data[x] = float(data[x])

    return data


def graph(xs, ys, color="black", name=""):

    plt.scatter(xs, ys, color=color)
    plt.plot(xs, ys, color=color, label = name)


def show(title = "",xlabel = "", ylabel=""):
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

