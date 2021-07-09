import numpy as np

def main(m0=2, m=2, r=1):
    import networkx as nx

    G = nx.Graph()
    nx.add_path(G, [3, 5, 4, 1, 0, 2, 7, 8, 9, 6])
    nx.add_path(G, [3, 0, 6, 4, 2, 7, 1, 9, 8, 5])

    nx.nx_agraph.view_pygraphviz(G, prog='fdp')
    # assert m0 >= m

    # edges = [[] for _ in range(m0)]
    # edges_sum = 0

    # while True:
    #     new = len(edges)
    #     vs = []
    #     p = [len(us)/edges_sum for us in edges]
    #     while True:

    #         [to] = np.random.choice(len(edges), 1, )



    #     if input("press q to quit") == "q":
    #         break


if __name__ == "__main__":
    main()