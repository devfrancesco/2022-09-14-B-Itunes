import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self._page = page
        self._page.title = "Esame 14/09/2022 Turno B - iTunes"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT

        self._controller = None

        self._title = None
        self._txt_d = None
        self._dd_album = None
        self._txt_tot = None

        self._btn_crea_grafo = None
        self._btn_analisi_componente = None
        self._btn_set_album = None
        self.txt_result = None

    def load_interface(self):
        self._title = ft.Text("Esame 14/09/2022 iTunes - Turno B", color="blue", size=24)
        self._page.controls.append(self._title)

        self._txt_d = ft.TextField(label="Durata (d)", hint_text="Inserisci la durata in secondi", width=300)
        self._btn_crea_grafo = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handleCreaGrafo,
                                                 width=200)

        row1 = ft.Row([self._txt_d, self._btn_crea_grafo],
                      alignment=ft.MainAxisAlignment.CENTER,
                      vertical_alignment=ft.CrossAxisAlignment.END)
        self._page.controls.append(row1)

        self._dd_album = ft.Dropdown(label="Album (a1)", hint_text="Seleziona un album dal grafo", width=300)
        self._btn_analisi_componente = ft.ElevatedButton(text="Analisi Componente",
                                                         on_click=self._controller.handleAnalisiComponente, width=200)

        row2 = ft.Row([self._dd_album, self._btn_analisi_componente],
                      alignment=ft.MainAxisAlignment.CENTER,
                      vertical_alignment=ft.CrossAxisAlignment.END)
        self._page.controls.append(row2)

        self._txt_tot = ft.TextField(label="Soglia (TOT)", hint_text="Inserisci la soglia in secondi", width=300)
        self._btn_set_album = ft.ElevatedButton(text="Set di Album", on_click=self._controller.handleSetAlbum,
                                                width=200)

        row3 = ft.Row([self._txt_tot, self._btn_set_album],
                      alignment=ft.MainAxisAlignment.CENTER,
                      vertical_alignment=ft.CrossAxisAlignment.END)
        self._page.controls.append(row3)

        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)

        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()