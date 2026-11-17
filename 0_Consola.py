import msvcrt
import os
import sys


# Activa los códigos ANSI en Windows
os.system('color')  # truco simple para activarlos

VERDE = "\033[92m"   # verde fosforescente
RESET = "\033[0m"

# un verde más brillante/viejo:
# VERDE = "\033[92m"  # verde claro, más "phosphoro"

_print_original = print
def print(*args, **kwargs):
    args = (f"{VERDE}{args[0]}{RESET}",) + args[1:] if args else args
    _print_original(*args, **kwargs)

################################################################
#             - Erstellen, Lesen, Aktualisieren, Löschen -
# Sistema CRUD (Create, Read, Update, Delete) básico, 
# es el corazón de cualquier programa de gestión de inventarios.
# Ein einfaches CRUD-System (Create, Read, Update, Delete) 
# ist das Herzstück eines jeden Bestandsverwaltungsprogramms.

# -----Listas



inventar_list = []
geloeschtes_videogame = []


##___________________KLASSE_________________________
class VideoGame:

    def __init__(self, title, jahr, console):
        self.settitle(title)
        self.setconsole(console)
        self.setjahr(jahr)

    ##--- Setters
    def settitle(self, title):                    
        self.__title = str(title)                 
    
    def setconsole(self, console):
        self.__console = str(console)
            
    def setjahr(self, jahr):
        self.__jahr = str(jahr)
    
    ##--- Getters
    def gettitle(self):
        return self.__title
    
    def getconsole(self):
        return self.__console
    
    def getjahr(self):
        return self.__jahr

##__________________FUNKTIONEN______________________
def getch():
    return msvcrt.getwch()

def jahr_eingabe():
    while True:
        jahr = input("Jahr: ")
        
        # Limpio los espacios 
        sauber_jahr = jahr.strip().replace(" ", "")
        
        # Comprobamos las reglas
        if sauber_jahr.isdigit() and len(sauber_jahr) == 4:
            return (sauber_jahr)  # Si es correcto, el 'return' rompe el bucle y devuelve el valor
        else:
            print("\a✗ Error: Bitte geben Sie eine gültige 4-stellige Jahreszahl ein.")

        # .strip(): Quita espacios "sobrantes" a los lados.
        # .replace(" ", ""): Borra cualquier espacio, incluso si el usuario escribió "2 0 2 2".
        # .isdigit(): Verifica que no haya letras ni símbolos.
        # len(variable) == 4: Asegura que el tamaño sea exactamente de 4 caracteres.

def title_eingabe():
    title = input("Title: ")
    title = title.strip().title()  #quita espacio y mete mayusculas
    return title

def console_eingabe():
    console = input("Console/s: ")
    console = console.strip().title()
    return console

def neues_videogame(title, jahr, console):
    neues_videogame_obj = VideoGame(title, jahr, console)
    inventar_list.append(neues_videogame_obj)

def load():
    global inventar_list

    try:
    
        datei = open("videogames_tab.txt", "r")

        while True:
            text = datei.readline()
            if text == '':  # si no hay más líneas, para
                break
            
            text_index = 0           #  
            character = ''           #  
            
            for i in range(len(text)):
                if text[i] != '\t':
                    character = character + text[i]
                else:
                    text_index = i + 1 # por el tabulador
                    break
            title = character
                                               # zeile durchlaufen  hasta salto de renglon Zeilenumbruch
            character = ''                     # y voy armando titulo, anio, y consola
            for i in range(text_index, len(text)):
                if text[i] != '\t':
                    character = character + text[i]
                else:
                    text_index = i + 1
                    break
            jahr = character

            character = ''
            for i in range(text_index, len(text)):
                if text[i] != '\n':
                    character = character + text[i]
                else:
                    break
            console = character

            videogame = VideoGame(title, jahr, console)
            inventar_list.append(videogame)
            
        datei.close()
    
    except FileNotFoundError:
        inventar_list = []

def save():
     # --- exportar a txt ---
    with open("videogames_tab.txt", "w") as datei_tab:
        for videogame in inventar_list:
            line = str(videogame.gettitle()) + "\t" + str(videogame.getjahr()) + "\t" + str(videogame.getconsole()) + "\n"
            datei_tab.write(line)

    # datei_koma = open ("videogames_komas.csv", "w")

    # for a in videogames_list:
    #     line = a.getkennzeichen() + ", " + a.gethersteller() + ", " + a.getbaujahr() + "\n"
    #     datei_koma.write(line)
    # datei_koma.close()


####   ________________PROGRAMM_______________________
## Aqui va la parte logica
load()

