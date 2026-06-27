import flet as ft


class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def handleCreaGrafo(self, e):
        self._view.txt_result.controls.clear()
        d = self._view._txt_d.value
        if d == "":
            self._view.create_alert("Scrivi un valore per d")
            return
        try:
            floatD = int(d)
        except ValueError:
            self._view.create_alert("Scrivi un valore numerico per d")
            return
        self._model.buildGraph(floatD)
        nNodes, nEdges = self._model.getGraphDetails()
        self._view.txt_result.controls.append(ft.Text("grafo creato"))
        self._view.txt_result.controls.append(ft.Text(f"Nodi: {nNodes}, Archi: {nEdges}"))
        self._view._dd_album.clean()
        self.fillDDAlbum()
        self._view.update_page()

    def handleAnalisiComponente(self, e):
        self._view.txt_result.controls.clear()
        a1_id = self._view._dd_album.value
        if a1_id is None:
            self._view.create_alert("Seleziona un album")
            return
        lunghezza, somma = self._model.getInfoConnessa(int(a1_id))
        if lunghezza == 0:
            self._view.txt_result.controls.append(ft.Text("Nessuna componente connessa trovata."))
            self._view.update_page()
            return
        self._view.txt_result.controls.append(ft.Text(f"Componente connessa lunga {lunghezza} con {somma} brani"))
        self._view.update_page()

    def handleSetAlbum(self, e):
        d = self._view._txt_tot.value
        if d == "":
            self._view.create_alert("Seleziona una soglia")
            return
        try:
            D = float(d)
        except ValueError:
            self._view.create_alert("Seleziona un valore numerico")
            return
        a1_id = self._view._dd_album.value
        if a1_id is None:
            self._view.create_alert("Seleziona un album")
            return
        path = self._model.getPath(D, int(a1_id))
        if path == []:
            self._view.txt_result.controls.append(ft.Text("Nessun set di album trovato"))
            self._view.update_page()
            return
        for a in path:
            self._view.txt_result.controls.append(ft.Text(a))
        self._view.update_page()

    def fillDDAlbum(self):
        album = self._model._album
        for a in album:
            self._view._dd_album.options.append(ft.dropdown.Option(key=a.AlbumId, text=a))
        self._view.update_page()