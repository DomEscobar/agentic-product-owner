# Forschungsbefunde

Recherche: 2026-11-03. Gezielte Recherche, kein systematisches Review mit Vollständigkeitsanspruch. Studienversionen und Modellstände begrenzen Übertragbarkeit.

| Quelle | Design | Ergebnis | Grenze | Designfolge |
|---|---|---|---|---|
| S05: Bashir et al., ICSME 2025 | Drei industrielle Datensätze; kleine offene Modelle; Few-shot; acht Industrieexperten | Llama-3/Westermo: gewichteter F1 61,3 % ohne Beispiele, 68,6 % mit zehn zufälligen Beispielen; Natürlichkeit 4,08/5, Nützlichkeit 3,38/5 | Kein Nachweis weniger Nacharbeit; gewichteter F1 nicht gleich kritischer Recall | Warnhinweise und Rückfragen, keine automatische Freigabe |
| S07: Quattrocchi et al., arXiv v1 2025 | Simulierte Analysten-/Kundeninterviews; Kunde bekommt Referenzanforderungen vorab | Claude 3 Sonnet: 96,23 % Referenzabdeckung bei Schwelle 0,8; Studierende 52,83 % | Wiedergewinnung vorgegebener Bedürfnisse; kein isolierter Mehragentenvorteil | Nicht als autonome Discovery interpretieren |
| S06: Paiva et al., 2026 | 150 OSS-Feature-Titel; zwei Modelle; drei Prompts; 900 Anforderungen; menschliche Teilbewertung | Exakte Mensch–Judge-Übereinstimmung 34–42 %; Expertenpersona verschlechtert teils Singularität | Intrinsische Textqualität, nicht fachliche Richtigkeit oder Nutzen; auch menschliche Einigkeit begrenzt | Rubriken kalibrieren; Persona kein Qualitätsnachweis |
| S15: Prioritizing Software Requirements, arXiv v1 2024 | GPT-3.5-Demonstrator für Stories und Priorisierung | Ranking-Erzeugung demonstriert | Keine belastbare Ranking-Validierung oder kontrollierter menschlicher Vergleich im gelesenen Evaluationsabschnitt | Ranking ≠ richtige Produktentscheidung |

## Aktualisierung durch Gegenprüfung

[Zweite Runde](critical-review.md): Agentische Steuerung bleibt eine zu testende Architekturhypothese. S21 liefert positive Evidenz für strukturierte Elicitation, isoliert aber keinen Agentikvorteil gegenüber einem gleichwertigen festen Workflow. S22 ergänzt reale industrielle Priorisierungsbewertung, überwiegend subjektiv und ohne kausalen Nutzenvergleich. Die folgenden Aussagen über die vier Erststudien bleiben auf diese vier begrenzt.

## Belastbare Schlussfolgerungen

- Aufgabenbezogene Assistenz ist plausibel und teilweise empirisch untersucht.
- Keine der vier Arbeiten weist höheren realen Kundennutzen durch einen autonomen PO nach.
- Fehlender Nachweis ist kein Beweis prinzipieller Unmöglichkeit.
- Herstellerdokumentation belegt Funktionen, keine unabhängige Produktwirkung.
- Rollen-/Methodenquellen definieren Verantwortung und Vorgehen, keine gemessene Agentenleistung.

## Methodische Fallstricke

- LLM-Judge-Scores nicht mit menschlicher oder fachlicher Wahrheit gleichsetzen.
- Simulierter Kunde mit Ground Truth ist kein unbekannter realer Kunde.
- Cross-System-Ergebnisse isolieren keinen Architektur- oder Mehragenteneffekt.
- Ältere kleine Modelle erlauben keine pauschale Prognose für heutige Modelle.
- Studien mit widersprüchlichen Rangfolgen nicht für Bestmodell-Empfehlungen verwenden.
- Tatsächliche Produktwirkung separat im Team und am Produkt messen.

[Quellenregister](sources.md)
