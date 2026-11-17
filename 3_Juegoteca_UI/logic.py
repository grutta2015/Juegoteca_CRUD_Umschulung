import os

class VideoGame:
    def __init__(self, title, jahr, console):
        self.__title = str(title)
        self.__jahr = str(jahr)
        self.__console = str(console)

    def gettitle(self): return self.__title
    def getjahr(self): return self.__jahr
    def getconsole(self): return self.__console

def load_from_file(filename="videogames_tab.txt"):
    lista = []
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("\t")
                if len(parts) == 3:
                    lista.append(VideoGame(parts[0], parts[1], parts[2]))
    return lista

def save_to_file(lista, filename="videogames_tab.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for g in lista:
            f.write(f"{g.gettitle()}\t{g.getjahr()}\t{g.getconsole()}\n")