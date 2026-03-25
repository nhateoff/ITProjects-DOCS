# Contributing

Danke, dass du zur Dokumentation in **ITProjects-DOCS** beiträgst!  
Dieses Repository ist als **centralized documentation repository** gedacht: Inhalte, Vorlagen, Medien und Standards sind an einem Ort gebündelt, damit alles **konsistent, auffindbar und wartbar** bleibt.

---

## 1) Ziel dieses Repos
- Eine zentrale Wissensbasis für IT-Themen, Guides und Projekt-Dokumentationen
- Einheitliche Struktur und Standards (Templates + Style Guide)
- “Searchable documentation”: Inhalte sollen über GitHub-Suche schnell auffindbar sein

---

## 2) Wo gehört was hin? (Ordner-Guide)
> Wichtig: Git speichert keine leeren Ordner. Lege bei Bedarf eine `.gitkeep` Datei an.

### `guides/`
**Step-by-step Anleitungen / How-tos**  
Beispiele:
- Setup-Anleitungen
- “How to …”-Guides
- Tool-Installationen / Konfigurationen  
➡️ Nutze die Templates aus `templates/` als Ausgangspunkt.

### `concepts/`
**“Finale” Dokumentationen / Abgaben / Exporte**  
Beispiele:
- PDF-Versionen von Dokus
- Zusammenfassungen für Abgaben
- Langform-Dokumente (wenn bewusst als “final” abgelegt)

### `templates/`
**Vorlagen (Templates)** für wiederkehrende Dokumenttypen  
Beispiele:
- How-to Template
- Runbook Template
- Release Notes Template

### `mediafiles/`
**Bilder/Videos/Assets** (Screenshots, Diagramme, etc.)  
➡️ Benenne Dateien sprechend (siehe Style Guide).

### `docs/`
Aktuell beinhaltet dieser Ordner Webfiles (HTML/CSS/JS).  
Wenn du Markdown-Doku für MkDocs/Pages aufbauen willst, nutze zukünftig:
- `docs/index.md` als Start
- `docs/...` für strukturierte Inhalte  
(Bei grösserer Umstrukturierung bitte zuerst kurz im Repo abstimmen.)

### `mkdocs.yml`
Konfiguration für MkDocs (Navigation/Pages). Änderungen daran bitte besonders sorgfältig machen.

---

## 3) Namenskonventionen (Pflicht)
### Dateien & Ordner
- Nutze **underscore**: `reverse_proxy_nginx.md`
- Keine Leerzeichen, keine Sonderzeichen: `ä/ö/ü` vermeiden
- Keine generischen Namen wie `doc1.md`, `final.pdf`, `image.png`


---

## 4) Content-Regeln (Pflicht)
### Einheitliche Seitenstruktur
Neue Inhalte sollen sich an einer Standardstruktur orientieren (siehe `STYLE_GUIDE.md`):
- Purpose → Prerequisites → Steps → Verify → Troubleshooting → Related

### Ein Thema pro Datei
- Lieber mehrere kleine Seiten + Links, statt eine riesige Seite.

### Searchability
- Baue echte Suchbegriffe ein (z. B. `nginx`, `cloudflare`, `ufw`, exakte Fehlermeldungen).
- Fehlertexte **wortwörtlich** in Troubleshooting übernehmen.

---

## 5) Workflow: So trägst du sauber bei
### Option A: Direkt im Repo (einfach)
1. Finde das passende Ziel-Verzeichnis (siehe Punkt 2)
2. Erstelle die Datei basierend auf einem Template aus `templates/`
3. Achte auf Naming (Punkt 3) + Struktur (Punkt 4)
4. Commit Message:
   - Nach deiner Wahl. Es soll schlussendlich für jeden verständlich sein.

### Option B: Pull Request (sauberer für grössere Änderungen)
Empfohlen für:
- neue Strukturen/Ordner
- Änderungen an Templates
- Änderungen an `mkdocs.yml`
- viele Dateien auf einmal

---

## 6) Definition of Done (Checkliste)
Bevor du commitest:
- [ ] Datei ist im richtigen Ordner
- [ ] Dateiname entspricht kebab-case und ist sprechend
- [ ] Seite hat klare Überschriften (H1/H2)
- [ ] Template/Struktur eingehalten
- [ ] Links funktionieren (relative Pfade)
- [ ] Bilder/Assets sind vorhanden und korrekt verlinkt
- [ ] Bei Troubleshooting: Fehlermeldungen exakt übernommen
- [ ] (Optional) “Last reviewed” / Owner gepflegt

---

## 7) Was bitte NICHT ins Repo gehört
- Secrets, Passwörter, Tokens, private Keys
- Interne sensible Daten (Kundendaten, private IPs, interne Links ohne Freigabe)
- Dubletten ohne Mehrwert (bitte verlinken statt kopieren)

---

## 8) Hilfe / Kontakt
Wenn du unsicher bist:
- Starte mit einem Template in `templates/`
- Halte dich an `STYLE_GUIDE.md`
- Oder melde dich allenfalls bei den Devs oder direkt beim PO
