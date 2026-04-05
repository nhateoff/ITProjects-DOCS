# Deployment Strategies — Feature Flag Implementation

## Purpose
Diese Seite erklärt **Feature Flags** als Deployment-Strategie: warum man sie nutzt, welche Kategorien es gibt und was eine gute Implementierung ausmacht.

## Definition
**Feature Flags** (Feature Toggles) sind eine Technik, mit der du Funktionen/Verhalten **zur Laufzeit ein-/ausschalten** oder gezielt für Nutzergruppen freischalten kannst, ohne jedes Mal neu zu deployen. Ziel ist, Releases **risikoärmer** zu machen: Der Code kann bereits enthalten sein, aber das Feature bleibt standardmässig deaktiviert und wird kontrolliert aktiviert.

## Wofür nutzt man Feature Flags?
Je nach Zweck werden Feature Flags in Kategorien eingeteilt (hilft für Naming, Ownership, Cleanup):
- **Release Flags** (Rollout neuer Features)
- **Ops/Operational Flags** (Kill Switches)
- **Experiment Flags** (Tests/Experimente)
- **Permission Flags** (Zugriffssteuerung)

## Gute Implementierung (Kernpunkte)
- **Lifecycle-Regeln:** Ablaufdatum/Cleanup-Plan, um “Flag Technical Debt” zu vermeiden
- **Konsistentes Naming + Metadaten:** klare Namen, Tags, Owner, Zweck, Gültigkeit
- **Targeting & Gradual Rollout:** schrittweise aktivieren (z. B. 5% → 25% → 100%) pro Environment
- **Vendor-agnostische Evaluation:** Abstraktion (z. B. OpenFeature + Provider), Toolwechsel ohne Neuimplementierung
- **Security & Vermeidung von stale flags:** alte/vergessene Flags entfernen (sonst riskante, ungetestete Codepfade)

## Praxis-Hinweis (Repo/CI)
- Flags sollten zentral dokumentiert werden (Single Source of Truth), inkl. Owner + Cleanup.
- Rollout-Schritte und Go/No-Go Kriterien definieren (z. B. Fehlerquote, 404s, Feedback).

## Keywords (Search)
feature flags, feature toggles, release flag, ops flag, kill switch, experiment flag, permission flag, gradual rollout, lifecycle, cleanup, stale flags, flag technical debt, targeting, environments

## PDF
- [PDF: IT Projects – Deployment Strategies](documentation_deployment_strategies.pdf)

## Metadata
- Owner: Nhat Tan Nguyen
- Last reviewed: 03.04.2026
