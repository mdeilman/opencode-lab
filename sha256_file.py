"""Berechnet SHA-256-Prüfsummen von Dateien."""

import argparse
import hashlib
import sys


BLOCK_SIZE = 64 * 1024


def hash_file(path):
    """Berechne den SHA-256-Hash einer Datei mit begrenztem Speicherbedarf."""
    digest = hashlib.sha256()
    with open(path, "rb") as file:
        while block := file.read(BLOCK_SIZE):
            digest.update(block)
    return digest.hexdigest()


def main(argv=None):
    parser = argparse.ArgumentParser(description="SHA-256-Hash einer Datei berechnen.")
    parser.add_argument("datei", help="Pfad zur Datei")
    args = parser.parse_args(argv)
    try:
        result = hash_file(args.datei)
    except OSError as error:
        print(f"Fehler beim Lesen von {args.datei!r}: {error.strerror or error}", file=sys.stderr)
        return 1
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
