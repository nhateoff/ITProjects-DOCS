# Deployment Strategies — Rollback Capabilities (GitHub)

## Purpose
Diese Seite beschreibt **Rollback Capabilities**: wie du nach einem schlechten Deploy schnell auf einen stabilen Stand zurückkehrst – speziell im GitHub-Kontext.

## Definition
Rollback Capabilities bedeuten: Von einem schlechten Deploy schnell auf einen **“last known good”** Stand zurückkehren – reproduzierbar und mit minimalem Risiko.

## Zwei Ebenen in GitHub
### 1) Rollback auf Code-Ebene (Git)
- **Revert statt History umschreiben:** Rollback als **neuer Commit**, der fehlerhafte Änderungen rückgängig macht (z. B. via `git revert`).

### 2) Rollback auf Deployment-Ebene (GitHub Actions)
- **Deployment History** hilft, zu sehen, welche Version wann deployed wurde.
- Empfohlen ist ein **Rollback-Workflow**, der eine bestimmte Version (Tag oder Commit SHA) erneut deployt.

### 3) Rollback via Feature Flags / Kill Switch (Runtime)
- Wenn ein neues Feature Probleme macht, wird es sofort deaktiviert, ohne neuen Deploy. Dies ist schnell, und reduziert Impact sofort

### 4) Rollback auf Datenbank-/Daten-Ebene (Schema & Data)
- Wenn ein Deploy DB-Änderungen oder Daten korrumpiert, reicht ein Code-Rollback nicht
- Rollback Optionen: Backup/Restore, Rollback/Down-Migration, Forward Fix

## Praktisches Rollback-Setup
1. **Last Known Good definieren**
   - Stabile Version festlegen
   - Beispiel: eine **Stable-Branch** oder ein **Tag** (v1.0.0)

2. **Rollback-Workflow in GitHub Actions**
   - Manuell startbarer Workflow (`workflow_dispatch`)
   - Input: Tag oder Commit SHA
   - Workflow deployt genau diese stabile Version neu

## Keywords (Search)
rollback, last known good, git revert, deployment history, github actions, rollback workflow, stable branch, tag, commit sha, recovery

## PDF
- [PDF: IT Projects – Deployment Strategies](documentation_deployment_strategies.pdf)

## Metadata
- Owner: Nhat Tan Nguyen
- Last reviewed: 03.04.2026
