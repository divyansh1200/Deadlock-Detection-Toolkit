
import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(n, m, alloc):
    G = nx.DiGraph()

    for i in range(n):
        G.add_node(f"P{i}")

    for j in range(m):
        G.add_node(f"R{j}")

    for i in range(n):
        for j in range(m):
            if alloc[i][j] > 0:
                G.add_edge(f"R{j}", f"P{i}")

    nx.draw(G, with_labels=True, node_color='lightblue',
            node_size=2000, font_size=10)
    plt.title("Resource Allocation Graph")
    plt.show()
