import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._album = []
        self._idMApA = {}
        self._path = []

    def getPath(self, d, id):
        source = self._idMApA[id]
        somma = source.Media/60
        if somma > d:
            return []
        componenti = list(nx.node_connected_component(self._graph, source))
        parziale = [source]
        self._ricorsione(parziale, d, componenti, somma, 0)
        return self._path

    def _ricorsione(self, parziale, d, componenti, somma, pos):
        if len(parziale) > len(self._path):
            self._path = list(parziale)
        for i in range(pos, len(componenti)):
            connesso = componenti[i]
            if connesso not in parziale:
                nuova_somma = connesso.Media/60 + somma
                if nuova_somma <= d:
                    parziale.append(connesso)
                    self._ricorsione(parziale, d, componenti, nuova_somma, i + 1)
                    parziale.pop()

    def buildGraph(self, d):
        self._graph.clear()
        self._idMApA = {}
        self._album = DAO.getAllAlbum(d)
        for a in self._album:
            self._idMApA[a.AlbumId] = a
        self._graph.add_nodes_from(self._album)
        allEdges = DAO.getAllEdges(d, self._idMApA)
        for e in allEdges:
            self._graph.add_edge(e[0], e[1])

    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)

    def getInfoConnessa(self, id):
        source = self._idMApA[id]
        componenti = list(nx.node_connected_component(self._graph,source))
        totBrani = sum(a.NBrani for a in componenti)
        return len(componenti), totBrani

    def getConnessa(self, id):
        source = self._idMApA[id]
        componenti = list(nx.node_connected_component(self._graph, source))
        return componenti


