# Juegoteca – Videospiele-Verwaltung in Python

Ein einfaches CRUD-Projekt. Meine erste Annäherung an Python, gemacht als Lernprojekt während meiner Umschulung zum Fachinformatiker für Anwendungsentwicklung.

Das Ziel war nicht nur, dass das Programm funktioniert. Ich wollte mit Klassen (Getter und Setter), Funktionen und Programmlogik arbeiten. Zuerst war alles in einer Datei. Danach habe ich den Code aufgeteilt und in eine Architektur gebracht – einfach, aber trotzdem eine Architektur.

## 
Die Dateien sind nach dem Arbeitsablauf nummeriert:

0_Consola.py – Klassen, Funktionen und Logik wurden aufgebaut.
1_Pre_UI.py – Eine Benutzeroberfläche wurde implementiert.
3_Juegoteca_UI/ – Der Code wurde refaktoriert. Dadurch entstand eine übersichtlichere Architektur, in der alles in die passenden Teile aufgeteilt ist.


## Funktionen

- Videospiele erfassen (Titel, Jahr, Konsole/n)
- Suchen nach Titel (in der Oberfläche live beim Tippen) und in der Konsole auch nach Jahr
- Liste aller Spiele
- Löschen mit Bestätigung
- Speichern in einer Textdatei (`videogames_tab.txt`, Tabulator-getrennt)
- Eingabeprüfung (z. B. Jahr mit 4 Ziffern)

## Entwicklung

Die Dateien sind nach dem Arbeitsablauf nummeriert:

- `0_Consola.py` – Konsolenversion. Klassen, Funktionen und Logik in einer Datei.
- `1_Pre_UI.py` – Erste grafische Oberfläche (customtkinter), weiterhin in einer Datei.
- `3_Juegoteca_UI/` – Überarbeitete Version mit klarer Aufteilung.

## Architektur (`3_Juegoteca_UI/`)

| Datei | Aufgabe |
|---|---|
| `main.py` | Startet das Programm |
| `ui.py` | Oberfläche: Eingabefelder, Tabelle, Suche, Buttons |
| `logic.py` | Klasse `VideoGame`, Laden und Speichern der Datei |
| `config.py` | Farben, Schriften und Texte der Oberfläche |

## Verwendete Konzepte

- **Kapselung:** Die Attribute von `VideoGame` sind privat (`__title`, `__jahr`, `__console`) und nur über Getter erreichbar. In `0_Consola.py` gibt es zusätzlich Setter.
- **Vererbung:** `JuegotecaGUI` erbt von `ctk.CTk`.
- **Trennung der Aufgaben:** Oberfläche, Logik und Konfiguration liegen in getrennten Dateien.
- **Dateizugriff:** Laden und Speichern mit `with open(...)` und Fehlerbehandlung bei fehlender Datei.

  <img width="1432" height="873" alt="image" src="https://github.com/user-attachments/assets/b1d8331b-9aec-47a1-9fb7-d25288a84f7f" />
  <img width="1413" height="860" alt="image" src="https://github.com/user-attachments/assets/0dba1012-bf4a-4e5f-bc80-4a3d5d70d64b" />
  <img width="715" height="691" alt="image" src="https://github.com/user-attachments/assets/66d48695-7a7e-432b-b46a-4671cb2cb59d" />
<img width="666" height="690" alt="image" src="https://github.com/user-attachments/assets/a74514a7-cbca-451c-996c-e14559c89f40" />
<img width="689" height="689" alt="image" src="https://github.com/user-attachments/assets/97b7d09e-27fb-41b3-9044-df6370ac162b" />






