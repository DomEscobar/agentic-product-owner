# Anforderungen

Designempfehlung; Quellenbasis: [Register](../research/sources.md); [kritische Gegenprüfung](../research/critical-review.md).

P0 = Mindestvertrag für den jeweiligen Pilot-Scope: Schreibkontrollen nur bei Writes, Datenkontrollen bereits beim Lesen. P1 = Ausbau. P2 = nur bei gemessenem Bedarf. Relevanz beschreibt eine Nutzenhypothese, keinen nachgewiesenen Effekt.

Vor Umsetzungsempfehlungen: Problem, beobachtetes Verhalten, Alternativen (einschließlich Nicht-Bauen), kritischste Annahme und Nutzenmessplan benennen [S02]. Agentik und Wiki sind Architekturhypothesen, keine Voraussetzungen.

| ID | Prio | Fähigkeit | Relevanz | Abnahme |
|---|---|---|---|---|
| R01 | P0 | Produktziel, Zielgruppe, Nicht-Ziele und Mandat kennen | Verhindert beliebige Feature-Erzeugung | Fehlendes Mandat blockiert verbindliche Entscheidungen |
| R02 | P0 | Beobachtung, Interpretation, Hypothese und Entscheidung trennen | Verhindert erfundene Gewissheit | Jeder tragende Claim hat Typ, Quelle/Begründung, Status |
| R03 | P0 | Quellen mit Fundstelle, Version und Zugriff prüfen | Prüfbarkeit und Datenschutz | Keine unberechtigten Quellen; Zitate am Original überprüfbar |
| R04 | P0 | Unsicherheitsursache und passende Folgeaktion bestimmen | Fehlentscheidungen und unnötige Rückfragen reduzieren | Fehlender Nutzerkontext → Frage; zugänglicher Fakt → Suche; Rechnung → Tool; Zielkonflikt → Entscheider; Kompetenzgrenze → begrenzen/eskalieren [S20] |
| R05 | P0 | Scope, Beispiele und prüfbare Kriterien verständlich machen | Umsetzbare Anforderungen | Konkreter Fall und Ausnahme; Beteiligte sagen erwartetes Verhalten voraus; Screens optional bei UI-Frage; keine Satzschablonenpflicht |
| R06 | P0 | Bestehendes Backlog und Abhängigkeiten prüfen | Weniger Duplikate und Konflikte | Vor Neuanlage vorhandene Kandidaten prüfen |
| R07 | P0 | Entscheidungsrechte und Vertretung festlegen | Keine unautorisierten Zusagen | PO: Backlog-Ordnung; Developers: Schätzung/Umsetzungsplan und Sprintauswahl im Austausch; Sprintziel gemeinsam; Sprint-Abbruch beim PO; Releasepolitik separat [S01] |
| R08 | P0 | Konkrete Autorisierung nach einem von zwei Wegen | Keine Ausweitung von Freigabe oder Mandat | Einzel-Diff-Freigabe ODER vorab autorisierte Aktionsklasse; beide an Scope, Version, Evidenzbasis, Policy und Gültigkeit prüfen |
| R09 | P0 | Sichere externe Writes | Verhindert Duplikate und stille Fehler | Operations-ID, Versionsprüfung, Read-back, Wiederanlauf |
| R10 | P0 | Prompt Injection und Datenabfluss begrenzen | Schutz vor fremden Anweisungen | Manipulierte Quellen erweitern keine Rechte und Ziele |
| R11 | P0 | Persistenz und Aktualität | Keine Selbstbestätigung und veralteten Regeln | Quellenänderungen markieren betroffene Claims und Artefakte |
| R12 | P0 | Audit und Evaluation | Fehler nachvollziehbar machen | Modell-/Prompt-/Toolstand, Inputs, Entscheidungen und Endzustand erfasst |
| R13 | P1 | Evidenzgestützte Priorisierung | Bessere Trade-offs als zu prüfende Hypothese | Belegte Inputs, Einheiten und Herkunft; deterministische Berechnung; Sensitivität; Restriktionen separat; Stabilität ≠ Geschäftswert [S22] |
| R14 | P0/P1 | Discovery- und Outcome-Vertrag | Lernen statt Feature-Fabrik | P0: Problem, Alternativen, kritische Annahme und Messplan; P1: laufende Experimente, valide Ergebnisse und Fortsetzen/Anpassen/Stoppen/Stilllegen |
| R15 | P1 | Stakeholderkonflikte aufbereiten | Keine letzte-Nachricht-gewinnt-Logik | Konflikt und zuständige Entscheidungsinstanz sichtbar |
| R16 | P1 | Änderungsfolgen analysieren | Konsistenz über Artefakte | Geänderte Regel findet abhängige Tickets und Kriterien |
| R17 | P0/P2 | Architekturmehrwert prüfen | Unnötige Agentik vermeiden | P0: Mensch/Vorlage, strukturierter Einzelaufruf, fester Workflow und Agent vergleichen; P2: Multi-Agent nur mit zusätzlichem Nutzen |
| R18 | P2 | Begrenzte Routineautonomie | Reviewaufwand senken | Nur erlaubte reversible Aktionen nach Pilotmessung |

## Nicht gleichsetzen

- Fertiges Ticket ≠ richtiger Bedarf.
- Grüne Tests ≠ korrekte fachliche Anforderung.
- Implementiert ≠ veröffentlicht ≠ wirksam.
- PO ≠ alleiniger Entscheider über Engineering-Schätzungen und Sprintplan [S01].
- RICE-Confidence ≠ kalibrierte Erfolgswahrscheinlichkeit [S03].
