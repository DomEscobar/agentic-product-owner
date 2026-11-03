# Verständliche Formate

**Auswahlregel:** Welche Frage ist offen? Den geringsten Gesamtaufwand bis zu einer belastbaren Antwort wählen — nicht automatisch das visuell einfachste Format. Ein direkt generierter interaktiver Ausschnitt kann der kürzeste Weg sein [S34][S35]. Kein Pflichtpaket aus Brief, Story Map, Mockup und Gherkin.

Designempfehlung aus [S25–S33](../research/sources.md); [Evidenz und Grenzen](../research/formats-evidence.md).

## Ein leichter Einstieg

1. **Situation:** Wer versucht gerade was?
2. **Problem:** Was scheitert — und woher wissen wir das?
3. **Entscheidung:** Was müssen wir jetzt klären oder auswählen?
4. **Konkreter Fall:** Was passiert heute, was soll künftig passieren?
5. **Offen:** Welche Annahme oder Frage könnte die Entscheidung verändern?

Keine verpflichtende Feldzahl: bereits bekannter Kontext wird verlinkt, nicht erneut abgeschrieben. Das bestehende [Requirement-Template](../templates/requirement.md) zeigt Details schrittweise.

## Format nach Unsicherheit

| Offene Frage | Kleinste geeignete Darstellung | Nicht damit beweisen |
|---|---|---|
| Welches Problem ist relevant? | Kurzer Problem-Brief mit realem Fall und Quelle | Nachfrage aus bloßer Plausibilität |
| Was bedeutet die Regel? | Regel → konkreter Normal-/Grenzfall → Ergebnis → offene Frage | Richtige Produktstrategie |
| Was gehört in einen nutzbaren ersten Schnitt? | Story Map: Nutzerziel, Aktivitäten, Varianten, Ende-zu-Ende-Schnitt [S33] | Präzise Zustandsübergänge |
| Welche Fähigkeit besprechen wir? | Story-Titel plus Nutzer/Zweck und Referenzen [S32] | Vollständige Spezifikation durch Satzschablone |
| Was geschieht bei einem Ereignis? | Given–When–Then für ausgewählte stabile Fälle [S29] | Ausführbarer Test ohne Step Definitions |
| Wo verzweigt oder übergibt der Ablauf? | Kleiner Flow mit Rollen, Start/Ende und relevantem Fehlerpfad | Verständlichkeit allein durch grafische Notation |
| Was sieht die Person hier? | Statischer Screen plus Regelreferenz | Navigations- oder Fehlerbehandlungsqualität |
| Kann sie die Aufgabe bedienen? | Klickbarer relevanter Ablauf, bei Bedarf direkt KI-generiert | Backend-Funktion, Sicherheit oder Produktnutzen |
| Können wir Absicht und fehlende Details besser ausdrücken? | Originalaussage plus LLM-Reformulierung; Ergänzungen markieren und rückvalidieren [S37] | Technische Richtigkeit allein durch Zustimmung |
| Welche Option wählen wir und warum? | Vorhandene Entscheidungsnotiz: Wahl, Grund, akzeptierter Nachteil | Konsens allein durch Dokumentation |

## Beispiele statt abstrakter Qualitätswörter

Nicht: „Freigaben müssen sicher und verständlich sein.“

| Regel | Konkreter Fall | Erwartetes Ergebnis | Offene Frage |
|---|---|---|---|
| Eine interne Freigabe gilt nicht für externe Kommunikation | Ein genehmigter interner Entwurf soll an einen Kunden gehen | Nicht senden; Empfänger und Inhalt neu autorisieren | Wer darf extern freigeben? |
| Ein abgelaufenes Mandat autorisiert keinen Write | Mandat läuft während einer Pause aus | Zustand neu prüfen; nicht ausführen | Wer kann das Mandat erneuern? |

Das sind illustrative Designfälle, keine beobachteten Nutzeranforderungen. Example Mapping unterstützt die Klärung; die begrenzte Feldstudie isoliert den Effekt der Karten nicht vom Gespräch [S28]. Für triviale Änderungen keinen Workshop erzwingen.

## Einfach für Menschen, präzise für den Agenten

- Oben: Entscheidung, Fall, offene Frage, nächster Schritt.
- Bei Bedarf: Regeln, Varianten, Screens und Testfälle.
- Dahinter: IDs, Provenienz, Statusachsen, Berechtigungen und Versionen.
- Eine gepflegte Aussage, mehrere Ansichten; keine unabhängigen Kopien in Story, Wiki, Mockup und Tests.
- Strukturierte Maschinenmetadaten nicht als YAML-Formularwand im Erstgespräch zeigen.
- Versteckte Darstellung darf weder Autorisierung noch Nachvollziehbarkeit entfernen.
- Repository-Zugang nicht voraussetzen: berechtigte Beteiligte brauchen eine lesbare Ansicht ohne Git-Kenntnisse.

## Gemeinsames Verständnis prüfen

Nicht nur „verstanden?“ oder „gefällt dir das?“ fragen.

- Fachseite und Umsetzung erklären denselben Fall unabhängig in eigenen Worten.
- Jede Person sagt das erwartete Ergebnis für einen neuen Grenzfall voraus.
- Unterschiedliche Interpretationen und fehlende Regeln sichtbar sammeln.
- Bei Bedienfragen eine konkrete Aufgabe ohne erklärendes Coaching durchführen lassen.
- Verständnis, Zustimmung zur Entscheidung und Einigkeit über Interessen getrennt erfassen.

Lokaler Evaluationsvorschlag, kein bereits validiertes Messinstrument: Fehlinterpretationen, kritische Konflikte, Klärungszeit, Reviewzeit und spätere Nacharbeit messen. Kurzer Text ist nicht automatisch einfacher; entscheidend ist die benötigte Interpretation.
