import matplotlib.pyplot as plt
import matplotlib.patches as patches

def plot_rect(data, delta=0.4):
    """data is a dictionary, {"Label":(low,hi), ... }
    return a drawing that you can manipulate, show, save etc"""

    yspan = len(data)
    yplaces = [.5+i for i in range(yspan)]
    ylabels = sorted(data.keys())

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_yticks(yplaces)
    ax.set_yticklabels(ylabels)
    ax.set_ylim((0,yspan))

    # min and max in the union of intervals
    low, hi =  data[ylabels[0]]
    for pos, label in zip(yplaces,ylabels):
        start, end = data[label]
        ax.add_patch(patches.Rectangle((start,pos-delta/2.0),end-start,delta))
        if start<low : low=start
        if end>hi : hi=end

    ax.plot((low,hi),(0,0))

    xmin, xmax = ax.get_xlim()
    ax.hlines(range(1,yspan),xmin,xmax)
    ax.grid(axis='x')
    return ax

data = {'test data 1':(1975,1979),
        'test data 2':(1979,1983),
        'test data 3':(1983,1987),
        'test data 4':(1987,1992),
        'test data 5':(1992,1996),
        'test data 6':(1996,1999),
        'test data 7':(1999,2003)}

ax = plot_rect(data)
ax.set_xlabel('test test')
plt.show()