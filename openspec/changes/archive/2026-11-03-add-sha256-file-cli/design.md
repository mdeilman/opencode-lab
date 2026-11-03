# Design

## Context

Das Repository enthält bisher keinen Anwendungscode oder vorhandene Tests. Für Motivation und Verhaltensvertrag siehe `proposal.md` und `specs/file-sha256-cli/spec.md`.

## Goals / Non-Goals

**Goals:** Ein direkt mit Python aufrufbares Skript mit größenunabhängig begrenztem Speicherbedarf und ohne externe Pakete.

**Non-Goals:** Installation als Paket, mehrere Dateien pro Aufruf, alternative Hashalgorithmen und Prüfsummenprüfung.

## Decisions

- `sha256_file.py` im Repository-Wurzelverzeichnis und `argparse` für genau ein Positionsargument verwenden. Das ist gegenüber einem Paket ohne vorhandene Projektstruktur einfacher; `argparse` bietet bereits Hilfe und Argumentfehler.
- Die Datei binär öffnen und `hashlib.sha256()` mit festen Blöcken, etwa 64 KiB, aktualisieren. Anders als beim vollständigen Einlesen bleibt der Speicherverbrauch begrenzt; die konkrete Blockgröße ist kein öffentlicher Vertrag.
- `OSError` beim Öffnen und Lesen abfangen, eine verständliche Meldung samt Pfad auf stderr ausgeben und erst nach vollständigem Lesen den Hash ausgeben. So entsteht bei einem Lesefehler keine scheinbar gültige Prüfsumme.
- `unittest`, temporäre Dateien und subprocess-basierte CLI-Tests verwenden; Lesefehler und begrenzte Lesegrößen bei Bedarf durch kontrollierte Testdoubles simulieren. Das vermeidet externe Testabhängigkeiten und von Benutzerrechten abhängige Berechtigungstests.

## Risks / Trade-offs

- Dateiänderungen während des Lesens → Der Hash beschreibt die tatsächlich gelesenen Bytes; eine atomare Momentaufnahme wird nicht garantiert und ist außerhalb des Umfangs.
- Berechtigungsfehler sind unter privilegierten Benutzern nicht zuverlässig reproduzierbar → Fehlerpfade deterministisch simulieren statt ausschließlich Dateirechte zu ändern.
