# Agentic Product Owner

Recherchebasierte Anforderungen und Referenzdesign für einen agentischen PO.

**Status:** Wissensbasis / Spezifikation. Kein implementierter PO-Agent. Keine nachgewiesenen Produktivitätsgewinne. Stand: 2026-11-03.

## Einstieg

| Datei | Inhalt |
|---|---|
| [Anforderungen](docs/requirements.md) | Prioritäten, Nutzen, Abnahmekriterien |
| [Edge Cases](docs/edge-cases.md) | Fehlerfall → erwartetes Verhalten → Prüfung |
| [Architektur](docs/architecture.md) | Workflow, Zustände, Integrationen |
| [Repo-Memory](docs/repo-memory.md) | Wiki, Provenienz, Aktualisierung, Grenzen |
| [Autonomie und Sicherheit](docs/security.md) | Rechte, Freigaben, Bedrohungen |
| [Evaluation](docs/evaluation.md) | Baselines, Metriken, Release-Gates |
| [Forschung](research/findings.md) | Studienergebnisse und Einschränkungen |
| [Quellen](research/sources.md) | Primärquellen und Evidenztypen |
| [Entscheidungen](docs/decisions.md) | Begründungen und Alternativen |
| [Pilot](docs/pilot.md) | Einstieg, Nicht-Ziele, offene Entscheidungen |
| [Templates](templates/) | Evidence, Decision, Requirement, Experiment |
| [Szenarien](evals/scenarios.json) | Maschinenlesbare Akzeptanzszenarien |

## Kernregeln

- Beleg ≠ Interpretation ≠ Hypothese ≠ Entscheidung ≠ Ergebnis.
- Keine erfundenen Kundenbedürfnisse, Schätzungen, Freigaben oder Zitate.
- Produktnutzen statt Ticketmenge optimieren.
- Vorschläge und freigegebene Entscheidungen getrennt halten.
- Policies außerhalb des Modells durchsetzen.
- Externe Änderungen zurücklesen; Timeout ist kein Beleg für Fehlschlag.
- Wiki ist Produktgedächtnis, nicht Autorisierungsinstanz oder Workflow-Datenbank.
- Eigene Zusammenfassungen sind keine unabhängigen Quellen.

## Lokale Prüfung

```sh
python3 scripts/check.py
```

Prüft Dokumentlinks, Szenario-IDs und Referenzen. **Prüft keinen PO-Agenten.**

## Evidenzkennzeichnung

- Normativ: Scrum-Verantwortlichkeiten.
- Empirisch: begrenzte Studien mit beschriebenem Versuchsdesign.
- Dokumentiert: Herstellerfunktionen; nicht unabhängig benchmarked.
- Empfehlung: abgeleitetes Design, kein gemessener Wirksamkeitsnachweis.

Keine privaten Kundendaten, kopierten Paper-Volltexte oder Zugangsdaten enthalten.
