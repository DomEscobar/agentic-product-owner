# Designentscheidungen

Status aller Einträge: vorgeschlagenes Referenzdesign, keine produktive Freigabe.

| ID | Entscheidung | Grund | Alternative / Neubewertung |
|---|---|---|---|
| D01 | Menschliche Accountability erhalten | Delegation ersetzt Verantwortlichkeit nicht [S01] | Autonomie nur innerhalb expliziten Mandats |
| D02 | Ein Orchestrator zum Start | Geringere Komplexität; Mehragentenvorteil nicht voraussetzen [S09] | Multi-Agent bei budgetgleichem Nachweis |
| D03 | Wiki im Repo für nicht sensibles Produktwissen | Versionierung, Review, Nähe zur Umsetzung | Separates System bei abweichenden Zugriffsrechten |
| D04 | Workflow-State außerhalb des Wikis | Atomare Operationen, Retry- und Freigabestatus | Persistenztechnologie nach Betriebsanforderungen |
| D05 | Vorschlag und Ausführung trennen | Konkrete Autorisierung und Nachvollziehbarkeit | Routineautonomie nur nach Messung |
| D06 | Originalquellen referenzieren | Keine Selbstbestätigung durch Zusammenfassungen | Sensible Originale geschützt extern halten |
| D07 | Outcome-Loop vorsehen | Lieferung ist kein Wertnachweis [S02] | Messdesign an Produkt anpassen |
| D08 | Kein zweites vollständiges Backlog | Verhindert widersprüchliche Wahrheit | Führendes System je Objekttyp festlegen |

Quellen: [Register](../research/sources.md).
