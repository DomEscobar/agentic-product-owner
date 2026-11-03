# Mockups: Beitrag, Auswahl und Grenzen

**Mockup:** sichtbarer Entwurf eines Zustands. **Interaktiver Prototyp:** reagiert auf Aktionen. **Technischer Spike:** prüft technische Machbarkeit. Die Begriffe nicht als automatische Reifestufen verwenden.

[Studienkritik](../research/formats-evidence.md) · [Formatauswahl](formats.md) · [Quellen](../research/sources.md)

## Was Mockups beitragen können

| Frage | Beitrag | Grenze |
|---|---|---|
| Verstehen wir dieselbe Anforderung? | Text um konkrete sichtbare Zustände ergänzen [S25] | Kein Ersatz für Regeln, Rechte und Ausnahmen |
| Findet die Person den nächsten Schritt? | Interaktion beobachtbar machen | Screenshot allein reicht dafür nicht |
| Welche Informationen fehlen? | Begriffe, Inhalte und Hierarchie konkretisieren | Erfundenes Feld bleibt Designannahme |
| Funktioniert der Produktansatz? | Gezielte Annahme im Nutzungskontext untersuchen | Gefallen oder Bedienbarkeit beweist keine Nachfrage |
| Funktioniert der Agent? | Oberfläche von Auftrag, Vorschlag, Freigabe und Ergebnis zeigen | Simulierte Antworten beweisen keine Agentenfähigkeit |

Kein belastbarer allgemeiner Prozentanteil von Mockups am Produkterfolg. S25 untersucht historisch Verständnis vorhandener Dokumente, nicht heutige Herstellungskosten. Aktuelle KI-Prototyping-Evidenz zeigt zusätzlich mehr Prototypfortschritt und bessere bewertete Storykonsistenz im Labor [S34] sowie qualitative Vorteile interaktiver Entwürfe für Domänenfeedback [S35].

## Detailgrad getrennt wählen

| Dimension | Entscheidung |
|---|---|
| Visuell | Skizze, Wireframe oder ausgearbeitete Oberfläche? |
| Interaktion | Einzelzustand, klickbarer Ablauf oder realistische Bedienung? |
| Inhalt | Platzhalter oder realistische, nicht sensible Fälle? |
| Verhalten | Welche Regeln sind echt, vereinfacht oder simuliert? |
| Abdeckung | Welche Rollen, Zustände und Fehlerpfade sind für die Frage nötig? |

Eine ansprechende Oberfläche darf früh entstehen, wenn sie günstig und für die Frage hilfreich ist. Kein künstlicher Zwang zu hässlichen Wireframes. Aber: visuell fertig ≠ vollständig, realistisch bedienbar ≠ produktionsreif. Höhere Fidelity ist nicht pauschal besser [S26][S27].

## KI-native Herstellung und gemeinsames Lernen

Reguläre Option, kein Pflichtschritt für jedes Ticket:

1. Belegtes Ziel, Domänenbegriffe und konkrete synthetische Fälle bereitstellen. Optional mit Skizze oder bestehendem Screen starten.
2. Editierbaren Screen oder unmittelbar interaktiven Ausschnitt erzeugen; fachlich unterschiedliche Alternativen zulassen.
3. Relevante Zustände und Interaktionen kurz testen, bevor Fachpersonen damit arbeiten.
4. Gemeinsam ausprobieren und bei Bedarf direkt verändern; beobachtetes Problem von Prototypdefekt trennen.
5. Neue fachliche Erkenntnisse als Story-Kandidaten mit Herkunft zurückführen; vom Stakeholder bestätigen oder verwerfen lassen.
6. Anforderungen und Design gezielt abgleichen; Entscheidung und Teststand speichern.

Das Design dieses Ablaufs ist unsere Ableitung aus S34/S35, nicht als Gesamtablauf validiert. Direkter interaktiver Einstieg darf günstiger sein als mehrere Vorstufen. „Klein“ bedeutet geringster Gesamtaufwand bis zur belastbaren Antwort, nicht automatisch wenige Pixel.

### Story–GUI-Verknüpfung

- Requirement-ID/Version ↔ Screen-/Komponenten-ID/Version.
- Herkunft: Nutzerbeobachtung / ursprüngliche Aussage / aus Design abgeleitet / Modellvorschlag.
- Automatisch erkannte sichtbare Abdeckung, fachliche Bestätigung und getestete Implementierung getrennt halten.
- Storyänderung markiert betroffene Screens; Designänderung erzeugt prüfbaren Änderungs-/Story-Vorschlag.
- Links und Statusvorschläge sind korrigierbar; kein blindes Überschreiben. Vollständige automatische Synchronisation ist nicht durch S34 belegt.

