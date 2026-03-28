# Style Guide

Dieser Style Guide definiert die **Standards** für Inhalte in **ITProjects-DOCS**, damit Dokumentation:
- konsistent bleibt
- gut auffindbar ist (searchable)
- schnell gelesen und gepflegt werden kann

---

## 1) Sprache & Ton
- Standard: **Deutsch**
- Schreibstil: **klar, knapp, task-orientiert**
- Aktiv statt Passiv:
  - ✅ “Starte den Service …”
  - ❌ “Der Service wird gestartet …”

---

## 2) Pflicht-Struktur für Dokumentationsseiten
> Für Guides/How-tos in `docs/guides/` und Markdown-Dokus wie auch PDFs in `docs/concepts/`.

### Standard-Template
Jede Seite soll (wenn sinnvoll) diese Abschnitte enthalten:

1. `# Titel`
2. `## Purpose`
3. `## Audience` (optional, aber empfohlen)
4. `## Prerequisites`
5. `## Steps`
6. `## Verify`
7. `## Troubleshooting`
8. `## Related`
9. `## Metadata` (optional)

---

## 3) Überschriften-Regeln
- Pro Datei genau **ein** H1 (`# ...`)
- Unterkapitel mit H2/H3 strukturieren
- Überschriften sollen Suchbegriffe enthalten:
  - ✅ `## Cloudflare SSL Mode`
  - ✅ `## UFW: Port 25565 freigeben`
  - ❌ `## Einstellungen`

---

## 4) Step-by-step Schreibstandard
### Gute Steps sind:
- nummeriert (`Schritt 1, Schritt 2, Schritt 3`)
- jeweils **eine** Aktion pro Schritt

Beispiel:
1. Installiere Abhängigkeiten.
2. Konfiguriere die `config.yml`.
3. Starte den Service.
4. Prüfe den Status im Log.

---

## 5) Codeblöcke & Commands
- Commands immer in Codeblöcken:
```bash
sudo systemctl status nginx
