# Pilot und offene Entscheidungen

## Erster Use Case

Reales Feedback → belegtes Problem → bestehende Lösung prüfen → kritische Annahme und Alternativen → entscheiden / recherchieren / fragen / klein testen → gegebenenfalls Anforderungsentwurf → Autorisierung → verifizierter Write.

Kundenwunsch ist ein Signal, kein fertiger Lösungsauftrag. Nutzenmessplan und Architekturvergleich vor produktivem Pilot festlegen.

## Einführung

1. Historische anonymisierte Fälle; ohne Schreibrechte.
2. Shadow Mode neben menschlichem PO; keine produktiven Änderungen.
3. Freigegebene Writes in begrenztem Projekt.
4. Begrenzte Routineautonomie nach Qualitäts-/Risikomessung.

## Lebenszyklus statt nur neue Features

Bei fehlender Wirkung auch Stoppen oder geordnete Stilllegung prüfen: reale Nutzung, Kundenabhängigkeiten, Zusagen, Migration, Support- und Betriebskosten. Produktbeschluss, technische Abschaltung und Datenlöschung getrennt autorisieren. Geringe Nutzung allein rechtfertigt keine Löschung [S01][S02].

## Nicht-Ziele

- Vollautonome Produktstrategie und Roadmap.
- Automatische Kunden- und Lieferzusagen.
- Synthetische Nutzer als echte Evidenz.
- Vollständige autonome Sprintplanung.
- Mehragentenensemble ohne Vergleichsmessung.

## Vor Implementierung klären

- Scrum-PO, Product Management oder Requirements Engineering als konkreter Scope?
- Produkt, Zielgruppe, Zielmetrik, Nicht-Ziele?
- Teuerste Fehler und größter heutiger Arbeitsaufwand?
- Verfügbare Quellen und führende Systeme?
- Entscheidungs- und Freigabebefugnisse?
- Datenklassen, Hosting, Löschregeln und Mandantengrenzen?
- Pilot-Baseline, Testfälle und akzeptable Fehlerkosten?

## Build vs Buy

| Angebot | Dokumentiert | Nicht belegt |
|---|---|---|
| Rovo [S12] | Jira-/Confluence-Tools, Erstellung und Änderungen | Wirtschaftlich richtige Prioritäten |
| Linear Agent [S13] | Workspace-/Code-Recherche, Issues/Projekte, Kundenanfragen | Einsparung inklusive Review im eigenen Team |
| Spec Kit [S14] | Spezifikationsbasierter Entwicklungsprozess | Eigenständiger PO oder echte Discovery |

Eigenbau rechtfertigen durch systemübergreifende Evidenz, spezifische Policies, Nachvollziehbarkeit oder eigene Evaluation; nicht nur durch Ticketgenerierung.

Quellen: [Register](../research/sources.md). Keine Produkt-Livetests durchgeführt.