## Minimaler Prototyp-Vertrag

Im bestehenden [Experiment-Template](../templates/experiment.md), kein zusätzliches Pflichtdokument:

- Welche Frage beantworten wir, und welche Entscheidung hängt davon ab?
- Wer testet welche konkrete Aufgabe?
- Welche Zustände sind dargestellt?
- Was ist simuliert, was tatsächlich ausgeführt?
- Welche Requirement-/Regel- und Prototypversion wird geprüft?
- Welche Beobachtung würde den Entwurf widerlegen oder verändern?
- Welche Schlussfolgerung ist ausdrücklich NICHT zulässig?

GOV.UK formuliert den Zweck als Lernen vor größerer Bindung, mit nur dem nötigen Detailgrad [S30]. Ein Prototyp kann auch eine E-Mail oder ein Prozess sein; nicht jedes Problem braucht eine Oberfläche.

## Konkretes Beispiel: Freigabeansicht eines PO-Agenten

Illustratives Design, noch keine implementierte UI:

```text
Entscheidung: Soll dieser Ticketentwurf veröffentlicht werden?
Problem:      Quelle und betroffene Nutzergruppe
Vorschlag:    Konkrete Änderung, Zielobjekt und Empfängerkreis
Unsicherheit: Fehlende oder widersprüchliche Grundlage
Konsequenz:   Was ändert sich; welche Benachrichtigung wird ausgelöst?
Aktionen:     Freigeben / Überarbeiten / Zurückstellen
```

Für die Frage „Versteht der Reviewer die Freigabe?“ genügt eventuell ein statischer Zustand plus Gegenfall. Für „Kann er nach einer Unterbrechung sicher weiterarbeiten?“ braucht es relevante Übergänge, etwa abgelaufene Freigabe, geänderte Evidenz und erneute Prüfung. Nicht alle denkbaren Screens vorab bauen.

## Schutz vor Demo-Scheinsicherheit

- Konzeptstatus, simulierte Daten und nicht implementierte Fähigkeiten sichtbar kennzeichnen.
- Im Mockup dargestellte Regel nicht still zur bestätigten Anforderung hochstufen.
- Screens, Text und Akzeptanzfälle referenzieren denselben Stand; Konflikt blockiert eine definitive Übergabe.
- Keine Produktionsschreibrechte, echten Nachrichten oder sensiblen Kundendaten für die Demo.
- Vor echten Teilnehmenden den Prototyp selbst prüfen; tote Links oder falsche Übergänge nicht als Nutzerfehler werten.
- Codeprototypen nicht ungeprüft in Produktion übernehmen [S31].
- Beobachtungen und Entscheidungen samt Prototypversion im Wiki speichern; nicht nur Screenshots sammeln.

## Beitrag lokal messen

Drei getrennte Fragen:

- **Herstellung:** manuell / KI-Erstfassung / KI plus Story–GUI-Abgleich. Gleiche Ausgangsinformation, gleicher Ausgabeauftrag und Rückfragezugang; Generierung, Reparatur, Review und Synchronisation bis zum gleichen Qualitätsziel messen. Nicht begonnene Aufgaben im Nenner behalten.
- **Darstellung:** gleicher fachlicher Inhalt als Text, Screens oder Interaktion.
- **Gemeinsames Lernen:** neue anschließend bestätigte Anforderungen, korrigierte Fehlannahmen und Zeit zur Entscheidung; repräsentative Fachpersonen und Vorwissensunterschiede berücksichtigen.

Produktwirkung bleibt eine separate spätere Messung.

- Gleiche fachliche Information: Text allein / Text plus Screens / Text plus interaktiver Ablauf.
- Interaktivität und visuelle Ausarbeitung nicht gleichzeitig ändern und alles „Mockup-Effekt“ nennen.
- Vergleichbare Aufgaben, repräsentative Rollen, ausgeglichene Reihenfolge.
- Messen: korrektes Verständnis, übersehene Fehler, Aufgabenerfolg, Reviewzeit sowie Herstellungs-/Pflegeaufwand.
- Separat fragen, welche realen Fähigkeiten die Person dem System zuschreibt.
- Zufriedenheit und Zustimmung separat ausweisen; kein Ersatz für Verhaltensmessung [S27].
- Keine universelle Stichprobengröße; Pilotvarianz und Fehlerkosten berücksichtigen. LLM-Rollenspiel ersetzt keine menschliche Untersuchung.
