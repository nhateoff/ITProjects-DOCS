# Deployment Strategies — Phased Deployment Approaches (Progressive Delivery)

## Purpose
Diese Seite erklärt **Phased Deployment** (Progressive Delivery): warum man schrittweise ausrollt, was dafür nötig ist und wie du das in deinem MkDocs/GitHub-Pages Projekt praktisch abbildest.

## Definition
Phased Deployment bedeutet, eine neue Version **nicht auf einen Schlag** an alle auszurollen, sondern **schrittweise**. Dadurch bleibt der “Blast Radius” klein und Bugs/Fehler werden früher erkannt.

Ein typischer Ansatz ist der **Canary Release**:
- Start mit einem kleinen Nutzer-/Traffic-Anteil
- stufenweise erhöhen bis 100%

## Was braucht es, damit es funktioniert?
- **Traffic-Steuerung:** Wer bekommt Version A vs. B?
- **Health Checks/Monitoring:** Wann stoppen/rollback?
- **Go/No-Go Kriterien:** z. B. Error-Rate, Latenz, 404

## Praxis in unserem Projekt (MkDocs + Feature Flag)
GitHub unterstützt **Environments** als kontrollierte Deploy-Ziele. Für unser Setup nutzen wir:
- `[dev]`
- `[prod]` (production)

Der Workflow deployt zuerst nach **dev**, dann nach **prod** (idealerweise mit Checks / manueller Freigabe).

### Wie wir “v1 vs v2” abbilden
Wir haben zwei Nav-Versionen:
- `nav_v1.yml`
- `nav_v2.yml`

Da GitHub Pages **kein echtes Traffic-Splitting** (z. B. 10% der Nutzer) bietet, machen wir das staged:
- **dev:** v2 einschalten (`rollout 100`)
- **prod:** v2 ausschalten (`rollout 0`)
- Sobald dev stabil ist: **prod aktivieren** (rollout > 0) → Einstellung in `flags.yml`

## Keywords (Search)
phased deployment, progressive delivery, canary release, blast radius, traffic shifting, monitoring, health checks, go/no-go, environments, dev, prod, rollout, feature flag

## PDF
- [PDF: IT Projects – Deployment Strategies](documentation_deployment_strategies.pdf)

## Metadata
- Owner: Nhat Tan Nguyen
- Last reviewed: 03.04.2026
