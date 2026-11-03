# Architektur

Referenzdesign, nicht implementiert. Grundlage: [S09–S11](../research/sources.md).

```text
Auftrag
  → Identität / Mandat / Projekt / Ziel prüfen
  → berechtigte Quellen gezielt abrufen
  → Evidenz und Konflikte erfassen
  → Analyse / Rückfrage / Entwurf
  → Schema + Fachprüfung + Policy
  → konkreten Diff freigeben
  → Zielversion und Rechte erneut prüfen
  → Aktion ausführen
  → Zielsystem zurücklesen
  → Ergebnis dokumentieren / Wirkung beobachten
```

## Komponenten

| Komponente | Zuständigkeit | Nicht zuständig |
|---|---|---|
| Quellenadapter | Berechtigter Abruf, Version, Fundstelle | Fachliche Wahrheit garantieren |
| Wiki | Produktwissen, Evidenzbeziehungen, Entscheidungen | Secrets, Freigabetokens, Retry-Status |
| Orchestrator | Zustandsübergänge, Budgets, Unterbrechungen | Eigene Berechtigungen definieren |
| Policy Engine | Aktion, Scope und Freigabe autorisieren | Durch LLM-Prompt ersetzt werden |
| Executor | Typisierte, begrenzte Aktionen | Freie Shell/HTTP als Standard |
| Operationsjournal | Idempotenz, Wiederanlauf, Read-back | Ticketstatus duplizieren |
| Evaluator | Deterministische Checks und fachliche Bewertung | Selbstauskunft des Agenten glauben |

## Zustände

`received → researching → needs_clarification | drafted → awaiting_approval → approved → executing → verified | needs_reconciliation | failed`

- `approved` ist an Diff und Zielversion gebunden.
- Timeout nach Write → `needs_reconciliation`, nicht blind erneut ausführen.
- Checkpoint-Replay garantiert kein Exactly-once im Zielsystem [S10].
- Abbruch: Budget, Zeit, Iterationslimit, fehlendes Mandat, nicht auflösbarer Konflikt.
- Parallelität: pro Zielobjekt Konfliktkontrolle; keine gegenseitigen unbemerkten Überschreibungen.

## Führende Systeme

- Arbeitselemente: Jira/GitHub/Linear, je nach festgelegtem Vertrag.
- Code und Build: Repository/CI.
- Produktwissen: vereinbarter Wiki-Bereich.
- Freigaben und laufende Operationen: Workflow-Speicher.
- Sensible Rohquellen: zugriffsgeschütztes Quellsystem.

## Tool-Verträge

- `search_evidence(query, project, scope)`
- `read_source(id, version)`
- `find_related_items(problem, project)`
- `propose_change(target, expected_version, patch, evidence_ids)`
- `request_approval(proposal_id)`
- `execute_approved_change(approval_id, operation_id)`
- `verify_target(operation_id)`

Namen sind Schnittstellenvorschläge, keine vorhandene API.
