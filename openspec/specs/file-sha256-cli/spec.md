# file-sha256-cli Specification

## Purpose

Ermöglicht die zuverlässige Berechnung einer SHA-256-Prüfsumme für eine lokale Datei über die Kommandozeile.

## Requirements

### Requirement: Dateihash ausgeben
Das Werkzeug SHALL genau einen Dateipfad als Argument annehmen und den SHA-256-Hash des vollständigen binären Dateiinhalts als 64 kleingeschriebene Hexadezimalzeichen mit Zeilenumbruch auf stdout ausgeben. Bei Erfolg SHALL der Exit-Status 0 sein.

#### Scenario: Bekannter Dateiinhalt
- **WHEN** das Werkzeug für eine Datei mit dem Inhalt `abc` aufgerufen wird
- **THEN** gibt es `ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad` und einen Zeilenumbruch auf stdout aus und beendet sich mit Status 0

#### Scenario: Leere Datei
- **WHEN** das Werkzeug für eine leere Datei aufgerufen wird
- **THEN** gibt es den SHA-256-Hash der leeren Bytefolge aus und beendet sich mit Status 0

### Requirement: Begrenzter Speicherverbrauch
Das Werkzeug SHALL Dateien blockweise lesen, sodass der für Dateidaten benötigte Speicher nicht mit der Dateigröße wächst.

#### Scenario: Datei größer als ein Leseblock
- **WHEN** eine lesbare Datei größer als ein Leseblock verarbeitet wird
- **THEN** wird ihr vollständiger Inhalt über mehrere begrenzte Lesevorgänge gehasht und der korrekte Hash ausgegeben

### Requirement: Dateifehler melden
Bei Fehlern beim Öffnen oder Lesen SHALL das Werkzeug eine verständliche Fehlermeldung mit dem betroffenen Pfad auf stderr ausgeben, keinen Hash ausgeben und sich mit einem Exit-Status ungleich 0 beenden.

#### Scenario: Datei fehlt
- **WHEN** der angegebene Dateipfad nicht existiert
- **THEN** meldet das Werkzeug den Fehler auf stderr, gibt keinen Hash aus und beendet sich mit einem Status ungleich 0

#### Scenario: Datei nicht lesbar
- **WHEN** die angegebene Datei nicht geöffnet oder vollständig gelesen werden kann
- **THEN** meldet das Werkzeug den Fehler auf stderr, gibt keinen Hash aus und beendet sich mit einem Status ungleich 0

### Requirement: Ungültige Argumente zurückweisen
Das Werkzeug SHALL bei fehlendem oder zusätzlichem Dateipfad eine Nutzungsmeldung auf stderr ausgeben und sich mit einem Exit-Status ungleich 0 beenden.

#### Scenario: Kein Dateipfad
- **WHEN** das Werkzeug ohne Dateipfad aufgerufen wird
- **THEN** zeigt es eine Nutzungsmeldung auf stderr und beendet sich mit einem Status ungleich 0

#### Scenario: Mehrere Dateipfade
- **WHEN** das Werkzeug mit mehr als einem Dateipfad aufgerufen wird
- **THEN** zeigt es eine Nutzungsmeldung auf stderr und beendet sich mit einem Status ungleich 0
