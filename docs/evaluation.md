# Evaluation

Designempfehlung; Methodik [S08](../research/sources.md), Judge-Grenzen [S06](../research/sources.md).

## Baselines

1. Heutiger menschlicher Ablauf.
2. Einfacher LLM-Assistent mit denselben Quellen.
3. Agentischer Workflow.

Gleicher Informationszugang; explizite Zeit-/Kostenbudgets; mehrere Läufe; getrennte Entwicklungs- und Testfälle. Modell, Prompt, Tools, Harness und Quellenstand pinnen.

## Metriken

| Ebene | Metrik |
|---|---|
| Evidenz | Belegte Aussagen, falsche Zitate, unbelegte Ergänzungen |
| Anforderungen | Übersehene Bedürfnisse, Randfälle, Widersprüche, Prüfbarkeit |
| Entscheidungen | Restriktionsverletzung, begründete Trade-offs, sinnvolle Enthaltung |
| Aktionen | Richtiger Zielzustand, Duplikate, unerlaubte Writes |
| Mensch | Gesamtzeit inklusive Review/Nacharbeit, wesentliche Korrekturen |
| Betrieb | Kosten pro akzeptiertem Ergebnis, Latenz, Wiederholungsstabilität |
| Produkt | Nutzererfolg, Zielerreichung, Nacharbeit; keine Kausalität ohne geeignetes Design behaupten |

## Bewertungsverfahren

- Deterministisch: Schema, Rechte, Referenzen, Zielversion, Endzustand.
- Fachlich: verblindetes PO-/Domänenreview mit Bewertungsrubrik.
- Modellbasiert: ergänzend; gegen menschliche Urteile kalibrieren.
- Adversarial: Injection, veraltete Daten, gefälschte Freigaben, Timeout nach Write.

## Release-Gates

- Beobachtete unautorisierte Aktionen, Datenabfluss oder falsche Freigaben: Release stoppen.
- Kritische Testfälle müssen bestehen; endliche Tests beweisen keine absolute Sicherheit.
- Qualitätsgrenzen aus Baseline und Fehlerkosten festlegen; keine universellen Prozentwerte erfinden.
- Zeitersparnis nur inklusive Review und Nacharbeit berichten.
- Autonomie nur erhöhen, wenn Nutzen und Risiko gegenüber der vorherigen Stufe gemessen wurden.

## Teststatus

`evals/scenarios.json` ist eine Szenariospezifikation, kein ausgeführter Agentenbenchmark.
`python3 scripts/check.py` prüft Repository-Konsistenz, nicht Agentenverhalten.
