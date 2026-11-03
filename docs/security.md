# Autonomie und Sicherheit

Designempfehlung; Bedrohungsgrundlage [S11](../research/sources.md).

| Stufe | Erlaubt | Voraussetzung |
|---|---|---|
| A | Berechtigte Recherche und Analyse | Quellen-Scope und Datenregeln |
| B | Entwürfe ohne externe Veröffentlichung | Quellenbindung und Qualitätsprüfung |
| C | Konkrete freigegebene Änderungen | Diff, Zielversion, Identität, Policy, Read-back |
| D | Begrenzte Routineaktionen | Vorautorisierte Aktionsklasse; gemessener Nutzen/Risiko; Nebenwirkungen eingeschlossen |

## Standardmäßig gesperrt

- Budgetbindung, externe Lieferzusagen, Sprint-Abbruch.
- Löschen, Rechteänderungen, Export sensibler Rohdaten.
- Agenteneigene Erweiterung von Policies oder Toolrechten.
- Änderung freigegebener Prioritäten ohne entsprechende Vollmacht.

## Kontrollen

- Least Privilege; Nutzerrechte sind Obergrenze, kein ausreichendes Agentenmandat.
- Projekt-/Repo-/Space-Allowlist; Lese- und Schreibidentitäten trennen.
- Fremde Texte ausschließlich als Daten behandeln.
- Ausgehende Ziele und Toolargumente serverseitig prüfen.
- Weg A: Einzel-Freigabe an Operation, Diff, Zielversion, Evidenzmanifest, Policy, Identität und Gültigkeitsdauer binden.
- Weg B: Aktionsklassenmandat definiert Scope, erlaubte Felder, Vorbedingungen, Empfänger, Nebenwirkungen, Budget und Ablauf/Widerruf. Kein zusätzlicher Klick für jede passende Routineaktion; konkreter Write bleibt technisch autorisierungspflichtig.
- Datenbank-Rollback macht Benachrichtigungen, Kundenmails oder gelesene Kommentare nicht rückgängig.
- Planfreigabe ist keine pauschale Laufzeitfreigabe. Neue Empfänger, Datenarten oder Verpflichtungen erfordern erneute Autorisierung [S19].
- Menschliche Autorisierung ≠ sorgfältige fachliche Prüfung. Review zeigt Konsequenz und entscheidende Unsicherheit, nicht nur einen Diff.
- Nach Pause Rechte erneut prüfen.
- Secrets nicht in Modellkontext, Logs oder Wiki.
- Logs minimieren, redigieren und mit Löschfristen versehen.
- Mandanten- und Projektgrenzen auch beim Retrieval prüfen.
- Rate Limits, Kostenlimits, Kill Switch, begrenzte Retries.

## Restunsicherheit

Guardrails und strukturierte Ausgaben garantieren keine vollständige Injection-Abwehr. Datenschutz-, Hosting- und Branchenanforderungen müssen projektspezifisch geprüft werden. Kein Rechtsgutachten.
