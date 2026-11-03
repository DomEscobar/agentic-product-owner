# Repo-Memory / Wiki

Designempfehlung. Wiki = Produktgedächtnis; Harness = Regeln, Tools, Laufsteuerung und Evaluation.

**Kein belegter Leistungsgewinn für PO-Arbeit.** Zuerst direkte Quellensuche gegen kleine kuratierte Karten und agentengepflegte Karten testen. Generierte Kontextdateien verbessern Coding-Aufgaben nicht generell [S17]; Verdichtung kann relevante Details verlieren [S18]. Das widerlegt weder notwendige Policies noch gezielten Wissenszugriff. Vollständige Wiki-Automatisierung ist kein Startziel.

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
| epistemic_status | observed / inferred / disputed; keine Freigabe durch richtige Formulierung |
| editorial_status | draft / reviewed |
| decision_status | proposed / approved / rejected / revoked; nur mit echter Autorisierungsreferenz |
| temporal_status | current / stale / superseded; Geltungszeit getrennt von Importzeit |
| access_state | available / unavailable / revoked / quarantined; nicht gleich wahr/falsch |
| scope | Produkt, Segment, Zeitraum, Version |
| sources | Originalquelle und konkrete Fundstelle |
| owner / approved_by | Zuständigkeit; keine selbst erfundene Freigabe |
| derived_from | Ableitungskette; keine unabhängige Bestätigung vortäuschen |
| supersedes / superseded_by | Historie und gültiger Stand |
| affected_items | Tickets, Anforderungen, Codebereiche |
| review_trigger | Anlass für Neubewertung |
| sensitivity | Zulässiger Speicher- und Zugriffskontext |

## Lesezyklus

1. Identität und Mandat serverseitig prüfen; Zugriff auf Regeln, Index und Ziele autorisieren.
2. Nur erlaubte Regeln, Indexteile und gültige Ziele laden.
3. Kandidaten einschließlich Titel/Snippets VOR Retrieval/Modellkontakt autorisieren.
4. Nur relevante erlaubte Seiten abrufen; Status, Scope, Geltungszeit und Quellenstand prüfen. Vor späterer Nutzung Rechte erneut prüfen.
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
- Fachlich überholte nicht-sensitive Entscheidungen historisieren. Datenschutz-/Sicherheitsvorfälle folgen separaten Lösch- und Retentionregeln; keine absolute Aufbewahrungspflicht [S23].
- Bei fachlicher Quellenänderung betroffene Ableitungen zur erneuten Prüfung markieren. Bei Rechteentzug oder Manipulationsverdacht aktive Nutzung blockieren und Entzug auf Ableitungen, Index und Cache anwenden.
- Quellausfall bedeutet nicht Widerlegung; veralteter Inhalt bedeutet nicht automatisch unzulässige Nutzung. Zustände getrennt behandeln.
- Entscheidungserhebliche Änderung nach Freigabe invalidiert die Ausführungsgrundlage auch bei unverändertem Ziel-Ticket.
- Konsolidierung versionieren; Originalfundstellen, Gegenbelege, Segmente, Nenner und Ausnahmen erhalten [S18]. Unterschiedliche Scopes nicht als Duplikate verschmelzen.
- Einmal ingestierte Fremdinstruktionen können später wieder erscheinen: Wissenspflege darf keine Autorisierungsdaten erzeugen; vorgeschlagene Regeln bleiben isolierte Daten bis zur zuständigen Prüfung.
- Duplikate zusammenführen, große Seiten thematisch teilen; neue Inhalte, Referenzen und Index konsistent veröffentlichen.
- Überholtes archivieren; gezieltes Retrieval statt vollständigem Wiki im Kontext.
- Relevanz und Abrufqualität evaluieren, nicht nur Anzahl gespeicherter Seiten.

## Git-Review

- Fachwissen und Harness-Änderungen getrennte Reviews.
- Geschützte Regeln über extern durchgesetzte Rechte absichern.
- CODEOWNERS allein ist keine durchgesetzte Branch Protection.
- Dieses Forschungsrepo richtet keine produktiven Rechte oder Branch-Protection-Garantien ein.
