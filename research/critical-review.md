# Kritische Gegenprüfung — Runde 2

Stand: 2026-11-03. Primärtexte geprüft; keine Benchmarks reproduziert. Designkorrekturen, keine implementierten Schutzfunktionen. Quellen: [Register](sources.md).

## Entscheidungen nach Prüfung

| Annahme / Lücke | Urteil | Konsequenz |
|---|---|---|
| Agentik ist die passende Grundarchitektur | Nicht belegt | Fester LLM-Workflow als eigenständige Baseline; Architekturmehrwert prüfen |
| Repo-Wiki verbessert Leistung | Offen, keine Zusicherung | Kleine Karten gegen direkte Quellensuche testen; Pflegekosten einschließen |
| Mehr komprimiertes Wissen ist besser | Zu pauschal | Gegenbelege, Scope und Originalfundstellen beim Verdichten erhalten |
| Unsicherheit bedeutet Rückfrage | Falsch als Universalregel | Fehlenden Kontext, fehlenden Fakt, Rechenproblem, Zielkonflikt und Kompetenzgrenze unterscheiden |
| Menschliche Freigabe sichert Qualität | Autorisierung ja, Qualität nicht automatisch | Konsequenzorientierte Reviewansicht und Fehlerdetektion separat testen |
| Jede Aktion braucht einen eigenen Klick | Widerspricht Routineautonomie | Einzel-Freigabe und vorautorisierte Aktionsklasse sauber trennen |
| Sicherer Ticketfluss reicht für PO-Pilot | Zu eng | Problem, Alternativen, kritische Annahme und Nutzenmessplan als Mindestvertrag |
| Aktueller Inhalt genügt | Unvollständig | Wahrheit, Geltungszeit und erlaubte Nutzung getrennt prüfen |
| Immer blockieren besteht Sicherheitstests | Fehlanreiz | Erlaubte Gegenfälle und unnötige Eskalation bewerten |

## Aufgenommene Evidenz

| Quelle | Was tatsächlich untersucht wurde | Belastbarer Befund | Übertragungsgrenze |
|---|---|---|---|
| S17: AGENTS.md v3 | 300 SWE-bench-Lite- und 138 CTXbench-Aufgaben; mehrere Agent-/Modellkonfigurationen | Keine signifikanten Resolution-Gewinne durch Kontextdateien gegenüber keiner Datei; generierte Dateien verursachen zusätzliche Kosten | Coding, nicht PO. Kein Beweis, dass notwendige Konventionen oder Sicherheitsregeln nutzlos sind. Ältere Headline-Zahlen nicht mit v3 mischen |
| S18: LongMemEval v2 | 500 Fragen zu langen Gesprächshistorien, Indexierung/Retrieval/Reading | Verdichtung zu Einzelfakten kann Gesamtleistung wegen Informationsverlust verschlechtern | Gesprächs-QA, keine Produktpriorisierung; Detailgewinn bei einzelnen Teilaufgaben möglich |
| S19: Human Oversight v2 | 48 Personen, 192 Sessions, vier Strategien, replizierte Websites und fiktives Profil | Strategien beeinflussen Auftreten und unkorrigierte Fehler; kein signifikanter Strategieunterschied bei bedingter Intervention | Kein vollständig autonomer Vergleich; kurzer Laborablauf; Intervention nur unter bereits aufgetretenen Problemen gemessen |
| S20: UA-Bench | Toolfreie QA/Mathematik; Unterscheidung von Daten- und Modellunsicherheit | Modelle können eigene Wissensgrenzen fälschlich als Unklarheit der Frage darstellen | Gemischte Unsicherheit ausgeschlossen; keine direkte Erfolgsquote für PO-Arbeit |
| S21: OntoAgent v1 | 101 simulierte Website-Interviews; menschliche Ergänzung mit sechs Studierenden | Strukturierte Ontologie und Frageauswahl zeigen positive Benchmarkresultate | Alle Hauptbaselines Free-form; keine gleichwertige Checklisten-/Workflow-Kontrolle. Interne Tabellen-/Textwidersprüche; kein isolierter Autonomieeffekt |
| S22: industrielle Priorisierung | Vier Firmen, neun Befragte, vier Interviews; Autorensystem | Relevante Praxiserfahrungen und gemischte Zustimmung zur Priorisierung | Keine kontrollierte Architekturstudie, keine detaillierten Interaktionslogs; stabile Rankings nicht gleich Geschäftswert |
| S23: GitHub | Dokumentation zur Entfernung sensibler Daten | Fremde Clones lassen sich nicht zentral bereinigen | Kein Ersatz für Datenklassifikation vor dem Commit |
| S24: Experimentierpraxis | Industrielle Methoden und Beispiele | Datenvalidität, Guardrails, Segmente und zeitlicher Verlauf vor Rolloutentscheidung prüfen | Keine Pflicht zu A/B-Tests für jede Produktfrage, kein PO-Agentenvergleich |

## Kurze Originalbelege

- S17, §4: “We observe that including context files does not significantly affect performance.”
- S18, §5: “While further compression into individual user facts harms overall performance due to information loss, it improves the multi-session reasoning accuracy.”
- S19, Limitations: “Finally, we compared oversight strategies without a fully autonomous baseline.”
- S21, Baselines: “These five baselines all use free-form elicitation approach.”
- S23: “You cannot remove sensitive data from other users' clones of your repository”.

## Bewusst nicht ins Referenzdesign übernommen

| Kandidat | Ausschlussgrund |
|---|---|
| Vollautomatische Wiki-/Graph-Plattform als Startarchitektur | PO-Mehrwert und Wartungskosten nicht nachgewiesen |
| Universelle optimale Eskalationsquote | Fatigue-Modellierung ist keine gemessene Langzeitwirkung auf Reviewer |
| Bestimmte kognitive Reviewintervention als bewiesene Lösung | Geprüfte Ergebnisse uneinheitlich; teils interne Widersprüche, kein gesicherter Vorteil gegenüber Kontrolle |
| PM-Adoption/Toolnutzung als Produktivitätsnachweis | Nutzungshäufigkeit misst weder Entscheidungsqualität noch Kundennutzen |
| Große Effektzahlen aus sehr neuen Memory-Preprints | Enge/offline oder nicht held-out bestätigte Designs; keine Grundlage für universelle Architekturentscheidung |
| Mehragenten-Rollenkonsens als Stakeholderkonsens | Simulierte Perspektiven ersetzen keine realen Befugnisse und Interessen |
| Pflicht-RCT, feste Interviewzahl oder Informationsquote | Kontextabhängige Methoden; keine belastbare universelle Schwelle |
| Direkte Übernahme von Coding-Produktivität auf PO-Arbeit | Andere Aufgabe, andere Feedbacksignale und Fehlerkosten |

Ausschluss bedeutet: keine tragende Designbegründung in dieser Runde. Nicht: Quelle widerlegt oder Ansatz grundsätzlich unbrauchbar.

## Offene Entscheidungen

- Liefert adaptives Fragen mehr relevante Information pro Stakeholderminute als eine gute Checkliste?
- Wann ist Wiki-Pflege günstiger als aktuelle Quellensuche?
- Welche Reviewdarstellung verbessert Fehlererkennung ohne untragbare Teamkosten?
- Welche Aktionsklasse ist im konkreten Produkt ohne erneuten Klick vertretbar?

Antworten benötigen einen eigenen Pilot. Die Recherche liefert dafür Prüfbedingungen, keine erfundenen Resultate.
