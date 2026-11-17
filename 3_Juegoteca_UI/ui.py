import customtkinter as ctk
from tkinter import messagebox, ttk
import config
import logic

class JuegotecaGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(config.TXT_TITULO_APP)
        self.geometry("950x550")
        ctk.set_appearance_mode(config.COLOR_FONDO)
        ctk.set_default_color_theme(config.TEMA_ACCENTO)

        self.inventar_list = logic.load_from_file()

        # Layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ---- PANEL IZQUIERDO (Controles) ----
        self.sidebar = ctk.CTkFrame(self, width=280, corner_radius=10)
        self.sidebar.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        ctk.CTkLabel(self.sidebar, text=config.TXT_LABEL_ADD, font=config.FUENTE_TITULO).pack(pady=20)

        self.entry_title = ctk.CTkEntry(self.sidebar, placeholder_text=config.TXT_PLACEHOLDER_TITLE)
        self.entry_title.pack(pady=10, padx=20, fill="x")

        self.entry_jahr = ctk.CTkEntry(self.sidebar, placeholder_text=config.TXT_PLACEHOLDER_JAHR)
        self.entry_jahr.pack(pady=10, padx=20, fill="x")

        self.entry_console = ctk.CTkEntry(self.sidebar, placeholder_text=config.TXT_PLACEHOLDER_CONSOLE)
        self.entry_console.pack(pady=10, padx=20, fill="x")

        self.btn_add = ctk.CTkButton(self.sidebar, text=config.TXT_BTN_ADD, 
                                     fg_color=config.COLOR_BOTON_GUARDAR, command=self.add_game)
        self.btn_add.pack(pady=(20, 10), padx=20, fill="x")

        # Botón eliminar abajo de los inputs en el panel izquierdo
        self.btn_delete = ctk.CTkButton(self.sidebar, text=config.TXT_BTN_DELETE, 
                                        fg_color=config.COLOR_BOTON_ELIMINAR, 
                                        hover_color=config.COLOR_BOTON_ELIMINAR_HOVER, 
                                        command=self.delete_game)
        self.btn_delete.pack(pady=10, padx=20, fill="x")

        # ---- PANEL DERECHO (Tabla) ----
        self.main_content = ctk.CTkFrame(self)
        self.main_content.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.search_entry = ctk.CTkEntry(self.main_content, placeholder_text=config.TXT_SEARCH)
        self.search_entry.pack(pady=10, padx=20, fill="x")
        self.search_entry.bind("<KeyRelease>", self.filter_list)

        self.setup_table()
        self.refresh_table()

    def setup_table(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="#2b2b2b", 
                        foreground="white", fieldbackground="#2b2b2b", 
                        borderwidth=0, font=config.FUENTE_TABLA)
        style.map("Treeview", background=[('selected', '#2fa572')])

        self.table = ttk.Treeview(self.main_content, columns=("Title", "Year", "Console"),
                                  show="headings")
        self.table.heading("Title", text="Título")
        self.table.heading("Year", text="Año")
        self.table.heading("Console", text="Consola")
        self.table.pack(expand=True, fill="both", padx=20, pady=20)

    def add_game(self):
        t, j, c = self.entry_title.get().strip().title(), self.entry_jahr.get().strip(), self.entry_console.get().strip().title()
        
        if t and c and len(j) == 4 and j.isdigit():
            nuevo = logic.VideoGame(t, j, c)
            self.inventar_list.append(nuevo)
            self.refresh_table()
            self.clear_entries()
            logic.save_to_file(self.inventar_list)
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios y el año debe ser de 4 dígitos.")

    def delete_game(self):
        selected = self.table.selection()
        if not selected:
            messagebox.showwarning("Atención", "Selecciona un juego de la lista.")
            return
            
        index = self.table.index(selected)
        if messagebox.askyesno("Confirmar", "¿Deseas eliminar este juego?"):
            self.inventar_list.pop(index)
            self.refresh_table()
            logic.save_to_file(self.inventar_list)

    def refresh_table(self, data_list=None):
        for item in self.table.get_children(): self.table.delete(item)
        display = data_list if data_list is not None else self.inventar_list
        for g in display:
            self.table.insert("", "end", values=(g.gettitle(), g.getjahr(), g.getconsole()))

    def filter_list(self, event):
        query = self.search_entry.get().lower()
        filtered = [g for g in self.inventar_list if query in g.gettitle().lower()]
        self.refresh_table(filtered)

    def clear_entries(self):
        for e in [self.entry_title, self.entry_jahr, self.entry_console]: e.delete(0, 'end')