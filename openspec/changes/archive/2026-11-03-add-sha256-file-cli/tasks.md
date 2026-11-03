# Tasks

## 1. Hashberechnung und Kommandozeile

- [x] 1.1 `sha256_file.py` mit binärem blockweisem Lesen und `hashlib.sha256` erstellen; mit `unittest` bekannte und leere Inhalte sowie eine Datei über mehrere Blöcke und begrenzte Lesegrößen prüfen.
- [x] 1.2 CLI mit genau einem Dateipfad, Hash-Ausgabe auf stdout und Erfolgsstatus 0 ergänzen; mittels Subprozess-Tests Ausgabeformat und Status sowie fehlende und zusätzliche Argumente prüfen.
- [x] 1.3 Fehler beim Öffnen und Lesen abfangen; fehlende Dateien und simulierte Öffnungs- und Lesefehler auf stderr, Pfadangabe, fehlende Hash-Ausgabe und Fehlerstatus testen.
- [x] 1.4 Eine kurze `README.md` mit Voraussetzungen, Aufrufbeispiel, Ausgabe, Fehlerverhalten und Testkommando erstellen; den dokumentierten Aufruf mit einer Beispieldatei prüfen.

## 2. Integration

- [x] 2.1 Die gesamte Testsuite mit `python3 -m unittest discover` ausführen und sicherstellen, dass keine externen Pakete erforderlich sind.
