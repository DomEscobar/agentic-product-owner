# Anforderungen

Designempfehlung; Quellenbasis: [S01–S16](../research/sources.md).

P0 = Voraussetzung für einen schreibenden Pilot. P1 = nächste Ausbaustufe. P2 = nur bei gemessenem Bedarf.

| ID | Prio | Fähigkeit | Relevanz | Abnahme |
|---|---|---|---|---|
| R01 | P0 | Produktziel, Zielgruppe, Nicht-Ziele und Mandat kennen | Verhindert beliebige Feature-Erzeugung | Fehlendes Mandat blockiert verbindliche Entscheidungen |
| R02 | P0 | Beobachtung, Interpretation, Hypothese und Entscheidung trennen | Verhindert erfundene Gewissheit | Jeder tragende Claim hat Typ, Quelle/Begründung, Status |
| R03 | P0 | Quellen mit Fundstelle, Version und Zugriff prüfen | Prüfbarkeit und Datenschutz | Keine unberechtigten Quellen; Zitate am Original überprüfbar |
| R04 | P0 | Unklarheiten und Widersprüche erkennen | Weniger falsch spezifizierte Arbeit | Kritische Unklarheit führt zu gezielter Frage, nicht erfundener Antwort |
| R05 | P0 | Scope, Nicht-Ziele und prüfbare Kriterien formulieren | Umsetzbare Anforderungen | Kriterien beschreiben beobachtbares Verhalten und Fehlerfälle |
| R06 | P0 | Bestehendes Backlog und Abhängigkeiten prüfen | Weniger Duplikate und Konflikte | Vor Neuanlage vorhandene Kandidaten prüfen |
| R07 | P0 | Entscheidungsrechte respektieren | Keine unautorisierten Zusagen | Keine eigenmächtigen Sprint-, Budget- oder Kundenzusagen |
| R08 | P0 | Diff-gebundene Freigabe | Verhindert Freigabeausweitung | Ziel, Felder, Version, Identität und Gültigkeit geprüft |
| R09 | P0 | Sichere externe Writes | Verhindert Duplikate und stille Fehler | Operations-ID, Versionsprüfung, Read-back, Wiederanlauf |
| R10 | P0 | Prompt Injection und Datenabfluss begrenzen | Schutz vor fremden Anweisungen | Manipulierte Quellen erweitern keine Rechte und Ziele |
| R11 | P0 | Persistenz und Aktualität | Keine Selbstbestätigung und veralteten Regeln | Quellenänderungen markieren betroffene Claims und Artefakte |
| R12 | P0 | Audit und Evaluation | Fehler nachvollziehbar machen | Modell-/Prompt-/Toolstand, Inputs, Entscheidungen und Endzustand erfasst |
| R13 | P1 | Evidenzgestützte Priorisierung | Bessere Trade-offs | Keine Scores ohne gekennzeichnete Inputs; Restriktionen separat |
| R14 | P1 | Experiment- und Outcome-Loop | Lernen statt Feature-Fabrik | Hypothese, Messplan, Ergebnis und Folgeentscheidung verbunden |
| R15 | P1 | Stakeholderkonflikte aufbereiten | Keine letzte-Nachricht-gewinnt-Logik | Konflikt und zuständige Entscheidungsinstanz sichtbar |
| R16 | P1 | Änderungsfolgen analysieren | Konsistenz über Artefakte | Geänderte Regel findet abhängige Tickets und Kriterien |
| R17 | P2 | Mehrere spezialisierte Agenten | Nur bei Mehrwert | Vorteil gegen budgetgleiches Einzelagentensystem zeigen |
| R18 | P2 | Begrenzte Routineautonomie | Reviewaufwand senken | Nur erlaubte reversible Aktionen nach Pilotmessung |

## Nicht gleichsetzen

- Fertiges Ticket ≠ richtiger Bedarf.
- Grüne Tests ≠ korrekte fachliche Anforderung.
- Implementiert ≠ veröffentlicht ≠ wirksam.
- PO ≠ alleiniger Entscheider über Engineering-Schätzungen und Sprintplan [S01].
- RICE-Confidence ≠ kalibrierte Erfolgswahrscheinlichkeit [S03].
