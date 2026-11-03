# Evaluation

Designempfehlung; Methodik [S08](../research/sources.md), Judge-Grenzen [S06](../research/sources.md).

## Baselines

1. Heutiger menschlicher Ablauf mit Vorlage.
2. Einzelner strukturierter LLM-Aufruf mit denselben zulässigen Quellen.
3. Fester Retrieval-/Validierungs-/Freigabe-Workflow mit LLM.
4. Dynamisch steuernder Einzelagent; Multi-Agent erst als weitere Variante.

Separater Memory-Vergleich: direkte Quellensuche / kleine kuratierte Karten / agentengepflegte Karten. Vorbereitungs-, Wartungs- und Indexkosten einschließen. Kein Architekturgewinn allein aus höherem Aufwand oder besseren Quellen ableiten.

Gleicher Informationszugang; explizite Zeit-/Kostenbudgets; mehrere Läufe; getrennte Entwicklungs- und Testfälle. Modell, Prompt, Tools, Harness und Quellenstand pinnen.

## Metriken

| Ebene | Metrik |
|---|---|
| Evidenz | Belegte Aussagen, falsche Zitate, unbelegte Ergänzungen |
| Anforderungen | Übersehene Bedürfnisse, Randfälle, Widersprüche, Prüfbarkeit |
| Entscheidungen | Restriktionsverletzung, begründete Trade-offs, sinnvolle UND unnötige Enthaltung, vermeidbare Rückfragen, verpasste erlaubte Aktionen |
| Aktionen | Richtiger Zielzustand, Duplikate, unerlaubte Writes |
| Mensch | Aktive Zeit aller Rollen, Review-Wartezeit, Unterbrechungen, zusätzliche Reviewer, nachgelagerte Korrekturen; auch abgelehnte Fälle |
| Betrieb | Kosten pro akzeptiertem Ergebnis, Latenz, Wiederholungsstabilität |
| Produkt | Nutzererfolg, Zielerreichung, Nacharbeit; keine Kausalität ohne geeignetes Design behaupten |

## Bewertungsverfahren

- Deterministisch: Schema, Rechte, Referenzen, Zielversion, Endzustand.
- Fachlich: verblindetes PO-/Domänenreview mit Rubrik; mehrere vertretbare Optionen zulassen und Reviewer-Dissens dokumentieren.
- Reviewwirksamkeit: plausible Fehler gezielt einbauen; Entdeckungsrate und falsche Zurückweisung korrekter Vorschläge messen. Ein Freigabeklick ist kein Qualitätsnachweis [S19].
- Gegenfälle: Verbotsfall mit möglichst gleichem erlaubten Fall paaren. Ein immer blockierender Agent darf nicht als gut bestehen.
- Ergebniszustände statt nur Planbefolgung prüfen; auch bereits vorhandene problematische Defaults und Unterlassungsfehler berücksichtigen.
- Modellbasiert: ergänzend; gegen menschliche Urteile kalibrieren.
- Adversarial: Injection, veraltete Daten, gefälschte Freigaben, Timeout nach Write.

## Release-Gates

- Beobachtete unautorisierte Aktionen, Datenabfluss oder falsche Freigaben: Release stoppen.
- Kritische Testfälle müssen bestehen; endliche Tests beweisen keine absolute Sicherheit.
- Qualitätsgrenzen aus Baseline und Fehlerkosten festlegen; keine universellen Prozentwerte erfinden.
- Zeitersparnis nur inklusive Review und Nacharbeit berichten.
- Autonomie nur erhöhen, wenn Nutzen und Risiko gegenüber der vorherigen Stufe gemessen wurden.

## Verständlichkeit und Mockups

- [Formatvergleich](formats.md): gemeinsame Fallinterpretation statt bloßes „verstanden“.
- [Mockupvergleich](mockups.md): gleiche fachliche Information; Text / Text plus Screens / interaktiver Ablauf. Visuelle Fidelity getrennt variieren.
- Aufgabenerfolg, Regelverständnis, Zufriedenheit und irrtümlich zugeschriebene Agentenfähigkeiten separat messen.
- Erstellung/Pflege und Versionskonflikte einbeziehen. Keine Produktivitätszahl aus reiner Verständnisstudie ableiten [S25].

## Produktwirkung auswerten

- Ergebnisstatus: positiv / negativ / unentschieden / nicht auswertbar.
- Methodenabhängig zuerst Datenvalidität, dann Nutzen, Guardrails und betroffene Segmente prüfen [S24].
- Bei A/B-Tests: Zuteilung, Sample-Ratio-Mismatch, wiederholtes Nachsehen und voreiliges Erfolgsstoppen prüfen. Keine Pflicht-RCTs für jede Produktfrage.
- Unpräzises Ergebnis ist kein Nachweis von Nullwirkung. Gesamtgewinn darf Schaden an relevanten Segmenten nicht verbergen.

## Teststatus

`evals/scenarios.json` ist eine Szenariospezifikation, kein ausgeführter Agentenbenchmark.
`python3 scripts/check.py` prüft Repository-Konsistenz, nicht Agentenverhalten.
