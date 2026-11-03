# Proposal

## Why

Ein kleines Kommandozeilenwerkzeug soll SHA-256-Prüfsummen lokaler Dateien ohne zusätzliche Abhängigkeiten berechnen, auch wenn die Dateien groß sind.

## What Changes

- Ein Python-Kommandozeilenprogramm nimmt genau einen Dateipfad entgegen und gibt dessen SHA-256-Hash aus.
- Die Datei wird mit begrenztem Speicherverbrauch blockweise gelesen; fehlende oder nicht lesbare Dateien führen zu verständlichen Fehlern.
- Tests und kurze Nutzungsdokumentation beschreiben das Verhalten. Es wird ausschließlich die Python-Standardbibliothek verwendet.

## Capabilities

### New Capabilities
- `file-sha256-cli`: Berechnung und Ausgabe des SHA-256-Hashes einer angegebenen Datei einschließlich Fehlerverhalten.

### Modified Capabilities

Keine.

## Impact

Das bislang ohne Anwendungscode vorliegende Repository erhält ein eigenständiges Python-Skript, Standardbibliotheks-Tests und eine Nutzungsanleitung. Es entstehen keine externen Laufzeitabhängigkeiten.
