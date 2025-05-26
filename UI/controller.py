import flet as ft
import networkx as nx


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        self._view._txt_result.controls.clear()
        anno = self._view._txtAnno.value
        if anno is None or anno == "":
            self._view.create_alert("Inserire un anno")
            return
        try:
            anno_int = int(anno)
        except ValueError:
            self._view.create_alert("La distanza deve essere un numero intero")
            return
        if anno_int<1816 or anno_int>2016:
            self._view.create_alert("anno inserito non compreso negli estremi")
            return
        else:
            grafo = self._model.buildgraph3(anno_int)
            self._view._txt_result.controls.append(ft.Text("Grafo correttamente creato!"))
            self._view._txt_result.controls.append(ft.Text(f"Il grafo contiene {nx.number_connected_components(grafo)} componenti connesse."))
            self._view._txt_result.controls.append(ft.Text(f"di seguito il dettaglio sui nodi"))
            for stato, grado in sorted(grafo.degree()):
                self._view._txt_result.controls.append(ft.Text(f"{stato}: {grado} stati confinanti"))
            self._view.update_page()
