# SHA-256-Dateihash

Das Kommandozeilenwerkzeug berechnet den SHA-256-Hash einer Datei und liest auch große Dateien blockweise. Es benötigt Python 3.8 oder neuer und ausschließlich die Python-Standardbibliothek.

## Verwendung

```sh
python3 sha256_file.py pfad/zur/datei
```

Der Hash wird als 64 kleingeschriebene Hexadezimalzeichen auf der Standardausgabe ausgegeben. Bei Erfolg ist der Exit-Status 0. Fehlende oder nicht lesbare Dateien erzeugen eine Fehlermeldung auf der Standardfehlerausgabe und einen Exit-Status ungleich 0. Pfade mit Leerzeichen müssen in der Shell zitiert werden.

## Tests

```sh
python3 -m unittest discover
```
