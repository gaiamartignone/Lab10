import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self.archi = DAO.getallarchi()

    def buildgraph3(self, anno):
        G = nx.Graph()
        for archi in self.archi:
            c1 = archi.s1
            c2 = archi.s2
            if archi.anno <= anno:
                G.add_edge(c1, c2)
        return G