# ProjectBasics_ReadMe

# README-File
TEST zur Erstellung einer README.md Datei in GitHub

# Was ist ein README-File und was ist der Zweck davon?
Ein  README-File ist die **Einführungs- und Anleitungsdatei** eines Projekts, welches meist mit diesem Dateinamen versehen wird `README.md`
Es erklärt kurz und verständlich um was es in einem Projekt geht, wie es installiert, gestartet und benutzt wird, sowie im Falle von Unklarheiten wo man Hilfeleistungen und weitere Infos findet. Auf GitHub wird es üblicherweise automatisch auf der Startseite des Repos angezeigt.

**Kurz zusammengefasst: Zweck eines README-Files**
- Orientierung: Was ist das für ein Projekt? Was ist das Ziel davon?
- Projekteinstieg: Was muss gemacht werden um es zu verwenden (usage)
- Erleicherung von Zusammenarbeit: Beantwortung von Fragen wie z.B., wie kann ich es testen? auf was muss ich mich achten? Wo erhalte ich Support?

Um das ganze README-File etwas funktionaler und ansprechender zu gestallten gibt es diverse Funktionen im Markdown (.md). Diese werden mit relativ simplen Zeichenkombinationen ausgeführt. Dazu mehr unter dem  Abschnitt "**Formatierungen im Markdown**".

# Formatierungen im Markdown

## Überschriften

```md
# Titel 
##  Untertitel
###  Normaler Text mit "Titel-Formatierung"
```

**Ergebnis**
# Titel 
## Untertitel
### Normaler Text mit "Titel-Formatierung"

---

## Fett / Kursiv / Inline-Code

```md
**fett**
*kursiv*
`inline-code`
~~durchgestrichen~~
```

**Ergebnis**
**fett**  
*kursiv*  
`inline-code`  
~~durchgestrichen~~

---

## Listen (Aufzählungen)

```md
- 1. Punkt
- 2. Punkt
  - eingezogene Aufzählung

1. Schritt 
2. Schritt 
3. Schritt 
```

**Ergebnis**
- Punkt 1
- Punkt 2
  - Unterpunkt

1. Schritt 
2. Schritt 
3. Schritt 

---

## Links

```md
[GitHub](https://github.com)
[Interner Link (Datei im Repo)](docs/anleitung.md)
In eckiger Klammer geschriebener Teil wird als Ausgabetext definiert
Die normalen Klammern bilden den effektiven "Dateipfad"
```

**Ergebnis**
[GitHub](https://github.com)  
[Interner Link (Datei im Repo)](docs/anleitung.md)

---

## Zitate

```md
> Das ist ein Hinweis/Zitat.
> Es kann mehrere Zeilen haben.
```

**Ergebnis**
> Das ist ein Hinweis/Zitat.  
> Es kann mehrere Zeilen haben.

---

## Trennlinie

```md
---
```

**Ergebnis**
---

---

## Tabellen

```md
| Element | Bedeutung |
|--------|-----------|
| README.md | Anleitung |
| src/ | Code |
```

**Ergebnis**
| x | Y |
|--------|-----------|
| README.md | Anleitung |
| src/ | Code |

---

## Checkboxen (Task List)

```md
- [x] Erledigt
- [ ] Offen
- [ ] Noch zu tun
```

**Ergebnis**
- [x] Erledigt
- [ ] Offen
- [ ] Noch zu tun

---

## Codeblöcke (Befehle/Code)

> Hinweis: Um im README einen Codeblock zu schreiben nutzt man drei Backticks.


````md
```

```
````

**Ergebnis**
```
Beispiel
Beispiel
Beispiel
```

---

## Bilder

```md
![Beschreibung1 (Beschreibung 2)](assets/screenshot.png)
```

**Ergebnis**
![Beschreibung1 (Beschreibung 2)](assets/screenshot.png)

> Hinweis: Das Bild wird nur angezeigt, wenn die Datei wirklich im Repo existiert (z.B. `assets/screenshot.png`).

---

## Eine Zeile NICHT als Überschrift formatieren

```md
\# Das ist keine Überschrift, sondern normaler Text (weil ein Backslash davor ist).
```

**Ergebnis**
\# Das ist keine Überschrift, sondern normaler Text (weil ein Backslash davor ist).




