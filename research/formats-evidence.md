# Formate und Mockups: Evidenzprüfung

Stand: 2026-11-03. Keine Studie untersucht den hier entworfenen PO-Agenten. Empfehlungen in den [Formatregeln](../docs/formats.md) und [Mockup-Regeln](../docs/mockups.md) sind Übertragungen, keine validierten Gesamtprozesse.

## Aktuelle KI-native Arbeit: 2025/2026

**Korrektur:** Die erste Fassung gewichtete klassische Formatstudien zu stark. Sie erklärt Darstellungswirkungen, nicht den aktuellen Nutzen generativer Herstellung, gemeinsamer Iteration oder Story–GUI-Verknüpfung. Die folgenden positiven Befunde ändern den empfohlenen Arbeitsablauf.

| Quelle | Design | Positiver Befund | Grenze |
|---|---|---|---|
| S34 CHI 2025 | Randomisierter Laborvergleich, 40 Studierende, 45 Minuten Herstellungszeit; Figma mit/ohne Assistenzbündel; separate Artefaktbewertungen | Im Mittel 1,75 gegenüber 1,35 Prototypscreens; höhere bewertete Storykonsistenz | Statische Einzel-Screens, kein fertiges Produkt. Funktionen gebündelt; einzelne Beiträge nicht isoliert. Nicht begonnene Apps aus Erfüllungsbewertung ausgeschlossen; keine universelle Nettozeitersparnis |
| S35 Li et al., 2025 | UCD-Fallstudie zu Verkehrsanalytik, v0/Bolt.new; Expertenfeedback und gemeinsame Sessions | Konkrete neue Interaktionsalternative; qualitativ mehr und gehaltvolleres Feedback durch ausprobierbare Entwürfe | Kein kontrollierter Vergleich; Expertenanzahl nicht berichtet; Vorwissen wächst über Projektverlauf. Kumulative Generierungsfehler und falsche Interaktionen dokumentiert |
| S36 Romero et al., 2026 | 92 Studierende bewerten zehn statische Entwürfe, Herkunft verborgen; fünf KI-Tools und ein menschlicher Designer | Ein KI-Entwurf mit höchstem Gesamtmittel, vergleichbar bewertet mit führenden menschlichen Entwürfen | Nur Wahrnehmungsratings; keine Interaktion. Alle Gesamtmittel nach eigener Skala neutral. Keine kausale KI-Konventionalität und kein belastbares Toolranking |
| S37 Mircea et al., 2026 | 26 IDE-Nutzende bewerten 130 eigene Anforderungen und GPT-4o-Reformulierungen; Hauptanalyse pro Person | Signifikant bessere wahrgenommene Absichtstreue, Lesbarkeit, Begründung und Eindeutigkeit | Unverblindete Selbstbewertung; kein objektiver Verständnistest oder Vergleich mit menschlicher Redaktion. Ergänzte Inhalte machen es nicht informationsgleich |

### Geprüft, aber nur schwach gewichtet

- **S38 Sketch → Requirements/HTML:** eine Skizze, ein simuliertes Szenario, drei Modelle, drei Experten. Generierung demonstriert; behauptete iterative Schleife nicht evaluiert. Interne Mittelwert-/Rankingwidersprüche; keine Modellrangliste und keine behauptete Elicitation-Zeitersparnis übernehmen.
- **S39 Prototypingtools:** 14 Studierende, feste Toolreihenfolge, kein manueller Kontrollarm. SUS misst Werkzeugusability, nicht Stakeholderverständnis. Nutzbare Generierung, aber manuelle Reparatur bleibt relevant; keine belegte toolweise Nettozeit.
- Publikationsjahr ≠ Modellstand: S34 nutzt GPT-4o mit Zugriff August 2024; S37 nennt GPT-4o ohne datierten Snapshot. Bei S39 betrifft „ChatGPT 5.2“ Manuskriptübersetzung, nicht das getestete Prototypingmodell.

Volltexte der sechs aktuellen Arbeiten gelesen; Studien nicht reproduziert. SEMISH-Veröffentlichung von S36 bestätigt; S37-Ergebnisse aus ausdrücklich genannter arXiv-Version.

## Historische Grundlagen: Darstellung und Verständnis

