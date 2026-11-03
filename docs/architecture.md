# Architektur

Referenzdesign, nicht implementiert. Grundlage: [S09–S11](../research/sources.md).

```text
Auftrag
  → Identität / Mandat / Projekt / Ziel prüfen
  → berechtigte Quellen gezielt abrufen
  → Evidenz und Konflikte erfassen
  → Analyse / Rückfrage / Entwurf
  → Schema + Fachprüfung + Policy
  → Einzel-Diff-Freigabe ODER bestehendes Aktionsklassenmandat validieren
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

`received → researching → needs_clarification | drafted → authorization_check → awaiting_approval | authorized → executing → verified | needs_reconciliation | failed`

`authorized` entsteht durch gültige Einzel-Freigabe oder passende vorautorisierte Aktionsklasse, niemals durch Selbstauskunft des Modells.

- Einzel-Freigabe bindet Diff, Zielversion, Evidenzmanifest und Policy-Version. Aktionsklassenmandat bindet erlaubte Felder, Vorbedingungen, Nebenwirkungen, Budget und Ablauf/Widerruf; jeder konkrete Write wird dagegen geprüft.
- Vor Ausführung zusätzlich Nutzungsrechte und entscheidungsrelevante Quelländerungen prüfen. Unverändertes Zielobjekt heilt widerrufene Entscheidungsgrundlage nicht.
- Server authentifiziert Identität/Mandat; das Modell darf keinen frei gewählten Principal an Tools übergeben.
- Timeout nach Write → `needs_reconciliation`, nicht blind erneut ausführen.
- Checkpoint-Replay garantiert kein Exactly-once im Zielsystem [S10].
- Abbruch: Budget, Zeit, Iterationslimit oder fehlendes Mandat. Tatsachenunsicherheit → Recherche/Test; legitimer Zielkonflikt → zuständige Entscheidung; kein pauschaler Abbruch bei jeder offenen Frage.
- Fehlende Befugnis ist nicht durch kleine Experimente oder Zeitdruck überbrückbar.
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
- `execute_authorized_change(authorization_ref, operation_id, expected_version)`
- `verify_target(operation_id)`

Namen sind Schnittstellenvorschläge, keine vorhandene API.
