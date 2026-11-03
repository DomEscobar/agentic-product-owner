# Repo-Memory / Wiki

Designempfehlung. Wiki = Produktgedächtnis; Harness = Regeln, Tools, Laufsteuerung und Evaluation.

## Zielstruktur im späteren Produkt-Repository

```text
AGENTS.md
product/
  index.md
  goals.md
  domain/
  evidence/
  opportunities/
  decisions/
  requirements/
  experiments/
  open-questions.md
agent/
  policies/
  schemas/
  evals/
```

## Informationsvertrag

| Feld | Zweck |
|---|---|
| id / type | Stabile Referenz; Beobachtung, Hypothese, Regel, Entscheidung |
| status | draft, confirmed, contested, superseded, rejected |
| scope | Produkt, Segment, Zeitraum, Version |
| sources | Originalquelle und konkrete Fundstelle |
| owner / approved_by | Zuständigkeit; keine selbst erfundene Freigabe |
| derived_from | Ableitungskette; keine unabhängige Bestätigung vortäuschen |
| supersedes / superseded_by | Historie und gültiger Stand |
| affected_items | Tickets, Anforderungen, Codebereiche |
| review_trigger | Anlass für Neubewertung |
| sensitivity | Zulässiger Speicher- und Zugriffskontext |

## Lesezyklus

1. Mandat und geschützte Regeln laden.
2. Index und gültige Ziele lesen.
3. Nur relevante Wissensseiten abrufen.
4. Status, Scope, Quellenstand und Zugriff prüfen.
5. Für folgenreiche Entscheidungen die Originale nachprüfen.

## Schreibzyklus

1. Bestehenden Eintrag suchen.
2. Quelle und Datenklassifikation prüfen.
3. Beobachtung von Ableitung trennen.
4. Konflikte markieren; nicht still auflösen.
5. Änderung samt betroffenen Referenzen vorschlagen.
6. Erforderliche fachliche Freigabe einholen.
7. Versionieren, Index aktualisieren, Konsistenz prüfen.

## Grenzen

- Keine privaten Rohinterviews und Kundendaten standardmäßig in Git.
- Git-Löschung entfernt weder Historie noch externe Indizes.
- Keine Secrets, Chatsammlungen, Freigabetokens oder flüchtigen Run-Zustände.
- Keine automatische Änderung von AGENTS.md, Policies und Tests durch den Wissenspflegeprozess.
- Neuere Quelle ist nicht automatisch verbindlicher.
- Ein Merge ohne Textkonflikt kann einen fachlichen Konflikt enthalten.
- Ein Branch-Entwurf ist keine beschlossene Strategie.
- Ein Merge ist kein Beleg, dass die Funktion veröffentlicht wurde.
- Zusammenfassung verliert Details: Originalfundstellen erhalten.
- Wiederholung desselben Claims erhöht seine Evidenz nicht.

## Wartung

- Broken Links, fehlende Quellen und unaufgelöste Konflikte prüfen.
- Veraltete Entscheidungen markieren; nicht aus der Historie entfernen.
- Ableitungen bei Quellenänderung invalidieren oder zur Prüfung stellen.
- Duplikate zusammenführen, große Seiten thematisch teilen.
- Überholtes archivieren; gezieltes Retrieval statt vollständigem Wiki im Kontext.
- Relevanz und Abrufqualität evaluieren, nicht nur Anzahl gespeicherter Seiten.

## Git-Review

- Fachwissen und Harness-Änderungen getrennte Reviews.
- Geschützte Regeln über extern durchgesetzte Rechte absichern.
- CODEOWNERS allein ist keine durchgesetzte Branch Protection.
- Dieses Forschungsrepo richtet keine produktiven Rechte oder Branch-Protection-Garantien ein.
