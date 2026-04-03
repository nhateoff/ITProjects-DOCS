# Feature Flags — Rules (Repo Standard)

Dieses README definiert **nur die Regeln**, damit Feature Flags sauber bleiben: **Naming, Owner, Rollout, Cleanup**.

---

## Regeln

### 1) Naming (Pflicht)
**Key-Format:** `<domain>.<area>.<feature>.<variant?>`  
- nur Kleinbuchstaben/Zahlen/Punkte  
- keine Leerzeichen, keine Umlaute  
- sprechende Keywords (nicht generisch)

[+] `wiki.sidebar.v2`  
[-] `newFeature`, `SidebarV2`, `test1`

### 2) Pflichtfelder pro Flag (Pflicht)
Jede Flag in `feature-flags/flags.yml` muss mindestens haben:
- `key`, `type`, `default`
- `category` (release/ops/experiment/permission)
- `purpose` (1–2 Sätze)
- `owner` (z. B. `@nhateoff`)
- `tags` (2–5 Keywords)
- `environments` (mind. dev + prod)
- `expires_on` **oder** `review_on`
- `cleanup_plan`

### 3) Default & Safety
- Default muss **sicher** sein (bei neuen Features i. d. R. `false`).
- Wenn Flag nicht gefunden wird → **Default** verwenden.

### 4) Rollout (Standard)
Phased rollout ist Standard:
- 10% → 25% → 50% → 100%
- Bei Problemen: Rollout stoppen oder auf 0% zurück (Rollback/Kill-Switch je nach Setup).

### 5) Cleanup (Pflicht)
- **Release Flags werden entfernt**, sobald 100% stabil (z. B. 14 Tage stabil).
- Entfernen heisst: aus Registry + Codepfaden + Doku raus.

---

## Checkliste (vor Merge)
- [ ] Key entspricht Naming-Konvention
- [ ] Kategorie gesetzt (release/ops/experiment/permission)
- [ ] Owner gesetzt
- [ ] Purpose klar (1–2 Sätze)
- [ ] Default sicher gewählt
- [ ] dev + prod Konfiguration vorhanden
- [ ] `expires_on` oder `review_on` gesetzt
- [ ] Rollout-Plan kurz definiert (mind. Prozent-Schritte)
- [ ] Cleanup-Plan vorhanden (wann & wie entfernen)
- [ ] Verify/Monitoring klar (woran erkenne ich Erfolg?)

---

## Beispiel: `wiki.sidebar.v2` (Release Flag)

```yaml
flags:
  - key: "wiki.sidebar.v2"
    type: "boolean"
    default: false
    category: "release"
    purpose: "Rollout der neuen Wiki Sidebar v2 (Navigation/UX)."
    owner: "@nhateoff"
    tags: ["wiki", "sidebar", "navigation", "ux"]
    environments:
      dev:
        enabled: true
        rollout: 100
      prod:
        enabled: true
        rollout: 10
    expires_on: "2026-05-31"
    cleanup_plan: "Nach 100% Rollout und 14 Tagen stabil: Flag + Codepfade entfernen."
