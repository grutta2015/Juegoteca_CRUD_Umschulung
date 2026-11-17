import customtkinter as ctk
from tkinter import messagebox, ttk

# --- Lógica de la Clase  ---
class VideoGame:
    def __init__(self, title, jahr, console):
        self.__title = str(title)
        self.__jahr = str(jahr)
        self.__console = str(console)

    def gettitle(self): return self.__title
    def getjahr(self): return self.__jahr
    def getconsole(self): return self.__console

# --- Ventana Principal ---
class JuegotecaGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Juegoteca - Gestión de Videojuegos")
        self.geometry("900x500")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green") # Mantenemos tu estilo verde

        self.inventar_list = []
        self.load_data()

        # Configuración de Layout (2 columnas)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ---- PANEL IZQUIERDO (Entrada de Datos) ----
        self.sidebar = ctk.CTkFrame(self, width=250, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        ctk.CTkLabel(self.sidebar, text="Añadir Juego", font=("Arial", 20, "bold")).pack(pady=20)

        self.entry_title = ctk.CTkEntry(self.sidebar, placeholder_text="Título")
        self.entry_title.pack(pady=10, padx=20, fill="x")

        self.entry_jahr = ctk.CTkEntry(self.sidebar, placeholder_text="Año")
        self.entry_jahr.pack(pady=10, padx=20, fill="x")

        self.entry_console = ctk.CTkEntry(self.sidebar, placeholder_text="Consola/s")
        self.entry_console.pack(pady=10, padx=20, fill="x")

        self.btn_add = ctk.CTkButton(self.sidebar, text="Guardar Juego", command=self.add_game)
        self.btn_add.pack(pady=20, padx=20, fill="x")

        # ---- PANEL DERECHO (Visualización y Búsqueda) ----
        self.main_content = ctk.CTkFrame(self)
        self.main_content.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        # Barra de búsqueda rápida
        self.search_entry = ctk.CTkEntry(self.main_content, placeholder_text="Buscar por título...")
        self.search_entry.pack(pady=10, padx=20, fill="x")
        self.search_entry.bind("<KeyRelease>", self.filter_list)

        # Tabla (Treeview de Tkinter para simplicidad de datos)
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="#2b2b2b", foreground="white", fieldbackground="#2b2b2b", borderwidth=0)
        style.map("Treeview", background=[('selected', '#2fa572')])

        self.table = ttk.Treeview(self.main_content, columns=("Title", "Year", "Console"), show="headings")
        self.table.heading("Title", text="Título")
        self.table.heading("Year", text="Año")
        self.table.heading("Console", text="Consola")
        self.table.pack(expand=True, fill="both", padx=20, pady=10)

        self.btn_delete = ctk.CTkButton(self.main_content, text="Eliminar Seleccionado", fg_color="#ae2626", hover_color="#8a1d1d", command=self.delete_game)
        self.btn_delete.pack(pady=10)

        self.refresh_table()

    # --- Funcionalidades ---

    def add_game(self):
        title = self.entry_title.get().strip().title()
        jahr = self.entry_jahr.get().strip()
        console = self.entry_console.get().strip().title()

        # Añadimos 'console' a la validación
        if title and console and len(jahr) == 4 and jahr.isdigit():
            nuevo_juego = VideoGame(title, jahr, console)
            self.inventar_list.append(nuevo_juego)
            self.refresh_table()
            self.clear_entries()
            self.save_data()
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios y el año debe tener 4 dígitos.")

    def delete_game(self):
        selected_item = self.table.selection()
        if selected_item:
            index = self.table.index(selected_item)
            confirm = messagebox.askyesno("Confirmar", "¿Deseas eliminar este juego?")
            if confirm:
                self.inventar_list.pop(index)
                self.refresh_table()
                self.save_data()
        else:
            messagebox.showwarning("Atención", "Selecciona un juego de la lista.")

    def refresh_table(self, data_list=None):
        for item in self.table.get_children():
            self.table.delete(item)
        
        display_list = data_list if data_list is not None else self.inventar_list
        for game in display_list:
            self.table.insert("", "end", values=(game.gettitle(), game.getjahr(), game.getconsole()))

    def filter_list(self, event):
        query = self.search_entry.get().lower()
        filtered = [g for g in self.inventar_list if query in g.gettitle().lower()]
        self.refresh_table(filtered)

    def clear_entries(self):
        self.entry_title.delete(0, 'end')
        self.entry_jahr.delete(0, 'end')
        self.entry_console.delete(0, 'end')

    def save_data(self):
        with open("videogames_tab.txt", "w", encoding="utf-8") as f:
            for g in self.inventar_list:
                f.write(f"{g.gettitle()}\t{g.getjahr()}\t{g.getconsole()}\n")

    def load_data(self):
        try:
            with open("videogames_tab.txt", "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split("\t")
                    if len(parts) == 3:
                        self.inventar_list.append(VideoGame(parts[0], parts[1], parts[2]))
        except FileNotFoundError:
            self.inventar_list = []

if __name__ == "__main__":
    app = JuegotecaGUI()
    app.mainloop()