while True:

    r = 50
    print('┌' + '─' * r + '┐')
    print('│' + '  VIDEO JUEGOS'.center(r) + '│')
    print('└' + '─' * r + '┘')
  
    print('┌' + '─' * r + '┐')
    print('│' + '1) VideoGame Eingabe'.ljust(r) + '│')
    print('│' + '2) VideoGame Suchen'.ljust(r) + '│')
    print('│' + '3) VideoGame Liste'.ljust(r) + '│')
    print('│' + '4) VideoGame Löschen'.ljust(r) + '│')
    #print('│' + '5) Liste durch Datei Type'.ljust(r) + '│')
    print('│' + '6) Ende'.ljust(r) + '│')
    print('└' + '─' * r + '┘')
    
    print("--> Bitte wählen: ", end='', flush=True)
    eingabe_option = getch()
    print(eingabe_option)  # para que el número aparezca en pantalla

    match eingabe_option:

        case '1':
            title = title_eingabe()
            jahr = jahr_eingabe()
            console = console_eingabe()

            neues_videogame(title, jahr, console)

        case '2':
            while True:

                r = 50
                print('┌' + '─' * r + '┐')
                print('│' + '  Suchen'.center(r) + '│')
                print('└' + '─' * r + '┘')
            
                print('┌' + '─' * r + '┐')
                print('│' + '1) VideoGame nach Title suchen'.ljust(r) + '│')
                print('│' + '2) VideoGame nach Jahr Suchen'.ljust(r) + '│')
                print('│' + '3) Zurück'.ljust(r) + '│')
                print('└' + '─' * r + '┘')
                
                print("--> Bitte wählen: ", end='', flush=True)
                eingabe_option = getch()
                print(eingabe_option)  # para que el número aparezca en pantalla

                match eingabe_option:
                    case '1':
                        title = title_eingabe()
                        gefunden = False
                        for videogame in inventar_list:   # iterieren (?) aufzählen la lista del inventar
                            if videogame.gettitle() == title:
                                print(f"\n✓ Gefunden!")
                                print(f"Title: {videogame.gettitle()}")
                                print(f"Jahr: {videogame.getjahr()}")
                                print(f"Console/s: {videogame.getconsole()}")
                                gefunden = True
                                break
                        if not gefunden:
                            print(f"\n✗ Kein VideoGame mit Title '{title}' gefunden.")
                            


                    case '2':
                        jahr = jahr_eingabe()
                        gefunden = 0
                        for videogame in inventar_list:
                            if videogame.getjahr() == jahr:
                                gefunden += 1
                                print(f"\n{gefunden}. Titel: {videogame.gettitle()}")
                                print(f"   Jahr: {videogame.getjahr()}")
                                print(f"   Konsole/n: {videogame.getconsole()}")
                        if gefunden == 0:
                            print(f"\n✗ Kein VideoGame mit dem Jahr '{jahr}' gefunden.")
                        else:
                            print(f"\n── {gefunden} VideoGame(s) gefunden ──")

                    case '3':
                        break

                    case _:
                        print("\a\nUngültige Eingabe. Bitte versuchen Sie es erneut.")

        case '3':
            r = 50
            print('┌' + '─' * r + '┐')
            print('│' + '  VideGame Liste'.center(r) + '│')
            print('└' + '─' * r + '┘')

            if inventar_list:                                       # Iterieren, aufzählen (?)
                for i, videogame in enumerate(inventar_list, 1):    # sirve para numerar los elementos de 
                    print(f"\n{i}. Title: {videogame.gettitle()}")  # una lista mientras los recorres. que comienze desde 1
                    print(f"   Jahr: {videogame.getjahr()}")
                    print(f"   Console/s: {videogame.getconsole()}")
            else:
                print("Es sind keine VideoGames in der Liste.")
  
        case '4':
            print("\nTitle des zu löschenden VideoGame: ")
            title = title_eingabe()
            gefunden = False
            
            # Usamos enumerate para tener la posición (i) y el objeto (videogame)
            for i, videogame in enumerate(inventar_list):
                if videogame.gettitle() == title:
                    print(f"\n✓ Gefunden!")
                    print(f"Title: {videogame.gettitle()}")
                    print(f"Jahr: {videogame.getjahr()}")
                    print(f"Console: {videogame.getconsole()}")
                    gefunden = True
                    
                    while True:

                        bestehen = input("\nMöchten Sie löschen (J / N): ")
                        
                        match bestehen.upper(): # .upper() por si escriben 'j' minúscula
                                                    
                            case 'J':
                                # pop(i) extrae el videogame de la lista y lo devuelve
                                geloeschtes_videogame.append(inventar_list.pop(i))
                                
                                # Ahora el videogame vive en 'geloeschtes_videogames'
                                print(f"\n✓ VideoGame mit title '{geloeschtes_videogame[-1].gettitle()}' wurde gelöscht.\n")
                                #[-1] simplemente significa "el último 
                                # elemento de la lista" — que es justamente el que acabas de agregar.
                                break
                            case 'N':
                                print("\nLöschvorgang abgebrochen.")
                                break
                            case _:
                                print(f"\a\nBitte drücken Sie J oder N\n")
                    
                    break
            
            if not gefunden:
                print(f"\n✗ Kein VideoGame mit title '{title}' gefunden.")

        case '6':
            save()
            print("\nAuf Wiedersehen!")
            break

        case _:
            print("\a\nUngültige Eingabe. Bitte versuchen Sie es erneut.")
