# ProjectBasics_ReadMe

# README-File
TEST zur Erstellung einer README.md Datei in GitHub

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