| Quelle | Design | Befund | Grenze / Zugriff |
|---|---|---|---|
| S25 Ricca et al., 2014 | Vier kontrollierte gegenbalancierte Experimente, insgesamt 139 Studierende; zwei Desktop-Anwendungen; strukturierter Text mit/ohne verlinkte Screen-Mockups | Publizierter Abstract berichtet bessere Comprehension und Effizienz; kein signifikanter Effekt auf Bearbeitungszeit | Methoden im Autorentext gelesen; Ergebnistabellen abgeschnitten, Richtung am Verlagsabstract geprüft. Keine Effektgrößen-Reanalyse. Verständnis vorhandener Dokumente, nicht Discovery oder PO-Produktivität |
| S26 Walker et al., 2002 | 28 Personen; zwei Banking-Websites; visuelle Fidelity × Papier/Computer; beide Medien erlauben Interaktion | Keine signifikanten Unterschiede bei Zahl/Schwere gefundener Probleme; Unterschiede bei Problemtypen | Kleine Stichprobe; Nichtsignifikanz beweist keine Gleichwertigkeit. Kein Vergleich statisch gegen interaktiv; Volltext gelesen |
| S27 Sauer/Sonderegger, 2009 | 60 Studierende; drei Fidelity-Ausprägungen × zwei Telefonmodelle; zwei Aufgaben | Objektive Leistung und subjektive Usability nicht verbunden; simuliertes Interaktionsmodell kann Zeitmessung verzerren | Ältere Handys, enges Setting; kein direkter Nachweis von blindem Vertrauen in Agenten; Volltext gelesen |
| S28 Example Mapping, 2021 | Zwei longitudinale Fallstudien mit acht bzw. fünf Sessions, Beobachtungen/Fragebögen | Positive Hinweise auf wahrgenommenes gemeinsames Verständnis; sehr kleine Stories problematisch | Keine randomisierte Vergleichsstudie; Gespräch/Moderation und Kartendarstellung nicht isoliert; Volltext gelesen |
| S29–S33 Methodenquellen | Gherkin, Prototyping, Stories und Story Mapping | Beabsichtigter Einsatz, Begriffe, Ablauf und Grenzen | Keine kausalen Nachweise für ein universelles Formatpaket |

## Präzise Schlussfolgerungen

- KI-generierte Erstentwürfe sind ein regulär zu prüfender Arbeitsweg, nicht bloß hypothetische Zukunftsmusik [S34][S35].
- Anforderungen können Input UND überprüfbarer Output von Designarbeit sein: GUI-abgeleiteter Story-Kandidat ist noch kein bestätigter Nutzerbedarf [S34].
- Herstellungsfortschritt, Story-Abdeckung, wahrgenommenes Verständnis, Lerngewinn und Produktwirkung getrennt berichten [S34][S35][S37].
- Vollautomatisches Round-Tripping ist nicht gelöst: S34 kann neue Komponenten erzeugen, bestehende aber nicht automatisch anpassen.

- Text plus gezielte Screens ist bei UI-Anforderungen plausibel und durch begrenzte direkte Verständnis-Evidenz gestützt [S25].
- Mehr visuelle Ausarbeitung ist keine allgemeine Garantie besserer Problemsuche [S26].
- Gut aussehen, gut bewertet werden und eine Aufgabe tatsächlich bewältigen sind getrennte Größen [S27].
- Regelbeispiele sind sinnvoll zu testen; eine vollständige Example-Mapping-Session nicht für triviale Änderungen erzwingen [S28].
- Interaktivität, Inhalt, visuelle Fidelity und Zustandsabdeckung separat auswählen.
- Kein belastbarer universeller Prozentwert zum Beitrag von Mockups an Produktnutzen oder PO-Arbeit.

## Originalbelege

- S34, §5.2.1: “On average, 1.35 apps were created in the control group and 1.75 apps in the treatment group.” Gemeint: Prototypscreens.
- S34, §8: “the implementation of our approach in its current form is limited to creating new components and cannot adapt existing components.”
- S37, §5.2: “we recognize our results capture only perceived improvements in requirement quality.”

- S25, Abstract: “No significant effect was observed on the effort to complete tasks.”
- S26, Discussion: “The types of usability issues found were significantly different between low- and high-fidelity conditions.”
- S27, Discussion: “It also emerged that objective performance parameters collected during the usability test and subjective usability ratings were not associated.”
- S30: “A prototype answers a question.”
- S32: “The card does not contain all the information that makes up the requirement.”

## Bewusst nicht übernommen

- Feste Prozentanteile, universelle Testpersonenzahlen oder Pflicht-Mockup je Ticket.
- „Low Fidelity ist immer billiger“: historische Herstellungsannahmen gelten nicht automatisch für heutige KI-Werkzeuge.
- „High Fidelity erzeugt zwingend Fixierung“: gelesene Parallel-Prototyping-Studien manipulieren Arbeitsablauf, nicht Fidelity; keine direkte Übertragung.
- Story-Vorlagenranking und allgemeine Text-versus-Diagramm-Rangfolge: zugängliche Abstracts reichen dafür nicht.
- Zusätzlichen Formal-Experiment-Titel als unabhängige Bestätigung zählen: vollständiger Primärtext nicht verfügbar; keine KI-Zusammenfassungen als Evidenz.
- Zustimmung zum Mockup als Beleg für Nachfrage, Zahlungsbereitschaft, technische Machbarkeit oder Agentensicherheit.

[Quellenregister](sources.md)
